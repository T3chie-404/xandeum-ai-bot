"""
Bot Commands Module
Handles all Discord bot commands and responses
"""

import discord
from discord.ext import commands
from typing import Dict, Any, Optional
import asyncio
from config.apis import ProjectAPIClient, get_mock_data
from utils.ai_handler import AIHandler
from utils.port_checker import PortChecker
from config.project_info import PROJECT_INFO, BOT_COMMANDS

class BotCommands:
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.ai_handler = AIHandler()
        self.port_checker = PortChecker()
    
    async def handle_price_command(self, ctx) -> str:
        """Handle !price command"""
        try:
            async with ProjectAPIClient() as api_client:
                price_data = await api_client.get_price_data()
            
            if "error" in price_data:
                # Use mock data if API fails
                price_data = await get_mock_data("price_data")
            
            return f"""
**XAND Price Information**
💰 Price: ${price_data.get('price_usd', 'N/A')}
📊 24h Change: {price_data.get('change_24h', 'N/A')}%
💎 Market Cap: ${price_data.get('market_cap', 'N/A'):,}
📈 24h Volume: ${price_data.get('volume_24h', 'N/A'):,}
            """.strip()
            
        except Exception as e:
            return f"Error fetching price data: {str(e)}"
    
    async def handle_stake_command(self, ctx) -> str:
        """Handle !stake command"""
        try:
            async with ProjectAPIClient() as api_client:
                staking_data = await api_client.get_staking_info()
            
            if "error" in staking_data:
                # Use mock data if API fails
                staking_data = await get_mock_data("staking_info")
            
            return f"""
**Staking Information**
🎯 Total Staked: {staking_data.get('total_staked', 'N/A')} XAND
📈 APY: {staking_data.get('staking_apy', 'N/A')}
⚡ Min Stake: {staking_data.get('min_stake', 'N/A')} XAND
🔧 Active Validators: {staking_data.get('active_validators', 'N/A')}
📊 Total Validators: {staking_data.get('total_validators', 'N/A')}
            """.strip()
            
        except Exception as e:
            return f"Error fetching staking data: {str(e)}"
    
    async def handle_validators_command(self, ctx) -> str:
        """Handle !validators command"""
        try:
            async with ProjectAPIClient() as api_client:
                validators_data = await api_client.get_validators()
            
            if "error" in validators_data:
                # Use mock data if API fails
                validators_data = await get_mock_data("validators")
            
            response = f"""
**Validators Information**
🔧 Active Validators: {validators_data.get('active', 'N/A')}
📊 Total Validators: {validators_data.get('total', 'N/A')}

**Top Validators:**
            """
            
            for i, validator in enumerate(validators_data.get('top_validators', [])[:5], 1):
                response += f"""
{i}. **{validator.get('name', 'Unknown')}**
   Stake: {validator.get('stake', 'N/A')} XAND
   Commission: {validator.get('commission', 'N/A')}
                """
            
            return response.strip()
            
        except Exception as e:
            return f"Error fetching validators data: {str(e)}"
    
    async def handle_governance_command(self, ctx) -> str:
        """Handle !governance command"""
        try:
            async with ProjectAPIClient() as api_client:
                governance_data = await api_client.get_governance_proposals()
            
            if "error" in governance_data:
                # Use mock data if API fails
                governance_data = await get_mock_data("governance")
            
            response = f"""
**Governance Proposals**
📋 Active Proposals: {governance_data.get('active_proposals', 'N/A')}

**Current Proposals:**
            """
            
            for proposal in governance_data.get('proposals', []):
                response += f"""
• **{proposal.get('title', 'Unknown')}**
  ID: {proposal.get('id', 'N/A')}
  Status: {proposal.get('status', 'N/A')}
                """
            
            return response.strip()
            
        except Exception as e:
            return f"Error fetching governance data: {str(e)}"
    
    async def handle_network_command(self, ctx) -> str:
        """Handle !network command"""
        try:
            async with ProjectAPIClient() as api_client:
                network_data = await api_client.get_network_status()
            
            if "error" in network_data:
                # Use mock data if API fails
                network_data = await get_mock_data("network_status")
            
            return f"""
**Network Status**
🟢 Status: {network_data.get('status', 'N/A')}
📦 Block Height: {network_data.get('block_height', 'N/A'):,}
🔧 Validators: {network_data.get('validators', 'N/A')}
💰 Total Staked: {network_data.get('total_staked', 'N/A')} XAND
⏱️ Uptime: {network_data.get('network_uptime', 'N/A')}
            """.strip()
            
        except Exception as e:
            return f"Error fetching network data: {str(e)}"
    
    async def handle_help_command(self, ctx) -> str:
        """Handle !help command"""
        response = """
**Xandeum AI Bot Commands**

**Information Commands:**
"""
        
        for command, description in BOT_COMMANDS.items():
            response += f"• `{command}` - {description}\n"
        
        response += """
**AI Features:**
• Mention the bot or use `!ai` to ask questions
• Ask about Xandeum project details
• Get technical information and support

**Quick Info:**
• `!overview` - Project overview
• `!technical` - Technical specifications  
• `!token` - Token information (XAND, Solana)
• `!eras` - Innovation eras roadmap
• `!docs` - Documentation links
• `!pnode` - pNode information and guides
• `!vnode` - vNode information and guides
• `!devnet` - DevNet information and resources
• `!dao` - DAO information and governance
        """
        
        return response.strip()
    
    async def handle_overview_command(self, ctx) -> str:
        """Handle !overview command"""
        return self.ai_handler.format_project_info("overview")
    
    async def handle_technical_command(self, ctx) -> str:
        """Handle !technical command"""
        return self.ai_handler.format_project_info("technical")
    
    async def handle_token_command(self, ctx) -> str:
        """Handle !token command"""
        return self.ai_handler.format_project_info("token")
    
    async def handle_eras_command(self, ctx) -> str:
        """Handle !eras command"""
        return self.ai_handler.format_project_info("eras")
    
    async def handle_docs_command(self, ctx) -> str:
        """Handle !docs command"""
        return self.ai_handler.format_project_info("docs")
    
    async def handle_pnode_command(self, ctx) -> str:
        """Handle !pnode command"""
        pnode_info = PROJECT_INFO.get('pnodes', {})
        pnode_specs = PROJECT_INFO.get('pnode_specs', {})
        
        return f"""
**pNode Information**

🔗 **Resources:**
• Setup Guide: {pnode_info.get('setup_guide', 'N/A')}
• Update Guide: {pnode_info.get('update_guide', 'N/A')}
• Status Page: {pnode_info.get('pnode_status', 'N/A')}

🖥️ **Hardware Requirements:**
• CPU: {pnode_specs.get('hardware_requirements', {}).get('cpu', 'N/A')}
• RAM: {pnode_specs.get('hardware_requirements', {}).get('ram', 'N/A')}
• Storage: {pnode_specs.get('hardware_requirements', {}).get('storage', 'N/A')}
• Network: {pnode_specs.get('hardware_requirements', {}).get('network', 'N/A')}
• OS: {pnode_specs.get('hardware_requirements', {}).get('os', 'N/A')}

🔌 **Required Ports:**
• UDP 5000 - pNode communication
• TCP 3000 - Xandminer Web GUI
• TCP 4000 - Xandminerd service

⚙️ **Services:**
• Xandminer - Web GUI for pNode management
• Xandminerd - Background service for mining operations
        """.strip()
    
    async def handle_pnode_setup_command(self, ctx) -> str:
        """Handle !pnode-setup command"""
        return self.port_checker.get_pnode_setup_guide()
    
    async def handle_pnode_update_command(self, ctx) -> str:
        """Handle !pnode-update command"""
        pnode_info = PROJECT_INFO.get('pnodes', {})
        
        return f"""
**pNode Update Guide**

📖 **Official Update Guide:** {pnode_info.get('update_guide', 'N/A')}

🔄 **Update Process:**
1. SSH into your pNode server
2. Run the installer script with option 2 for upgrades
3. Follow the official guide for detailed steps
4. Restart services if required

💡 **Tips:**
• Always backup your configuration before updating
• Check the official guide for the latest instructions
• Monitor your pNode after updates
        """.strip()
    
    async def handle_pnode_ports_command(self, ctx, ip_address: str = "") -> str:
        """Handle !pnode-ports command"""
        if not ip_address:
            return "Please provide an IP address. Example: `!pnode-ports 192.168.1.100`"
        
        # Validate IP address
        if not self.port_checker.validate_ip_address(ip_address):
            return "❌ Invalid IP address format. Please provide a valid IP address (e.g., 192.168.1.100)"
        
        try:
            # Check all pNode ports
            results = await self.port_checker.check_pnode_ports(ip_address)
            return self.port_checker.format_port_results(ip_address, results, "pNode")
            
        except Exception as e:
            return f"❌ Error checking ports: {str(e)}"
    
    async def handle_vnode_command(self, ctx) -> str:
        """Handle !vnode command"""
        vnode_info = PROJECT_INFO.get('vnodes', {})
        vnode_specs = PROJECT_INFO.get('vnode_specs', {})
        
        return f"""
**vNode Information**

🔗 **Resources:**
• DevNet Home: {vnode_info.get('devnet_home', 'N/A')}
• Validator Home: {vnode_info.get('validator_home', 'N/A')}
• Faucet Repayment: {vnode_info.get('faucet_repayment', 'N/A')}
• RPC Upgrade Guide: {vnode_info.get('rpc_upgrade', 'N/A')}

🖥️ **Hardware Requirements:**
• CPU: {vnode_specs.get('hardware_requirements', {}).get('cpu', 'N/A')}
• RAM: {vnode_specs.get('hardware_requirements', {}).get('ram', 'N/A')}
• Storage: {vnode_specs.get('hardware_requirements', {}).get('storage', 'N/A')}
• Network: {vnode_specs.get('hardware_requirements', {}).get('network', 'N/A')}
• OS: {vnode_specs.get('hardware_requirements', {}).get('os', 'N/A')}

🔌 **Required Ports:**
• TCP 8000 - Validator RPC port
• TCP 8001 - Validator P2P port
• TCP 8002 - Validator metrics port

⚙️ **Services:**
• Validator - Main validator service
• Xandeum RPC - Xandeum RPC functions
• System Service - System service management
• Logrotate - Log rotation service
        """.strip()
    
    async def handle_vnode_setup_command(self, ctx) -> str:
        """Handle !vnode-setup command"""
        return self.port_checker.get_vnode_setup_guide()
    
    async def handle_vnode_update_command(self, ctx) -> str:
        """Handle !vnode-update command"""
        vnode_info = PROJECT_INFO.get('vnodes', {})
        
        return f"""
**vNode Update Guide**

📖 **RPC Upgrade Guide:** {vnode_info.get('rpc_upgrade', 'N/A')}

🔄 **Update Process:**
1. SSH into your vNode server
2. Follow the RPC upgrade guide for detailed steps
3. Restart validator services if required
4. Monitor your validator after updates

💡 **Tips:**
• Always backup your configuration before updating
• Check the official guide for the latest instructions
• Monitor your validator after updates
• Test on DevNet before mainnet
        """.strip()
    
    async def handle_vnode_ports_command(self, ctx, ip_address: str = "") -> str:
        """Handle !vnode-ports command"""
        if not ip_address:
            return "Please provide an IP address. Example: `!vnode-ports 192.168.1.100`"
        
        # Validate IP address
        if not self.port_checker.validate_ip_address(ip_address):
            return "❌ Invalid IP address format. Please provide a valid IP address (e.g., 192.168.1.100)"
        
        try:
            # Check all vNode ports
            results = await self.port_checker.check_vnode_ports(ip_address)
            return self.port_checker.format_port_results(ip_address, results, "vNode")
            
        except Exception as e:
            return f"❌ Error checking ports: {str(e)}"
    
    async def handle_devnet_command(self, ctx) -> str:
        """Handle !devnet command"""
        return self.port_checker.get_devnet_info()
    
    async def handle_dao_command(self, ctx) -> str:
        """Handle !dao command"""
        dao_info = PROJECT_INFO.get('dao', {})
        dao_specs = PROJECT_INFO.get('dao_specs', {})
        
        return f"""
**Xandeum DAO Information**

🔗 **DAO Platform:** {dao_info.get('dao_platform', 'N/A')}

🏛️ **Governance Type:** {dao_specs.get('governance_type', 'N/A')}
🗳️ **Voting Power:** {dao_specs.get('voting_power', 'N/A')}
📋 **Platform:** {dao_specs.get('platform', 'N/A')}

📋 **Proposal Types:**
{chr(10).join([f"• {proposal_type}" for proposal_type in dao_specs.get('proposal_types', [])])}

⚙️ **Features:**
{chr(10).join([f"• {feature}" for feature in dao_specs.get('features', [])])}

💡 **How to Participate:**
• Hold XAND tokens to get voting power
• Visit the DAO platform to view proposals
• Vote on proposals that interest you
• Participate in community discussions
        """.strip()
    
    async def handle_dao_proposals_command(self, ctx) -> str:
        """Handle !dao-proposals command"""
        dao_info = PROJECT_INFO.get('dao', {})
        
        return f"""
**DAO Proposals**

📋 **DAO Platform:** {dao_info.get('dao_platform', 'N/A')}

🔍 **To view current proposals:**
1. Visit the DAO platform
2. Connect your wallet with XAND tokens
3. Browse active proposals
4. Read proposal details and discussions
5. Cast your vote

💡 **Proposal Types:**
• Network upgrades and parameter changes
• Funding proposals for development
• Community initiatives and events
• Governance structure changes

🗳️ **Voting:**
• Voting power based on XAND token holdings
• You can vote Yes, No, or abstain
• Results are executed automatically if passed
        """.strip()
    
    async def handle_dao_vote_command(self, ctx) -> str:
        """Handle !dao-vote command"""
        dao_info = PROJECT_INFO.get('dao', {})
        
        return f"""
**DAO Voting Information**

🗳️ **How Voting Works:**
• Voting power is based on your XAND token holdings
• More tokens = more voting power
• You can vote Yes, No, or abstain on proposals

📋 **Voting Process:**
1. Visit: {dao_info.get('dao_platform', 'N/A')}
2. Connect your wallet containing XAND tokens
3. Browse active proposals
4. Read proposal details and community discussion
5. Cast your vote before the deadline

💡 **Tips:**
• Read proposal details carefully before voting
• Participate in community discussions
• Consider the long-term impact of proposals
• Your vote helps shape the network's future

🔗 **DAO Platform:** {dao_info.get('dao_platform', 'N/A')}
        """.strip()
    
    async def handle_ai_command(self, ctx, message: str) -> str:
        """Handle AI-powered responses"""
        # Remove the command prefix from the message
        clean_message = message.replace('!ai', '').strip()
        
        if not clean_message:
            return "Please provide a question after !ai. For example: `!ai What is Xandeum?`"
        
        return await self.ai_handler.get_ai_response(clean_message)
    
    def get_command_handler(self, command: str):
        """Get the appropriate command handler"""
        command_handlers = {
            '!price': self.handle_price_command,
            '!stake': self.handle_stake_command,
            '!validators': self.handle_validators_command,
            '!governance': self.handle_governance_command,
            '!network': self.handle_network_command,
            '!help': self.handle_help_command,
            '!overview': self.handle_overview_command,
            '!technical': self.handle_technical_command,
            '!token': self.handle_token_command,
            '!eras': self.handle_eras_command,
            '!docs': self.handle_docs_command,
            '!pnode': self.handle_pnode_command,
            '!pnode-setup': self.handle_pnode_setup_command,
            '!pnode-update': self.handle_pnode_update_command,
            '!pnode-ports': self.handle_pnode_ports_command,
            '!vnode': self.handle_vnode_command,
            '!vnode-setup': self.handle_vnode_setup_command,
            '!vnode-update': self.handle_vnode_update_command,
            '!vnode-ports': self.handle_vnode_ports_command,
            '!devnet': self.handle_devnet_command,
            '!dao': self.handle_dao_command,
            '!dao-proposals': self.handle_dao_proposals_command,
            '!dao-vote': self.handle_dao_vote_command
        }
        
        return command_handlers.get(command) 