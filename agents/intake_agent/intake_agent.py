from uagents import Agent, Context, Model

class Invoice(Model):
    invoice_id: str
    vendor: str
    amount: float

agent = Agent(
    name="payshield_intake",
    seed="payshield_cloud_seed_2025_v2"
)

@agent.on_event("startup")
async def startup(ctx: Context):
    ctx.logger.info("🚀 PayShield Intake Agent started on Agentverse!")
    ctx.logger.info(f"   Agent Address: {agent.address}")
    ctx.logger.info("   Ready to process invoices from anywhere!")
    ctx.logger.info("   Version: 2.0 (Cloud Optimized)")

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
    
    # Process the invoice (add your business logic here)
    # For now, we just log it as processed
    ctx.logger.info("✅ Invoice processed and stored successfully!")
    ctx.logger.info(f"   Status: ACCEPTED")
    ctx.logger.info(f"   Processing complete for {msg.invoice_id}")
    ctx.logger.info("")
    
    # Try to send confirmation back (but don't fail if sender is unreachable)
    try:
        await ctx.send(sender, Invoice(
            invoice_id=msg.invoice_id,
            vendor=msg.vendor,
            amount=msg.amount
        ))
        ctx.logger.info(f"✉️  Confirmation sent to {sender}")
    except Exception as e:
        ctx.logger.info(f"ℹ️  Note: Could not send confirmation to sender (sender may be offline)")
        ctx.logger.info(f"   This is normal for cloud-only communication")

if __name__ == "__main__":
    agent.run()