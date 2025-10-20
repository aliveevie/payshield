#!/usr/bin/env python3
"""
Terminal CLI to chat with the PayShield cloud agent on Agentverse.
Commands:
  - send: send invoice interactively
  - verify: verify an invoice id
  - quit/exit: leave the CLI
"""

import sys
from uagents import Agent, Context
from agents.intake_agent.models import Invoice, Action

CLOUD_AGENT = "agent1q0c8tjx6932mn999jj4htx7wt2x0r7p7jem4hezuf2z8nsx7dwx5z780k7h"

cli = Agent(name="payshield_cli", seed="payshield_cli_seed_2025")


def prompt(text: str) -> str:
    print(text, end="", flush=True)
    return sys.stdin.readline().strip()


@cli.on_event("startup")
async def main(ctx: Context):
    print("\n=== PayShield Cloud CLI ===")
    print(f"Target: {CLOUD_AGENT}\n")
    while True:
        cmd = prompt("Command [send|verify|quit]: ").lower()
        if cmd in {"quit", "exit"}:
            print("Goodbye!")
            sys.exit(0)
        if cmd == "send":
            invoice_id = prompt("Invoice ID: ")
            vendor = prompt("Vendor: ")
            amount_str = prompt("Amount (e.g., 420.00): ")
            try:
                amount = float(amount_str)
            except Exception:
                print("Invalid amount. Try again.\n")
                continue
            action = Action(
                kind="send_invoice",
                payload={"invoice_id": invoice_id, "vendor": vendor, "amount": amount},
            )
            await ctx.send(CLOUD_AGENT, action)
            print("✅ Sent invoice to cloud agent. Check Agentverse logs.\n")
        elif cmd == "verify":
            invoice_id = prompt("Invoice ID to verify: ")
            action = Action(kind="verify_invoice", payload={"invoice_id": invoice_id})
            await ctx.send(CLOUD_AGENT, action)
            print("✅ Sent verification request. Check Agentverse logs.\n")
        else:
            print("Unknown command. Use send, verify, quit.\n")


if __name__ == "__main__":
    print("Starting CLI... Press Ctrl+C to exit")
    cli.run()
