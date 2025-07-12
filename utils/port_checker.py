"""
Port Checker Utility for pNode and vNode Connectivity Testing
Tests required ports for pNode and vNode operation
"""

import asyncio
import subprocess
import re
from typing import Dict, List, Tuple
import logging

logger = logging.getLogger(__name__)

class PortChecker:
    def __init__(self):
        self.pnode_ports = {
            'udp_5000': 'UDP 5000 - pNode communication',
            'tcp_3000': 'TCP 3000 - Xandminer Web GUI',
            'tcp_4000': 'TCP 4000 - Xandminerd service'
        }
        
        self.vnode_ports = {
            'tcp_8000': 'TCP 8000 - Validator RPC port',
            'tcp_8001': 'TCP 8001 - Validator P2P port',
            'tcp_8002': 'TCP 8002 - Validator metrics port'
        }
    
    async def check_port(self, ip_address: str, port: int, protocol: str = 'tcp') -> Tuple[bool, str]:
        """Check if a specific port is open on the given IP address"""
        try:
            # Use netcat to test port connectivity
            if protocol.lower() == 'udp':
                cmd = f"timeout 10 nc -zu {ip_address} {port}"
            else:
                cmd = f"timeout 10 nc -zv {ip_address} {port}"
            
            # Run the command
            process = await asyncio.create_subprocess_shell(
                cmd,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            
            stdout, stderr = await process.communicate()
            
            if process.returncode == 0:
                return True, f"✅ {protocol.upper()} {port} is OPEN on {ip_address}"
            else:
                return False, f"❌ {protocol.upper()} {port} is CLOSED on {ip_address}"
                
        except Exception as e:
            logger.error(f"Error checking port {port} on {ip_address}: {e}")
            return False, f"❌ Error checking {protocol.upper()} {port} on {ip_address}: {str(e)}"
    
    async def check_pnode_ports(self, ip_address: str) -> Dict[str, Tuple[bool, str]]:
        """Check all required pNode ports"""
        results = {}
        
        # Check UDP 5000
        results['udp_5000'] = await self.check_port(ip_address, 5000, 'udp')
        
        # Check TCP 3000
        results['tcp_3000'] = await self.check_port(ip_address, 3000, 'tcp')
        
        # Check TCP 4000
        results['tcp_4000'] = await self.check_port(ip_address, 4000, 'tcp')
        
        return results
    
    async def check_vnode_ports(self, ip_address: str) -> Dict[str, Tuple[bool, str]]:
        """Check all required vNode ports"""
        results = {}
        
        # Check TCP 8000
        results['tcp_8000'] = await self.check_port(ip_address, 8000, 'tcp')
        
        # Check TCP 8001
        results['tcp_8001'] = await self.check_port(ip_address, 8001, 'tcp')
        
        # Check TCP 8002
        results['tcp_8002'] = await self.check_port(ip_address, 8002, 'tcp')
        
        return results
    
    def format_port_results(self, ip_address: str, results: Dict[str, Tuple[bool, str]], node_type: str = "pNode") -> str:
        """Format port check results for Discord message"""
        formatted = f"**Port Check Results for {ip_address} ({node_type})**\n\n"
        
        for port_name, (is_open, message) in results.items():
            formatted += f"{message}\n"
        
        # Summary
        open_ports = sum(1 for is_open, _ in results.values() if is_open)
        total_ports = len(results)
        
        formatted += f"\n**Summary:** {open_ports}/{total_ports} required ports are open"
        
        if open_ports == total_ports:
            formatted += f"\n🎉 **All ports are open! Your {node_type} should work properly.**"
        elif open_ports > 0:
            formatted += f"\n⚠️ **Some ports are closed. Check your firewall settings.**"
        else:
            formatted += f"\n🚫 **No required ports are open. Please check your server configuration.**"
        
        return formatted
    
    def validate_ip_address(self, ip_address: str) -> bool:
        """Basic IP address validation"""
        # Simple regex for IP validation
        ip_pattern = r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
        return bool(re.match(ip_pattern, ip_address))
    
    def get_pnode_requirements(self) -> str:
        """Get pNode hardware and software requirements"""
        return """
**pNode Requirements:**

🖥️ **Hardware:**
• CPU: 4+ cores
• RAM: 4+ GB
• Storage: 80+ GB SSD (60+ GB free for Xandeum)
• Network: 1 Gbps
• OS: Ubuntu 24.04 LTS or later

🔌 **Required Ports:**
• UDP 5000 - pNode communication
• TCP 3000 - Xandminer Web GUI
• TCP 4000 - Xandminerd service

📚 **Resources:**
• Setup Guide: https://pnodes.xandeum.network/
• Update Guide: https://pnodes.xandeum.network/pnode-update-version
        """.strip()
    
    def get_vnode_requirements(self) -> str:
        """Get vNode hardware and software requirements"""
        return """
**vNode Requirements:**

🖥️ **Hardware:**
• CPU: 8+ cores (recommended)
• RAM: 16+ GB (recommended)
• Storage: 500+ GB SSD
• Network: 1 Gbps
• OS: Ubuntu 24.04 LTS or later

🔌 **Required Ports:**
• TCP 8000 - Validator RPC port
• TCP 8001 - Validator P2P port
• TCP 8002 - Validator metrics port

📚 **Resources:**
• DevNet Home: https://devnet.xandeum.network/
• Validator Home: https://devnet.xandeum.network/
• Faucet Repayment: https://devnet.xandeum.network/faucet-repayment
• RPC Upgrade Guide: https://devnet.xandeum.network/vnode-xandeum-rpc-upgrade-guide
        """.strip()
    
    def get_pnode_setup_guide(self) -> str:
        """Get pNode setup guide information"""
        return """
**pNode Setup Guide:**

📖 **Official Setup Guide:** https://pnodes.xandeum.network/

🔄 **Update Instructions:** https://pnodes.xandeum.network/pnode-update-version

⚙️ **Services:**
• Xandminer - Web GUI for pNode management
• Xandminerd - Background service for mining operations

💡 **Tips:**
• Make sure all required ports are open
• Use Ubuntu 24.04 LTS or later
• Ensure you have sufficient storage space
• Check your firewall settings
        """.strip()
    
    def get_vnode_setup_guide(self) -> str:
        """Get vNode setup guide information"""
        return """
**vNode Setup Guide:**

📖 **DevNet Home:** https://devnet.xandeum.network/

🔄 **Setup Steps:**
1. Old server housekeeping
2. Access your server
3. Ports setup
4. Setup your disks
5. Validator installation
6. Setup system service
7. Setup logrotate
8. Starting your validator
9. Monitoring your validator
10. Onboarding

⚙️ **Services:**
• Validator - Main validator service
• Xandeum RPC - Xandeum RPC functions
• System Service - System service management
• Logrotate - Log rotation service

💡 **Tips:**
• Make sure all required ports are open
• Use Ubuntu 24.04 LTS or later
• Ensure you have sufficient storage space (500+ GB)
• Check your firewall settings
• Monitor your validator regularly
        """.strip()
    
    def get_devnet_info(self) -> str:
        """Get DevNet information"""
        return """
**Xandeum DevNet Information:**

🌐 **DevNet Home:** https://devnet.xandeum.network/

📋 **Available Resources:**
• Validator Home: https://devnet.xandeum.network/
• Faucet Repayment: https://devnet.xandeum.network/faucet-repayment
• RPC Upgrade Guide: https://devnet.xandeum.network/vnode-xandeum-rpc-upgrade-guide

🔧 **DevNet Details:**
• Based on Agave codebase v2.2.0
• Testing environment for mainnet
• Active validator network
• Faucet available for testing

💡 **Getting Started:**
• Visit the DevNet home page
• Follow the validator setup guide
• Join the community for support
        """.strip() 