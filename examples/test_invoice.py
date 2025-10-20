#!/usr/bin/env python3
"""
Test script to send invoice messages to the intake agent.
This demonstrates how to interact with the PayShield intake agent.
"""

from uagents import Agent, Context, Model
import asyncio

class Invoice(Model):
    invoice_id: str
    vendor: str
    amount: float

# Create a test client agent
client = Agent(
    name="test_client",
    port=8002,
    seed="test_client_seed_phrase",
    endpoint=["http://localhost:8002/submit"]
)

# The intake agent's address (from the logs)
INTAKE_AGENT_ADDRESS = "agent1q0c8tjx6932mn999jj4htx7wt2x0r7p7jem4hezuf2z8nsx7dwx5z780k7h"

@client.on_event("startup")
async def send_test_invoice(ctx: Context):
    """Send a test invoice to the intake agent"""
    ctx.logger.info("Test client started. Sending test invoice...")
    
    # Create a sample invoice
    test_invoice = Invoice(
        invoice_id="INV-TEST-001",
        vendor="Test Vendor Corp",
        amount=250.00
    )
    
    # Send it to the intake agent
    await ctx.send(INTAKE_AGENT_ADDRESS, test_invoice)
    ctx.logger.info(f"Sent invoice: {test_invoice.invoice_id} for ${test_invoice.amount}")

@client.on_message(Invoice)
async def handle_response(ctx: Context, sender: str, msg: Invoice):
    """Handle the response from the intake agent"""
    ctx.logger.info(f"✅ Received confirmation from intake agent!")
    ctx.logger.info(f"   Invoice ID: {msg.invoice_id}")
    ctx.logger.info(f"   Vendor: {msg.vendor}")
    ctx.logger.info(f"   Amount: ${msg.amount}")
    
    # Exit after receiving response
    import sys
    sys.exit(0)

if __name__ == "__main__":
    print("=" * 60)
    print("PayShield Invoice Test Client")
    print("=" * 60)
    print(f"Sending test invoice to intake agent...")
    print(f"Intake Agent Address: {INTAKE_AGENT_ADDRESS}")
    print("=" * 60)
    
    client.run()

