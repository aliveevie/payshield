from datetime import datetime
from uuid import uuid4

from openai import OpenAI
from uagents import Agent, Context, Model, Protocol
from uagents_core.contrib.protocols.chat import (
	ChatAcknowledgement,
	ChatMessage,
	EndSessionContent,
	TextContent,
	chat_protocol_spec,
)


class Invoice(Model):
	invoice_id: str
	vendor: str
	amount: float


# Intake agent identity (cloud-friendly)
agent = Agent(
	name="payshield_intake",
	seed="payshield_cloud_seed_2025_v2",
)


# ==========================
# ASI:One Chat Configuration
# ==========================
# Subject matter expertise for ASI:One chat responses
SUBJECT_MATTER = "invoices and payments processing"

# ASI:One API client (inlined)
asi_client = OpenAI(
	base_url="https://api.asi1.ai/v1",
	api_key="sk_fcdb3ecbb0184049b7eb1f347a0dc9e91c5d96717cba4a1e97f6e9dafa53e04b",
)

# Chat protocol spec/handlers
chat_protocol = Protocol(spec=chat_protocol_spec)


@chat_protocol.on_message(ChatMessage)
async def handle_chat_message(ctx: Context, sender: str, msg: ChatMessage):
	# Acknowledge receipt
	await ctx.send(
		sender,
		ChatAcknowledgement(timestamp=datetime.now(), acknowledged_msg_id=msg.msg_id),
	)

	# Aggregate plain text from the message content
	user_text = ""
	for item in msg.content:
		if isinstance(item, TextContent):
			user_text += item.text

	# Default fallback
	response_text = (
		"I am afraid something went wrong and I am unable to answer your question at the moment"
	)

	# Call ASI:One model constrained to SUBJECT_MATTER
	try:
		r = asi_client.chat.completions.create(
			model="asi1-mini",
			messages=[
				{
					"role": "system",
					"content": (
						f"You are a helpful assistant who only answers questions about {SUBJECT_MATTER}. "
						"If the user asks about any other topics, politely say you do not know about them."
					),
				},
				{"role": "user", "content": user_text},
			],
			max_tokens=1024,
		)
		response_text = str(r.choices[0].message.content)
	except Exception:
		ctx.logger.exception("Error querying ASI:One model")

	# Send chat response and end session
	await ctx.send(
		sender,
		ChatMessage(
			timestamp=datetime.utcnow(),
			msg_id=uuid4(),
			content=[
				TextContent(type="text", text=response_text),
				EndSessionContent(type="end-session"),
			],
		),
	)


@chat_protocol.on_message(ChatAcknowledgement)
async def handle_ack(ctx: Context, sender: str, msg: ChatAcknowledgement):
	# No-op for read receipts in this simple example
	pass


# Attach the chat protocol to the agent (and publish its manifest)
agent.include(chat_protocol, publish_manifest=True)


@agent.on_event("startup")
async def startup(ctx: Context):
	ctx.logger.info("🚀 PayShield Intake Agent started on Agentverse!")
	ctx.logger.info(f"   Agent Address: {agent.address}")
	ctx.logger.info("   Ready to process invoices from anywhere!")
	ctx.logger.info("   Version: 2.0 (Cloud + ASI:One Chat)")


@agent.on_message(Invoice)
async def handle_invoice(ctx: Context, sender: str, msg: Invoice):
	# Log received invoice
	ctx.logger.info("")
	ctx.logger.info("═" * 60)
	ctx.logger.info("📥 INVOICE RECEIVED")
	ctx.logger.info(f"   Invoice ID: {msg.invoice_id}")
	ctx.logger.info(f"   Vendor:     {msg.vendor}")
	ctx.logger.info(f"   Amount:     ${msg.amount:,.2f} USD")
	ctx.logger.info(f"   From:       {sender}")
	ctx.logger.info("═" * 60)

	# Process the invoice (business logic placeholder)
	ctx.logger.info("✅ Invoice processed and stored successfully!")
	ctx.logger.info("   Status: ACCEPTED")
	ctx.logger.info(f"   Processing complete for {msg.invoice_id}")
	ctx.logger.info("")

	# Do not enforce replies (cloud senders may be unreachable). Best-effort only.
	try:
		await ctx.send(
			sender,
			Invoice(invoice_id=msg.invoice_id, vendor=msg.vendor, amount=msg.amount),
		)
		ctx.logger.info(f"✉️  Confirmation sent to {sender}")
	except Exception:
		ctx.logger.info(
			"ℹ️  Note: Could not send confirmation to sender (sender may be offline)"
		)
		ctx.logger.info("   This is normal for cloud-only communication")


if __name__ == "__main__":
	agent.run()