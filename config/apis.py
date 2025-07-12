"""
API Configuration and Utilities
Handles external API calls for real-time project data
"""

import aiohttp
import asyncio
import json
from typing import Dict, Any, Optional
import os
from dotenv import load_dotenv

load_dotenv()

class ProjectAPIClient:
    def __init__(self):
        self.base_url = os.getenv('PROJECT_API_URL', 'https://api.xandeum.com')
        self.api_key = os.getenv('PROJECT_API_KEY')
        self.session = None
    
    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()
    
    async def get_network_status(self) -> Dict[str, Any]:
        """Get current network status"""
        try:
            async with self.session.get(f"{self.base_url}/status") as response:
                if response.status == 200:
                    return await response.json()
                else:
                    return {"error": f"Status {response.status}"}
        except Exception as e:
            return {"error": str(e)}
    
    async def get_price_data(self) -> Dict[str, Any]:
        """Get current token price data"""
        try:
            async with self.session.get(f"{self.base_url}/price") as response:
                if response.status == 200:
                    return await response.json()
                else:
                    return {"error": f"Status {response.status}"}
        except Exception as e:
            return {"error": str(e)}
    
    async def get_staking_info(self) -> Dict[str, Any]:
        """Get current staking information"""
        try:
            async with self.session.get(f"{self.base_url}/staking") as response:
                if response.status == 200:
                    return await response.json()
                else:
                    return {"error": f"Status {response.status}"}
        except Exception as e:
            return {"error": str(e)}
    
    async def get_validators(self) -> Dict[str, Any]:
        """Get list of active validators"""
        try:
            async with self.session.get(f"{self.base_url}/validators") as response:
                if response.status == 200:
                    return await response.json()
                else:
                    return {"error": f"Status {response.status}"}
        except Exception as e:
            return {"error": str(e)}
    
    async def get_governance_proposals(self) -> Dict[str, Any]:
        """Get current governance proposals"""
        try:
            async with self.session.get(f"{self.base_url}/governance") as response:
                if response.status == 200:
                    return await response.json()
                else:
                    return {"error": f"Status {response.status}"}
        except Exception as e:
            return {"error": str(e)}

# Mock data for testing when APIs are not available
MOCK_DATA = {
    "network_status": {
        "status": "online",
        "block_height": 1234567,
        "validators": 150,
        "total_staked": "50000000",
        "network_uptime": "99.9%"
    },
    "price_data": {
        "price_usd": 0.25,
        "price_btc": 0.00001234,
        "market_cap": 25000000,
        "volume_24h": 1000000,
        "change_24h": 2.5
    },
    "staking_info": {
        "total_staked": "50000000",
        "staking_apy": "12.5%",
        "min_stake": "1000",
        "active_validators": 150,
        "total_validators": 200
    },
    "validators": {
        "active": 150,
        "total": 200,
        "top_validators": [
            {"name": "Validator1", "stake": "1000000", "commission": "5%"},
            {"name": "Validator2", "stake": "950000", "commission": "4%"},
            {"name": "Validator3", "stake": "900000", "commission": "6%"}
        ]
    },
    "governance": {
        "active_proposals": 3,
        "proposals": [
            {"id": 1, "title": "Increase block reward", "status": "active"},
            {"id": 2, "title": "Update staking parameters", "status": "active"},
            {"id": 3, "title": "Add new validator", "status": "active"}
        ]
    }
}

async def get_mock_data(data_type: str) -> Dict[str, Any]:
    """Get mock data for testing purposes"""
    return MOCK_DATA.get(data_type, {"error": "Unknown data type"}) 