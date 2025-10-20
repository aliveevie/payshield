#!/usr/bin/env python3
"""
Chat with PayShield cloud agent on Agentverse
This script demonstrates how to send messages to your deployed agent
Note: This is one-way communication - we send to cloud, no response needed
"""

from uagents import Agent, Context, Model
import asyncio

class Invoice(Model):
    invoice_id: str
    vendor: str
    amount: float

class Message(Model):
    text: str

# Your chat agent (runs locally, no endpoint needed for one-way communication)
chat_client = Agent(
    name="chat_client_cloud",
    seed="chat_client_cloud_seed_2025"
    # No port or endpoint needed - we're just sending, not receiving
)

# Your cloud agent on Agentverse
PAYSHIELD_CLOUD_AGENT = "agent1qgl23rpuj06tz95rgzmcmjncl8mjkfv570vq34gsh5ts49rxpdpjgdsclex"

@chat_client.on_event("startup")
async def start_chat(ctx: Context):
    """Send various messages to the cloud agent"""
    ctx.logger.info("💬 Starting chat with PayShield cloud agent...")
    ctx.logger.info(f"   Target: {PAYSHIELD_CLOUD_AGENT}")
    ctx.logger.info("")
    
    # Send some invoices
    invoices = [
        Invoice(
            invoice_id="INV-CHAT-001",
            vendor="Tech Startup Inc",
            amount=3500.00
        ),
        Invoice(
            invoice_id="INV-CHAT-002",
            vendor="Software Solutions Ltd",
            amount=1250.50
        ),
        Invoice(
            invoice_id="INV-CHAT-003",
            vendor="Cloud Services Pro",
            amount=999.99
        ),
    ]
    
    for invoice in invoices:
        ctx.logger.info(f"📤 Sending Invoice: {invoice.invoice_id}")
        ctx.logger.info(f"   Vendor: {invoice.vendor}")
        ctx.logger.info(f"   Amount: ${invoice.amount}")
        await ctx.send(PAYSHIELD_CLOUD_AGENT, invoice)
        ctx.logger.info("")
    
    ctx.logger.info("✅ All messages sent to cloud agent!")
    ctx.logger.info("")
    ctx.logger.info("🔍 Check the cloud agent logs to see them being processed:")
    ctx.logger.info("   https://agentverse.ai/agents/agent1qgl23rpuj06tz95rgzmcmjncl8mjkfv570vq34gsh5ts49rxpdpjgdsclex")
    ctx.logger.info("")
    ctx.logger.info("💡 The cloud agent is processing your invoices right now!")
    ctx.logger.info("   (No local response needed - the cloud handles everything!)")
    ctx.logger.info("")
    
    # Wait a bit then exit gracefully
    await asyncio.sleep(3)
    ctx.logger.info("✨ Done! Check Agentverse dashboard for processing logs.")
    import sys
    sys.exit(0)

if __name__ == "__main__":
    print("\n" + "="*70)
    print("💬 Chat with PayShield Cloud Agent")
    print("="*70)
    print("Connecting to cloud-hosted agent on Agentverse...")
    print(f"Target: {PAYSHIELD_CLOUD_AGENT}")
    print("="*70 + "\n")
    
    chat_client.run()

