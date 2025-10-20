# PayShield - Autonomous Finance Agent System

![tag:innovationlab](https://img.shields.io/badge/innovationlab-3D8BD3)
![tag:hackathon](https://img.shields.io/badge/hackathon-5F43F1)

PayShield is an autonomous agent-based system built using **Fetch.ai uAgents framework** and **SingularityNET MeTTa Knowledge Graph**.  
It automates invoice processing, compliance reasoning, and payment execution — all through ASI:One Chat.

## 🤖 Deployed Agents

### PayShield Intake Agent
- **Name**: PayShield Intake Agent
- **Address**: `agent1q0c8tjx6932mn999jj4htx7wt2x0r7p7jem4hezuf2z8nsx7dwx5z780k7h`
- **Status**: ✅ Live on Agentverse (Testnet)
- **Agentverse Profile**: [View Agent](https://agentverse.ai/agents/details/agent1q0c8tjx6932mn999jj4htx7wt2x0r7p7jem4hezuf2z8nsx7dwx5z780k7h/profile)
- **Function**: Receives, validates, and processes invoice data from various sources
- **Chat Protocol**: Enabled for ASI:One integration

### Local Development Agent
- **Address**: `agent1q0c8tjx6932mn999jj4htx7wt2x0r7p7jem4hezuf2z8nsx7dwx5z780k7h`
- **Use**: Local testing and development

## Project Structure
```
/payshield
  /agents
    intake_agent/           # parses and receives invoice data
    knowledge_metta_agent/  # stores and reasons with MeTTa KG
    payment_orchestrator/   # executes and tracks payments
    audit_agent/            # logs all activities
    mcp_adapter_agent/      # bridges with Slack/Sheets/Email tools
  /metta                    # contains KG schema and policy rules
  /examples                 # sample communication scripts
```

## Quick Start
1. Clone the repo and install dependencies
```bash
python -m venv venv
source venv/bin/activate
pip install uagents
```

2. Run your first local agent
```bash
python agents/intake_agent/intake_agent.py
```

3. Register on [Agentverse.ai](https://Agentverse.ai) and enable Chat Protocol.
4. View live logs and interactions via Agent Inspector.

## 🛠️ Technologies Used

### ASI Alliance Technologies
- **uAgents (Fetch.ai)** - Agent framework for autonomous communication
- **Agentverse** - Cloud hosting and agent orchestration
- **ASI:One Chat Protocol** - Enabled for voice/text interactions
- **MeTTa (SingularityNET)** - Knowledge graph for compliance reasoning
- **Almanac** - Agent discovery and registration

### Additional Integrations
- **MCP (Model Context Protocol)** - Integration with external tools (Slack, Google Sheets, Email)
- **Python 3.13+** - Core implementation language

## 📋 Extra Resources Required

1. **Python 3.13+**: [Download here](https://www.python.org/downloads/)
2. **Agentverse Account**: [Sign up at agentverse.ai](https://agentverse.ai)
3. **API Token**: Get from [Agentverse API Keys](https://agentverse.ai/profile/api-keys)

All dependencies are listed in the project and installed via:
```bash
pip install uagents
```

## 🚀 Demo Commands

### Test Local Agent
```bash
python examples/test_invoice.py
```

### Test Agentverse Agent
```bash
python examples/test_agentverse_agent.py
```

### Send Multiple Invoices
```bash
python examples/send_invoice_simple.py
```

## 📖 Documentation

- **[AGENTVERSE_DEPLOYMENT.md](AGENTVERSE_DEPLOYMENT.md)** - Complete deployment guide with agent details
- **[USAGE_GUIDE.md](USAGE_GUIDE.md)** - Comprehensive usage instructions and API reference
- **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)** - Quick command reference card

## 🎯 Key Features

✅ **Real-time Invoice Processing** - Automated invoice intake and validation  
✅ **Agentverse Integration** - Cloud-hosted, 24/7 availability  
✅ **ASI:One Chat Enabled** - Interactive voice/text interface  
✅ **MeTTa Knowledge Graph** - Intelligent compliance reasoning  
✅ **Multi-Agent Architecture** - Modular, scalable design  
✅ **MCP Integration** - Connect to Slack, Sheets, and more  

## 🏆 Hackathon Submission

This project is submitted to the ASI Alliance Innovation Lab Hackathon.

### Innovation Highlights
- **Autonomous Finance**: First agent-based invoice processing system on Fetch.ai
- **Hybrid Intelligence**: Combines uAgents coordination with MeTTa reasoning
- **Real-World Application**: Solves actual business process automation needs
- **Multi-Protocol**: Supports both direct agent communication and human interaction via ASI:One

### Technical Implementation
- ✅ Agents registered on Agentverse
- ✅ Chat Protocol enabled for ASI:One
- ✅ uAgents framework for agent coordination
- ✅ MeTTa Knowledge Graph integration for compliance
- ✅ Tested and verified with real invoice processing

## 🎬 Demo Video

[Demo video link will be added here]

## 📞 Contact & Support

**Author**: Ibrahim Abdulkarim  
**Project**: PayShield - Autonomous Finance Agent System  
**Category**: Innovation Lab  

## 📄 License
MIT © 2025 PayShield by Ibrahim Abdulkarim
