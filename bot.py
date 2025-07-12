"""
Xandeum AI Bot - Main Bot File
Discord bot for Xandeum project information and AI assistance using Groq
"""

import discord
from discord.ext import commands
import asyncio
import os
import logging
from dotenv import load_dotenv
from utils.ai_handler import AIHandler
from commands.bot_commands import BotCommands

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Bot configuration
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(
    command_prefix=os.getenv('BOT_PREFIX', '!'),
    intents=intents,
    help_command=None
)

# Initialize handlers
ai_handler = AIHandler()
bot_commands = None

@bot.event
async def on_ready():
    """Called when the bot is ready"""
    global bot_commands
    bot_commands = BotCommands(bot)
    
    logger.info(f'{bot.user} has connected to Discord!')
    logger.info(f'Bot is in {len(bot.guilds)} guild(s)')
    
    # Set bot status
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="Xandeum Network"
        )
    )

@bot.event
async def on_message(message):
    """Handle incoming messages"""
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return
    
    # Process commands first
    await bot.process_commands(message)
    
    # Check if we should respond with AI
    if ai_handler.should_respond_to_message(message.content):
        try:
            # Get AI response
            response = await ai_handler.get_ai_response(message.content)
            
            # Send response
            await message.channel.send(response)
            
        except Exception as e:
            logger.error(f"Error processing AI response: {e}")
            await message.channel.send("Sorry, I encountered an error processing your request.")

@bot.command(name='price')
async def price_command(ctx):
    """Get current XAN price"""
    response = await bot_commands.handle_price_command(ctx)
    await ctx.send(response)

@bot.command(name='stake')
async def stake_command(ctx):
    """Get staking information"""
    response = await bot_commands.handle_stake_command(ctx)
    await ctx.send(response)

@bot.command(name='validators')
async def validators_command(ctx):
    """Get validators information"""
    response = await bot_commands.handle_validators_command(ctx)
    await ctx.send(response)

@bot.command(name='governance')
async def governance_command(ctx):
    """Get governance information"""
    response = await bot_commands.handle_governance_command(ctx)
    await ctx.send(response)

@bot.command(name='network')
async def network_command(ctx):
    """Get network status"""
    response = await bot_commands.handle_network_command(ctx)
    await ctx.send(response)

@bot.command(name='help')
async def help_command(ctx):
    """Show help information"""
    response = await bot_commands.handle_help_command(ctx)
    await ctx.send(response)

@bot.command(name='overview')
async def overview_command(ctx):
    """Show project overview"""
    response = await bot_commands.handle_overview_command(ctx)
    await ctx.send(response)

@bot.command(name='technical')
async def technical_command(ctx):
    """Show technical specifications"""
    response = await bot_commands.handle_technical_command(ctx)
    await ctx.send(response)

@bot.command(name='token')
async def token_command(ctx):
    """Show token information"""
    response = await bot_commands.handle_token_command(ctx)
    await ctx.send(response)

@bot.command(name='eras')
async def eras_command(ctx):
    """Show innovation eras roadmap"""
    response = await bot_commands.handle_eras_command(ctx)
    await ctx.send(response)

@bot.command(name='docs')
async def docs_command(ctx):
    """Show documentation links"""
    response = await bot_commands.handle_docs_command(ctx)
    await ctx.send(response)

@bot.command(name='pnode')
async def pnode_command(ctx):
    """Show pNode information and setup guides"""
    response = await bot_commands.handle_pnode_command(ctx)
    await ctx.send(response)

@bot.command(name='pnode-setup')
async def pnode_setup_command(ctx):
    """Show pNode setup requirements and guide"""
    response = await bot_commands.handle_pnode_setup_command(ctx)
    await ctx.send(response)

@bot.command(name='pnode-update')
async def pnode_update_command(ctx):
    """Show pNode update instructions"""
    response = await bot_commands.handle_pnode_update_command(ctx)
    await ctx.send(response)

@bot.command(name='pnode-ports')
async def pnode_ports_command(ctx, ip_address: str = ""):
    """Test pNode port connectivity"""
    response = await bot_commands.handle_pnode_ports_command(ctx, ip_address)
    await ctx.send(response)

@bot.command(name='vnode')
async def vnode_command(ctx):
    """Show vNode information and setup guides"""
    response = await bot_commands.handle_vnode_command(ctx)
    await ctx.send(response)

@bot.command(name='vnode-setup')
async def vnode_setup_command(ctx):
    """Show vNode setup requirements and guide"""
    response = await bot_commands.handle_vnode_setup_command(ctx)
    await ctx.send(response)

@bot.command(name='vnode-update')
async def vnode_update_command(ctx):
    """Show vNode update instructions"""
    response = await bot_commands.handle_vnode_update_command(ctx)
    await ctx.send(response)

@bot.command(name='vnode-ports')
async def vnode_ports_command(ctx, ip_address: str = ""):
    """Test vNode port connectivity"""
    response = await bot_commands.handle_vnode_ports_command(ctx, ip_address)
    await ctx.send(response)

@bot.command(name='devnet')
async def devnet_command(ctx):
    """Show DevNet information and resources"""
    response = await bot_commands.handle_devnet_command(ctx)
    await ctx.send(response)

@bot.command(name='ai')
async def ai_command(ctx, *, question: str = ""):
    """Ask the AI a question"""
    if not question:
        await ctx.send("Please provide a question. Example: `!ai What is Xandeum?`")
        return
    
    response = await bot_commands.handle_ai_command(ctx, f"!ai {question}")
    await ctx.send(response)

@bot.event
async def on_command_error(ctx, error):
    """Handle command errors"""
    if isinstance(error, commands.CommandNotFound):
        return  # Ignore unknown commands
    
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"Missing required argument: {error.param}")
        return
    
    logger.error(f"Command error: {error}")
    await ctx.send("An error occurred while processing your command.")

def main():
    """Main function to run the bot"""
    # Get bot token
    token = os.getenv('DISCORD_TOKEN')
    
    if not token:
        logger.error("No Discord token found! Please set DISCORD_TOKEN in your .env file")
        return
    
    # Run the bot
    try:
        bot.run(token)
    except discord.LoginFailure:
        logger.error("Failed to login to Discord. Please check your token.")
    except Exception as e:
        logger.error(f"Error running bot: {e}")

if __name__ == "__main__":
    main() 