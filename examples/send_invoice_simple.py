#!/usr/bin/env python3
"""
Simple invoice sender - Send invoices to PayShield cloud agent
Usage: python examples/send_invoice_simple.py
"""

from uagents import Agent, Context, Model
import asyncio

class Invoice(Model):
    invoice_id: str
    vendor: str
    amount: float

# Your client agent (no endpoint needed for cloud communication)
sender = Agent(name="invoice_sender_cloud", seed="sender_seed_cloud_2025")

# PayShield cloud agent on Agentverse
CLOUD_AGENT = "agent1qgl23rpuj06tz95rgzmcmjncl8mjkfv570vq34gsh5ts49rxpdpjgdsclex"

@sender.on_event("startup")
async def send_invoices(ctx: Context):
    """Send sample invoices to PayShield"""
    
    # Sample invoices
    invoices = [
        Invoice(invoice_id="INV-2001", vendor="Office Supplies Co", amount=150.50),
        Invoice(invoice_id="INV-2002", vendor="Cloud Services Inc", amount=899.99),
        Invoice(invoice_id="INV-2003", vendor="Marketing Agency", amount=2500.00),
    ]
    
    ctx.logger.info("📤 Sending invoices to PayShield cloud agent...")
    
    for invoice in invoices:
        await ctx.send(CLOUD_AGENT, invoice)
        ctx.logger.info(f"   ✉️  Sent: {invoice.invoice_id} | {invoice.vendor} | ${invoice.amount}")
    
    ctx.logger.info("✅ All invoices sent successfully!")
    ctx.logger.info("")
    ctx.logger.info("🔍 Check cloud processing logs:")
    ctx.logger.info("   https://agentverse.ai/agents/agent1qgl23rpuj06tz95rgzmcmjncl8mjkfv570vq34gsh5ts49rxpdpjgdsclex")
    ctx.logger.info("")
    
    # Wait then exit
    await asyncio.sleep(3)
    ctx.logger.info("✨ Done! Your cloud agent is processing the invoices.")
    import sys
    sys.exit(0)

if __name__ == "__main__":
    print("\n" + "="*70)
    print("PayShield - Cloud Invoice Sender")
    print("="*70)
    print("Sending invoices to cloud agent on Agentverse...")
    print(f"Target: {CLOUD_AGENT}")
    print("="*70 + "\n")
    sender.run()

