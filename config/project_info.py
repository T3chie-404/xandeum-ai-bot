"""
Project Information Configuration
Contains all project-specific information that the AI bot can reference
"""

PROJECT_INFO = {
    "name": "Xandeum",
    "description": "A decentralized blockchain platform with innovative consensus mechanisms and cross-chain interoperability",
    "website": "https://xandeum.network",
    "documentation": "https://docs.xandeum.network",
    "greenpaper": "https://greenpaper.xandeum.network",
    "innovation_eras": "https://www.xandeum.network/innovation-eras",
    "github": "https://github.com/xandeum",
    "discord": "https://discord.gg/xandeum",
    "twitter": "https://twitter.com/xandeum",
    "linktree": "https://linktr.ee/xandeum",
    
    # pNode Resources
    "pnodes": {
        "setup_guide": "https://pnodes.xandeum.network/",
        "update_guide": "https://pnodes.xandeum.network/pnode-update-version",
        "pnode_status": "https://pnodes.xandeum.network/#nyhpd"
    },
    
    # vNode Resources
    "vnodes": {
        "devnet_home": "https://devnet.xandeum.network/",
        "validator_home": "https://devnet.xandeum.network/",
        "faucet_repayment": "https://devnet.xandeum.network/faucet-repayment",
        "rpc_upgrade": "https://devnet.xandeum.network/vnode-xandeum-rpc-upgrade-guide"
    },
    
    # DAO Resources
    "dao": {
        "dao_platform": "https://dao.xandeum.network/dao/xand",
        "governance": "Decentralized governance platform",
        "voting": "Token-based voting system",
        "proposals": "Community proposal system"
    },
    
    # Key Features
    "features": [
        "Decentralized network with innovative consensus",
        "Cross-chain interoperability",
        "Smart contract platform",
        "Governance system",
        "Innovation eras roadmap",
        "Green and sustainable blockchain",
        "pNode network for storage and mining",
        "vNode network for validation and consensus",
        "DAO governance platform"
    ],
    
    # Technical Specifications
    "technical_specs": {
        "blockchain_type": "Decentralized",
        "consensus_algorithm": "Innovative consensus mechanism",
        "block_time": "Optimized for performance",
        "transaction_speed": "High throughput",
        "programming_language": "Multi-language support",
        "smart_contracts": "Yes",
        "cross_chain": "Yes",
        "pnode_network": "Yes",
        "vnode_network": "Yes",
        "dao_governance": "Yes"
    },
    
    # Token Information
    "token": {
        "name": "XAND",
        "symbol": "XAND",
        "chain": "Solana",
        "mint_address": "XANDuUoVoUqniKkpcKhrxmvYJybpJvUxJLr21Gaj3Hx",
        "solscan": "https://solscan.io/token/XANDuUoVoUqniKkpcKhrxmvYJybpJvUxJLr21Gaj3Hx",
        "total_supply": "To be announced",
        "decimals": "To be determined",
        "use_cases": [
            "Network security",
            "Governance voting",
            "Transaction fees",
            "Cross-chain operations",
            "Staking rewards",
            "pNode rewards",
            "vNode rewards",
            "DAO governance"
        ]
    },
    
    # Network Information
    "network": {
        "mainnet": "In development",
        "testnet": "In development",
        "devnet": "Active - https://devnet.xandeum.network/",
        "explorer": "Coming soon"
    },
    
    # pNode Information
    "pnode_specs": {
        "hardware_requirements": {
            "cpu": "4+ cores",
            "ram": "4+ GB",
            "storage": "80+ GB SSD (60+ GB free for Xandeum)",
            "network": "1 Gbps",
            "os": "Ubuntu 24.04 LTS or later"
        },
        "ports": {
            "udp_5000": "Required for pNode communication",
            "tcp_3000": "Xandminer Web GUI",
            "tcp_4000": "Xandminerd service"
        },
        "services": {
            "xandminer": "Web GUI for pNode management",
            "xandminerd": "Background service for mining operations"
        }
    },
    
    # vNode Information
    "vnode_specs": {
        "hardware_requirements": {
            "cpu": "8+ cores (recommended)",
            "ram": "16+ GB (recommended)",
            "storage": "500+ GB SSD",
            "network": "1 Gbps",
            "os": "Ubuntu 24.04 LTS or later"
        },
        "ports": {
            "tcp_8000": "Validator RPC port",
            "tcp_8001": "Validator P2P port",
            "tcp_8002": "Validator metrics port"
        },
        "services": {
            "validator": "Main validator service",
            "xandeum_rpc": "Xandeum RPC functions",
            "system_service": "System service management",
            "logrotate": "Log rotation service"
        },
        "setup_steps": [
            "Old server housekeeping",
            "Access your server",
            "Ports setup",
            "Setup your disks",
            "Validator installation",
            "Setup system service",
            "Setup logrotate",
            "Starting your validator",
            "Monitoring your validator",
            "Onboarding"
        ]
    },
    
    # DAO Information
    "dao_specs": {
        "platform": "Realms (Solana-based)",
        "governance_type": "Token-based voting",
        "voting_power": "Based on XAN token holdings",
        "proposal_types": [
            "Network upgrades",
            "Parameter changes",
            "Funding proposals",
            "Community initiatives"
        ],
        "features": [
            "Proposal creation",
            "Voting system",
            "Result execution",
            "Community discussion"
        ]
    },
    
    # Innovation Eras
    "innovation_eras": {
        "era_1": "Foundation and Core Development",
        "era_2": "Network Launch and Expansion",
        "era_3": "Cross-chain Integration",
        "era_4": "Ecosystem Growth",
        "era_5": "Global Adoption"
    },
    
    # Common Questions and Answers
    "faq": {
        "What is Xandeum?": "Xandeum is a decentralized blockchain platform that focuses on innovation, cross-chain interoperability, and sustainable blockchain technology. It features innovative consensus mechanisms and is designed for the future of decentralized applications.",
        "What makes Xandeum unique?": "Xandeum stands out with its innovative consensus mechanisms, cross-chain interoperability features, and commitment to sustainable blockchain technology. The project follows a structured innovation eras roadmap.",
        "What are Innovation Eras?": "Innovation Eras represent Xandeum's structured development phases, from foundation and core development to global adoption. Each era focuses on specific milestones and technological advancements.",
        "Is Xandeum environmentally friendly?": "Yes, Xandeum is designed with sustainability in mind, featuring green blockchain technology and energy-efficient consensus mechanisms.",
        "When will the mainnet launch?": "The mainnet launch timeline follows the Innovation Eras roadmap. Check the official documentation for the most current timeline.",
        "How can I get involved?": "You can get involved by joining the Discord community, following the project on social media, and staying updated through the official documentation and greenpaper.",
        "What is the XAND token?": "XAND is the native token of the Xandeum network, deployed on the Solana blockchain. Mint address: XANDuUoVoUqniKkpcKhrxmvYJybpJvUxJLr21Gaj3Hx. View on Solscan: https://solscan.io/token/XANDuUoVoUqniKkpcKhrxmvYJybpJvUxJLr21Gaj3Hx",
        "Where can I learn more?": "Visit the official website at xandeum.network, read the documentation at docs.xandeum.network, and check out the greenpaper for technical details.",
        "What is a pNode?": "pNodes are storage provider nodes in the Xandeum network that store encrypted data and participate in the network's consensus mechanism. They earn rewards for providing storage and maintaining network integrity.",
        "How do I set up a pNode?": "To set up a pNode, you need a VPS with at least 4 CPU cores, 4GB RAM, and 80GB SSD storage. Follow the setup guide at pnodes.xandeum.network for detailed instructions.",
        "What ports does a pNode need?": "pNodes require UDP port 5000 for network communication, TCP port 3000 for the Xandminer Web GUI, and TCP port 4000 for the Xandminerd service.",
        "How do I update my pNode?": "To update your pNode, SSH into your server and run the installer script with option 2 for upgrades. Follow the update guide at pnodes.xandeum.network/pnode-update-version for detailed steps.",
        "What is a vNode?": "vNodes are validator nodes in the Xandeum network that participate in consensus and transaction validation. They help secure the network and earn rewards for their contribution.",
        "How do I set up a vNode?": "To set up a vNode, you need a server with at least 8 CPU cores, 16GB RAM, and 500GB SSD storage. Follow the DevNet guide at devnet.xandeum.network for detailed instructions.",
        "What ports does a vNode need?": "vNodes require TCP port 8000 for RPC, TCP port 8001 for P2P communication, and TCP port 8002 for metrics.",
        "What is the DevNet?": "The Xandeum DevNet is the development network where validators can test and participate in the network. It's based on the Agave codebase v2.2.0 and provides a testing environment for the mainnet.",
        "What is the Xandeum DAO?": "The Xandeum DAO is a decentralized governance platform where XAN token holders can participate in network decisions through voting on proposals.",
        "How do I participate in DAO governance?": "To participate in DAO governance, you need XAN tokens. Visit the DAO platform at dao.xandeum.network/dao/xand to view proposals and vote.",
        "What types of proposals can I vote on?": "DAO proposals can include network upgrades, parameter changes, funding proposals, and community initiatives. All proposals are voted on by XAN token holders.",
        "How does DAO voting work?": "DAO voting is based on XAN token holdings. The more XAN tokens you hold, the more voting power you have. You can vote Yes, No, or abstain on proposals."
    }
}

# API Endpoints for real-time data
API_ENDPOINTS = {
    "network_status": "https://api.xandeum.network/status",
    "price_data": "https://api.xandeum.network/price",
    "staking_info": "https://api.xandeum.network/staking",
    "governance": "https://api.xandeum.network/governance",
    "validators": "https://api.xandeum.network/validators",
    "pnode_status": "https://api.xandeum.network/pnodes",
    "vnode_status": "https://api.xandeum.network/vnodes",
    "dao_proposals": "https://api.xandeum.network/dao/proposals"
}

# Commands that the bot can execute
BOT_COMMANDS = {
    "!price": "Get current XAN price (when available)",
    "!stake": "Get staking information (when available)",
    "!validators": "List active validators (when available)",
    "!governance": "Show current governance proposals (when available)",
    "!network": "Show network status (when available)",
    "!help": "Show all available commands",
    "!overview": "Show project overview",
    "!technical": "Show technical specifications",
    "!token": "Show token information",
    "!eras": "Show innovation eras roadmap",
    "!docs": "Show documentation links",
    "!pnode": "Show pNode information and setup guides",
    "!pnode-setup": "Show pNode setup requirements and guide",
    "!pnode-update": "Show pNode update instructions",
    "!pnode-ports": "Test pNode port connectivity (requires IP address)",
    "!vnode": "Show vNode information and setup guides",
    "!vnode-setup": "Show vNode setup requirements and guide",
    "!vnode-update": "Show vNode update instructions",
    "!vnode-ports": "Test vNode port connectivity (requires IP address)",
    "!devnet": "Show DevNet information and resources",
    "!dao": "Show DAO information and governance platform",
    "!dao-proposals": "Show current DAO proposals (when available)",
    "!dao-vote": "Show DAO voting information"
} 