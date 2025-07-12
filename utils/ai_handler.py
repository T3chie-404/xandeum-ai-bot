"""
AI Handler Module
Manages AI-powered responses using Groq API
"""

import os
import asyncio
import aiohttp
from typing import Dict, Any, Optional
from config.project_info import PROJECT_INFO

class AIHandler:
    def __init__(self):
        self.api_key = os.getenv('GROQ_API_KEY')
        self.base_url = "https://api.groq.com/openai/v1/chat/completions"
        self.model = "llama-3.1-8b-instant"
        
        # Prepare newlines for join expressions to avoid f-string backslash errors
        features = "\n".join([f"- {feature}" for feature in PROJECT_INFO.get('features', [])])
        tech_specs = "\n".join([f"- {key}: {value}" for key, value in PROJECT_INFO.get('technical_specs', {}).items()])
        token_uses = "\n".join([f"- {use_case}" for use_case in PROJECT_INFO.get('token', {}).get('use_cases', [])])
        network_info = "\n".join([f"- {network}: {status}" for network, status in PROJECT_INFO.get('network', {}).items()])
        dao_proposals = "\n".join([f"- {proposal_type}" for proposal_type in PROJECT_INFO.get('dao_specs', {}).get('proposal_types', [])])
        dao_features = "\n".join([f"- {feature}" for feature in PROJECT_INFO.get('dao_specs', {}).get('features', [])])
        innovation_eras = "\n".join([f"- {era}: {description}" for era, description in PROJECT_INFO.get('innovation_eras', {}).items()])
        faq = "\n".join([f"Q: {question}\nA: {answer}\n" for question, answer in PROJECT_INFO.get('faq', {}).items()])
        
        self.context = f"""
You are an AI assistant for the Xandeum blockchain project. You have access to comprehensive information about:

**Project Overview:**
- Xandeum is a decentralized blockchain platform with innovative consensus mechanisms
- Website: {PROJECT_INFO.get('website', 'N/A')}
- Documentation: {PROJECT_INFO.get('documentation', 'N/A')}
- Greenpaper: {PROJECT_INFO.get('greenpaper', 'N/A')}

**Key Features:**
{features}

**Technical Specifications:**
{tech_specs}

**Token Information (XAND on Solana):**
- Name: XAND
- Symbol: XAND
- Chain: Solana
- Mint Address: XANDuUoVoUqniKkpcKhrxmvYJybpJvUxJLr21Gaj3Hx
- Solscan: https://solscan.io/token/XANDuUoVoUqniKkpcKhrxmvYJybpJvUxJLr21Gaj3Hx
{token_uses}

**Network Information:**
{network_info}

**pNode Network:**
- pNodes are storage provider nodes that store encrypted data
- Setup guide: {PROJECT_INFO.get('pnodes', {}).get('setup_guide', 'N/A')}
- Hardware requirements: {PROJECT_INFO.get('pnode_specs', {}).get('hardware_requirements', {})}
- Required ports: UDP 5000, TCP 3000, TCP 4000

**vNode Network:**
- vNodes are validator nodes that participate in consensus
- DevNet: {PROJECT_INFO.get('vnodes', {}).get('devnet_home', 'N/A')}
- Hardware requirements: {PROJECT_INFO.get('vnode_specs', {}).get('hardware_requirements', {})}
- Required ports: TCP 8000, TCP 8001, TCP 8002

**DAO Governance:**
- DAO Platform: {PROJECT_INFO.get('dao', {}).get('dao_platform', 'N/A')}
- Governance type: {PROJECT_INFO.get('dao_specs', {}).get('governance_type', 'N/A')}
- Voting power: {PROJECT_INFO.get('dao_specs', {}).get('voting_power', 'N/A')}
- Platform: {PROJECT_INFO.get('dao_specs', {}).get('platform', 'N/A')}
- Proposal types:
{dao_proposals}
- Features:
{dao_features}

**Innovation Eras:**
{innovation_eras}

**Common Questions and Answers:**
{faq}

**Important Guidelines:**
1. Always provide accurate, up-to-date information about Xandeum
2. Be helpful and informative in your responses
3. If you don't know something specific, direct users to official resources
4. Use a friendly, professional tone
5. Include relevant links when appropriate
6. For technical questions, provide detailed but accessible explanations
7. For DAO questions, emphasize the importance of governance participation
8. For node setup questions, provide step-by-step guidance
9. Always mention the official documentation and resources

**Keywords to recognize:**
- Xandeum, XAN, blockchain, decentralized, consensus
- pNode, storage, mining, xandminer, xandminerd
- vNode, validator, devnet, consensus, validation
- DAO, governance, voting, proposals, Realms, Solana
- innovation eras, roadmap, development phases
- technical specs, hardware requirements, ports
- setup guides, troubleshooting, monitoring
        """
    
    async def get_ai_response(self, user_message: str) -> str:
        """Get AI response using Groq API"""
        if not self.api_key:
            return "❌ AI service not configured. Please set GROQ_API_KEY environment variable."
        
        try:
            async with aiohttp.ClientSession() as session:
                headers = {
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                }
                
                data = {
                    "model": self.model,
                    "messages": [
                        {"role": "system", "content": self.context},
                        {"role": "user", "content": user_message}
                    ],
                    "temperature": 0.7,
                    "max_tokens": 1000
                }
                
                async with session.post(self.base_url, headers=headers, json=data) as response:
                    if response.status == 200:
                        result = await response.json()
                        return result['choices'][0]['message']['content']
                    else:
                        error_text = await response.text()
                        return f"❌ AI service error: {response.status} - {error_text}"
                        
        except Exception as e:
            return f"❌ Error connecting to AI service: {str(e)}"
    
    def format_project_info(self, info_type: str) -> str:
        """Format project information for specific types"""
        if info_type == "overview":
            features = "\n".join([f"• {feature}" for feature in PROJECT_INFO.get('features', [])])
            return f"""
**Xandeum Project Overview**

🚀 **What is Xandeum?**
Xandeum is a decentralized blockchain platform that focuses on innovation, cross-chain interoperability, and sustainable blockchain technology.

🔗 **Official Resources:**
• Website: {PROJECT_INFO.get('website', 'N/A')}
• Documentation: {PROJECT_INFO.get('documentation', 'N/A')}
• Greenpaper: {PROJECT_INFO.get('greenpaper', 'N/A')}
• Innovation Eras: {PROJECT_INFO.get('innovation_eras', 'N/A')}

🌟 **Key Features:**
{features}

💎 **Native Token: XAN**
• Used for governance, staking, and network operations
• Powers the entire ecosystem

🏛️ **Governance:**
• DAO platform for decentralized decision-making
• Token-based voting system
• Community-driven development

🌐 **Networks:**
• pNode network for storage and mining
• vNode network for validation and consensus
• DevNet for testing and development
            """.strip()
        
        elif info_type == "technical":
            specs = PROJECT_INFO.get('technical_specs', {})
            return f"""
**Technical Specifications**

🔧 **Blockchain Type:** {specs.get('blockchain_type', 'N/A')}
⚡ **Consensus Algorithm:** {specs.get('consensus_algorithm', 'N/A')}
⏱️ **Block Time:** {specs.get('block_time', 'N/A')}
🚀 **Transaction Speed:** {specs.get('transaction_speed', 'N/A')}
💻 **Programming Language:** {specs.get('programming_language', 'N/A')}
📜 **Smart Contracts:** {specs.get('smart_contracts', 'N/A')}
🔗 **Cross-Chain:** {specs.get('cross_chain', 'N/A')}
🖥️ **pNode Network:** {specs.get('pnode_network', 'N/A')}
⚙️ **vNode Network:** {specs.get('vnode_network', 'N/A')}
🏛️ **DAO Governance:** {specs.get('dao_governance', 'N/A')}
            """.strip()
        
        elif info_type == "token":
            token_info = PROJECT_INFO.get('token', {})
            uses = "\n".join([f"• {use_case}" for use_case in token_info.get('use_cases', [])])
            return f"""
**XAND Token Information (Solana)**

💎 **Token Details:**
• Name: {token_info.get('name', 'N/A')}
• Symbol: {token_info.get('symbol', 'N/A')}
• Chain: {token_info.get('chain', 'Solana')}
• Mint Address: {token_info.get('mint_address', 'N/A')}
• [View on Solscan]({token_info.get('solscan', 'N/A')})
• Total Supply: {token_info.get('total_supply', 'N/A')}
• Decimals: {token_info.get('decimals', 'N/A')}

🎯 **Use Cases:**
{uses}
            """.strip()
        
        elif info_type == "eras":
            eras = PROJECT_INFO.get('innovation_eras', {})
            era_lines = "\n".join([f"• **{era.replace('_', ' ').title()}:** {description}" for era, description in eras.items()])
            return f"""
**Innovation Eras Roadmap**

📅 **Development Phases:**
{era_lines}

🔗 **Learn More:** {PROJECT_INFO.get('innovation_eras', 'N/A')}
            """.strip()
        
        elif info_type == "docs":
            return f"""
**Documentation Resources**

📚 **Official Documentation:**
• Website: {PROJECT_INFO.get('website', 'N/A')}
• Documentation: {PROJECT_INFO.get('documentation', 'N/A')}
• Greenpaper: {PROJECT_INFO.get('greenpaper', 'N/A')}
• Innovation Eras: {PROJECT_INFO.get('innovation_eras', 'N/A')}

🔧 **Technical Resources:**
• pNode Setup: {PROJECT_INFO.get('pnodes', {}).get('setup_guide', 'N/A')}
• vNode DevNet: {PROJECT_INFO.get('vnodes', {}).get('devnet_home', 'N/A')}
• DAO Platform: {PROJECT_INFO.get('dao', {}).get('dao_platform', 'N/A')}

🌐 **Community:**
• Discord: {PROJECT_INFO.get('discord', 'N/A')}
• Twitter: {PROJECT_INFO.get('twitter', 'N/A')}
• GitHub: {PROJECT_INFO.get('github', 'N/A')}
            """.strip()
        
        else:
            return "❌ Unknown information type. Use: overview, technical, token, eras, or docs" 