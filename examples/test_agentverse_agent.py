#!/usr/bin/env python3
"""
Test script to send invoices to the PayShield agent deployed on Agentverse.
This demonstrates how to interact with your cloud-hosted agent.
Note: One-way communication - sends to cloud, no local response needed!
"""

from uagents import Agent, Context, Model
import asyncio

class Invoice(Model):
    invoice_id: str
    vendor: str
    amount: float

# Create a test client agent (no endpoint needed for one-way communication)
client = Agent(
    name="agentverse_test_client",
    seed="agentverse_test_seed_2025"
    # No port or endpoint - we're just sending to cloud, not receiving responses
)

# Your PayShield agent on Agentverse
PAYSHIELD_AGENTVERSE = "agent1q0c8tjx6932mn999jj4htx7wt2x0r7p7jem4hezuf2z8nsx7dwx5z780k7h"

@client.on_event("startup")
async def send_test_invoice(ctx: Context):
    """Send test invoices to the Agentverse-hosted agent"""
    ctx.logger.info("🚀 Connecting to PayShield agent on Agentverse...")
    ctx.logger.info(f"   Target: {PAYSHIELD_AGENTVERSE}")
    
    # Sample invoices to test
    invoices = [
        Invoice(invoice_id="INV-AV-001", vendor="Cloud Services Pro", amount=1299.99),
        Invoice(invoice_id="INV-AV-002", vendor="Marketing Solutions", amount=2500.00),
        Invoice(invoice_id="INV-AV-003", vendor="Office Equipment Ltd", amount=450.75),
    ]
    
    for invoice in invoices:
        ctx.logger.info(f"📤 Sending: {invoice.invoice_id} | {invoice.vendor} | ${invoice.amount}")
        await ctx.send(PAYSHIELD_AGENTVERSE, invoice)
    
    ctx.logger.info("✅ All invoices sent to Agentverse agent!")
    ctx.logger.info("")
    ctx.logger.info("🔍 View processing logs on Agentverse:")
    ctx.logger.info("   https://agentverse.ai/agents/agent1q0c8tjx6932mn999jj4htx7wt2x0r7p7jem4hezuf2z8nsx7dwx5z780k7h")
    ctx.logger.info("")
    ctx.logger.info("💡 The cloud agent is processing them right now!")
    ctx.logger.info("   (Check the Agentverse dashboard for real-time logs)")
    ctx.logger.info("")
    
    # Wait a bit then exit gracefully
    await asyncio.sleep(3)
    ctx.logger.info("✨ Test complete! Your invoices are being processed on the cloud.")
    import sys
    sys.exit(0)

if __name__ == "__main__":
    print("\n" + "="*70)
    print("PayShield Agentverse Integration Test")
    print("="*70)
    print("Testing communication with cloud-hosted agent...")
    print(f"Target Agent: {PAYSHIELD_AGENTVERSE}")
    print("="*70 + "\n")
    
    client.run()

