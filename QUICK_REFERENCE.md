# PayShield Agent - Quick Reference Card

## 🎯 Agent Information
```
Name:     intake_agent
Address:  agent1q0c8tjx6932mn999jj4htx7wt2x0r7p7jem4hezuf2z8nsx7dwx5z780k7h
Port:     8001
Endpoint: http://localhost:8001/submit
Status:   ✅ Running
```

## 🚀 Common Commands

### Start Agent
```bash
cd /Users/macbookair/payshield
source venv/bin/activate
python agents/intake_agent/intake_agent.py
```

### Send Test Invoice
```bash
cd /Users/macbookair/payshield
source venv/bin/activate
python examples/test_invoice.py
```

### Send Multiple Invoices
```bash
python examples/send_invoice_simple.py
```

### Check Agent Status
```bash
# See if agent is running
ps aux | grep intake_agent

# View logs in real-time
tail -f agent.log

# View last 20 log lines
tail -20 agent.log
```

### Stop Agent
```bash
# Find and stop the agent process
pkill -f intake_agent
```

## 📊 Monitor Your Agent

**Agent Inspector (Real-time monitoring):**
```
https://agentverse.ai/inspect/?uri=http%3A//127.0.0.1%3A8001&address=agent1q0c8tjx6932mn999jj4htx7wt2x0r7p7jem4hezuf2z8nsx7dwx5z780k7h
```

## 💡 Quick Test
```python
from uagents import Agent, Context, Model

class Invoice(Model):
    invoice_id: str
    vendor: str
    amount: float

agent = Agent(name="test", port=9999, seed="test")
INTAKE = "agent1q0c8tjx6932mn999jj4htx7wt2x0r7p7jem4hezuf2z8nsx7dwx5z780k7h"

@agent.on_event("startup")
async def send(ctx: Context):
    await ctx.send(INTAKE, Invoice(
        invoice_id="INV-123",
        vendor="Vendor XYZ",
        amount=500.00
    ))

agent.run()
```

## 🔍 Troubleshooting

| Issue | Solution |
|-------|----------|
| Port 8001 in use | `lsof -i :8001` then `kill <PID>` |
| Agent not responding | Check `tail -f agent.log` |
| Import errors | `source venv/bin/activate` |
| Connection refused | Ensure agent is running |

## 📝 Invoice Format
```json
{
  "invoice_id": "INV-1001",  // Required: string
  "vendor": "Company Name",  // Required: string
  "amount": 999.99          // Required: float
}
```

## 🎓 Examples

**Single Invoice:**
```python
Invoice(invoice_id="INV-001", vendor="Acme Corp", amount=100.00)
```

**Multiple Invoices:**
```python
for i in range(5):
    await ctx.send(INTAKE, Invoice(
        invoice_id=f"INV-{i:03d}",
        vendor=f"Vendor-{i}",
        amount=i * 100.0
    ))
```

## 📚 Files

- `agents/intake_agent/intake_agent.py` - Main agent code
- `examples/test_invoice.py` - Test client
- `examples/send_invoice_simple.py` - Batch sender
- `USAGE_GUIDE.md` - Full documentation
- `agent.log` - Runtime logs

## 🌐 URLs

- **Agent Inspector**: https://agentverse.ai/inspect/?uri=http%3A//127.0.0.1%3A8001&address=agent1q0c8tjx6932mn999jj4htx7wt2x0r7p7jem4hezuf2z8nsx7dwx5z780k7h
- **Agentverse**: https://agentverse.ai
- **Docs**: https://docs.fetch.ai/uAgents

---

**Made with ❤️ by PayShield | MIT License © 2025**

