#!/usr/bin/env python3
"""
Demo: Local agent-to-agent communication
For cloud communication, see: chat_with_cloud_agent.py
"""

from uagents import Agent, Context, Model

class Message(Model):
    text: str

class Invoice(Model):
    invoice_id: str
    vendor: str
    amount: float

# Option 1: Local agents (Alice and Bob)
alice = Agent(name="alice", seed="alice_seed", port=8002, endpoint=["http://localhost:8002/submit"])
bob = Agent(name="bob", seed="bob_seed", port=8003, endpoint=["http://localhost:8003/submit"])

# Option 2: Cloud agent address (PayShield on Agentverse)
PAYSHIELD_CLOUD = "agent1q0c8tjx6932mn999jj4htx7wt2x0r7p7jem4hezuf2z8nsx7dwx5z780k7h"

@alice.on_event("startup")
async def start(ctx: Context):
    ctx.logger.info("Alice started.")
    
    # Send message to Bob (local)
    ctx.logger.info("📤 Sending message to Bob (local)...")
    await ctx.send(bob.address, Message(text="Hello Bob!"))
    
    # Optionally send invoice to cloud agent
    # Uncomment these lines to test cloud communication:
    # ctx.logger.info("📤 Sending invoice to PayShield cloud agent...")
    # await ctx.send(PAYSHIELD_CLOUD, Invoice(
    #     invoice_id="INV-DEMO-001",
    #     vendor="Demo Company",
    #     amount=500.00
    # ))

@bob.on_message(Message)
async def on_message(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"✅ Bob received message from {sender}: {msg.text}")

@alice.on_message(Invoice)
async def alice_on_invoice(ctx: Context, sender: str, msg: Invoice):
    ctx.logger.info(f"✅ Alice received invoice confirmation: {msg.invoice_id} for ${msg.amount}")

if __name__ == "__main__":
    print("\n" + "="*60)
    print("PayShield - Local Agent Demo")
    print("="*60)
    print("Alice and Bob will communicate locally.")
    print("For cloud communication, use: python examples/chat_with_cloud_agent.py")
    print("="*60 + "\n")
    
    alice.run()
    bob.run()
