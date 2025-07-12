# Xandeum AI Bot 🤖

A comprehensive Discord AI bot for the Xandeum blockchain project, providing real-time information, technical support, and AI-powered assistance.

## 🌟 Features

### **Project Information**
- Real-time project data and statistics
- Technical specifications and documentation links
- Token information and use cases
- Innovation eras roadmap

### **Node Support**
- **pNode Support**: Setup guides, hardware requirements, port testing
- **vNode Support**: DevNet integration, validator setup, monitoring
- **Port Checker**: Test connectivity for node ports

### **DAO Governance**
- DAO platform integration
- Voting information and proposal details
- Governance participation guidance

### **AI-Powered Responses**
- Groq AI integration with Llama 3.1-8b-instant model
- Context-aware responses about Xandeum
- Technical support and troubleshooting

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Discord Bot Token
- Groq API Key (for AI features)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/xandeum-ai-bot.git
cd xandeum-ai-bot
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**
```bash
cp .env.example .env
# Edit .env with your tokens
```

4. **Run the bot**
```bash
python bot.py
```

## 📋 Commands

### **Information Commands**
- `!overview` - Project overview
- `!technical` - Technical specifications
- `!token` - Token information
- `!eras` - Innovation eras roadmap
- `!docs` - Documentation links

### **Real-time Data**
- `!price` - Current XAN price
- `!stake` - Staking information
- `!validators` - Active validators
- `!governance` - Governance proposals
- `!network` - Network status

### **pNode Commands**
- `!pnode` - pNode information
- `!pnode-setup` - Setup guide
- `!pnode-update` - Update instructions
- `!pnode-ports <IP>` - Test port connectivity

### **vNode Commands**
- `!vnode` - vNode information
- `!vnode-setup` - Setup guide
- `!vnode-update` - Update instructions
- `!vnode-ports <IP>` - Test port connectivity
- `!devnet` - DevNet information

### **DAO Commands**
- `!dao` - DAO information
- `!dao-proposals` - Current proposals
- `!dao-vote` - Voting information

### **AI Features**
- Mention the bot or use `!ai <question>` for AI-powered responses
- Ask about Xandeum project details
- Get technical support and guidance

## 🏗️ Architecture

```
xandeum_ai_bot/
├── bot.py                 # Main bot file
├── config/
│   ├── __init__.py
│   ├── project_info.py    # Project configuration
│   └── apis.py           # API client
├── commands/
│   ├── __init__.py
│   └── bot_commands.py   # Command handlers
├── utils/
│   ├── __init__.py
│   ├── ai_handler.py     # AI integration
│   └── port_checker.py   # Port testing
├── knowledge_base/        # AI knowledge base
├── requirements.txt
├── .env.example
└── README.md
```

## 🔧 Configuration

### Environment Variables
```bash
DISCORD_TOKEN=your_discord_bot_token
GROQ_API_KEY=your_groq_api_key
```

### Project Information
All project data is stored in `config/project_info.py`:
- Official links and resources
- Technical specifications
- Node requirements and guides
- DAO governance information
- FAQ and common questions

## 🤖 AI Integration

The bot uses Groq's Llama 3.1-8b-instant model for AI-powered responses:
- Context-aware about Xandeum project
- Technical support for node setup
- Governance and DAO assistance
- Real-time information updates

## 🔌 Port Testing

The bot includes a port checker utility for testing node connectivity:

### pNode Ports
- UDP 5000 - Network communication
- TCP 3000 - Xandminer Web GUI
- TCP 4000 - Xandminerd service

### vNode Ports
- TCP 8000 - Validator RPC
- TCP 8001 - Validator P2P
- TCP 8002 - Validator metrics

## 📚 Resources

### Official Links
- **Website**: https://xandeum.network
- **Documentation**: https://docs.xandeum.network
- **Greenpaper**: https://greenpaper.xandeum.network
- **Innovation Eras**: https://www.xandeum.network/innovation-eras

### Node Resources
- **pNode Setup**: https://pnodes.xandeum.network/
- **vNode DevNet**: https://devnet.xandeum.network/
- **DAO Platform**: https://dao.xandeum.network/dao/xand

### Community
- **Discord**: https://discord.gg/xandeum
- **Twitter**: https://twitter.com/xandeum
- **GitHub**: https://github.com/xandeum

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support and questions:
- Join the Xandeum Discord: https://discord.gg/xandeum
- Check the documentation: https://docs.xandeum.network
- Review the project information in the bot

---

**Built with ❤️ for the Xandeum community** 