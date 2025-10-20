# PayShield Agent - Usage Guide

## 🚀 Quick Start

### 1. Start the Intake Agent

The intake agent processes incoming invoice data. To start it:

```bash
# Activate virtual environment
source venv/bin/activate

# Run the agent
python agents/intake_agent/intake_agent.py
```

The agent will start on **port 8001** and display:
- **Agent Address**: `agent1qdz9khs68u5vx2a0ae8uzdzuf9cjvzks32e3vke5a203wga7uy34xjcdwpu`
- **HTTP Endpoint**: `http://0.0.0.0:8001`
- **Agent Inspector URL**: For real-time monitoring

### 2. Monitor Your Agent

Once running, you can monitor your agent at:
```
https://agentverse.ai/inspect/?uri=http%3A//127.0.0.1%3A8001&address=agent1qdz9khs68u5vx2a0ae8uzdzuf9cjvzks32e3vke5a203wga7uy34xjcdwpu
```

## 💡 How to Use the Agent

### Method 1: Send Test Invoice (Recommended for Testing)

Use the provided test script:

```bash
# In a new terminal window
cd /Users/macbookair/payshield
source venv/bin/activate
python examples/test_invoice.py
```

This will:
1. Create a test client agent
2. Send a sample invoice to the intake agent
3. Display the confirmation response

### Method 2: Create Your Own Client

Here's how to interact with the agent programmatically:

```python
from uagents import Agent, Context, Model

# Define the Invoice model (must match the agent's model)
class Invoice(Model):
    invoice_id: str
    vendor: str
    amount: float

# Create your client agent
my_agent = Agent(name="my_client", port=8003, seed="my_seed")

# Intake agent address
INTAKE_AGENT = "agent1qdz9khs68u5vx2a0ae8uzdzuf9cjvzks32e3vke5a203wga7uy34xjcdwpu"

@my_agent.on_event("startup")
async def send_invoice(ctx: Context):
    invoice = Invoice(
        invoice_id="INV-1001",
        vendor="Acme Corp",
        amount=1000.00
    )
    await ctx.send(INTAKE_AGENT, invoice)

@my_agent.on_message(Invoice)
async def on_response(ctx: Context, sender: str, msg: Invoice):
    ctx.logger.info(f"Invoice {msg.invoice_id} processed!")

if __name__ == "__main__":
    my_agent.run()
```

### Method 3: HTTP API

You can also interact via HTTP POST to the agent's endpoint:

```bash
curl -X POST http://localhost:8001/submit \
  -H "Content-Type: application/json" \
  -d '{
    "invoice_id": "INV-2001",
    "vendor": "Tech Solutions Inc",
    "amount": 750.50
  }'
```

## 📊 Understanding the Workflow

```
┌─────────────┐         ┌──────────────────┐         ┌─────────────┐
│   Client    │ ──────> │  Intake Agent    │ ──────> │  Response   │
│  (You/App)  │ Invoice │   (Port 8001)    │ Confirm │ (to Client) │
└─────────────┘         └──────────────────┘         └─────────────┘
                               │
                               ├──> Knowledge Agent (MeTTa)
                               ├──> Payment Orchestrator
                               └──> Audit Agent
```

## 🔑 Key Information

- **Agent Name**: `intake_agent`
- **Agent Address**: `agent1qdz9khs68u5vx2a0ae8uzdzuf9cjvzks32e3vke5a203wga7uy34xjcdwpu`
- **Port**: `8001`
- **Endpoint**: `http://localhost:8001/submit`
- **Seed Phrase**: `intake_agent_seed_phrase`

## 📝 Invoice Message Format

```python
{
    "invoice_id": str,    # Unique invoice identifier (e.g., "INV-1001")
    "vendor": str,        # Vendor name (e.g., "Acme Corp")
    "amount": float       # Invoice amount in USD (e.g., 500.00)
}
```

## 🧪 Testing Examples

### Example 1: Simple Invoice
```python
Invoice(
    invoice_id="INV-1042",
    vendor="Travel Agency",
    amount=420.00
)
```

### Example 2: Large Invoice
```python
Invoice(
    invoice_id="INV-2050",
    vendor="Enterprise Software Ltd",
    amount=5000.00
)
```

### Example 3: Multiple Invoices
```python
invoices = [
    Invoice(invoice_id="INV-001", vendor="Vendor A", amount=100.00),
    Invoice(invoice_id="INV-002", vendor="Vendor B", amount=200.00),
    Invoice(invoice_id="INV-003", vendor="Vendor C", amount=300.00),
]

for invoice in invoices:
    await ctx.send(INTAKE_AGENT, invoice)
```

## 🛠️ Troubleshooting

### Agent Not Starting?
```bash
# Check if port 8001 is available
lsof -i :8001

# Kill existing process if needed
pkill -f intake_agent

# Restart the agent
python agents/intake_agent/intake_agent.py
```

### Check Agent Status
```bash
# View recent logs
tail -f agent.log

# Check if process is running
ps aux | grep intake_agent
```

### Insufficient Funds Warning
The warning about "insufficient funds to register on Almanac contract" is **normal** for local development. Your agent still works locally! To register on the public network:
1. Visit [Agentverse.ai](https://agentverse.ai)
2. Add testnet funds to your agent address
3. Enable the Chat Protocol

## 🌟 Next Steps

1. **Test locally**: Run `python examples/test_invoice.py`
2. **Build integrations**: Connect with Slack, Sheets, Email via MCP adapters
3. **Deploy to production**: Register on Agentverse.ai
4. **Add more agents**: Build the knowledge, payment, and audit agents
5. **Integrate MeTTa**: Use the knowledge graph for compliance reasoning

## 📚 Additional Resources

- [uAgents Documentation](https://docs.fetch.ai/uAgents)
- [Agentverse Platform](https://agentverse.ai)
- [MeTTa Documentation](https://singularitynet.io)
- [PayShield GitHub](https://github.com/yourusername/payshield)

## 💬 Support

Need help? Check the agent inspector logs or view the README.md for more information.

