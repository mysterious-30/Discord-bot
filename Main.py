import discord
from discord.ext import commands, tasks
import asyncio
import logging
import pytz
from datetime import datetime, timedelta
import re

# Setup logging
logging.basicConfig(level=logging.INFO, filename='discord.log', format='%(asctime)s - %(message)s')

# Bot prefix and intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Bot setup
bot = commands.Bot(command_prefix="~", intents=intents)

# Global variables for scheduled tasks
cleanup_schedule = {}

# Welcome and farewell channels (to be customized)
WELCOME_CHANNEL_ID = 1234567890  # Example ID (Replace with actual)
FAREWELL_CHANNEL_ID = 1234567890  # Example ID (Replace with actual)

# Timezone setup
IST = pytz.timezone('Asia/Kolkata')

# Define a command to log bot activity
@bot.event
async def on_ready():
    logging.info(f'{bot.user} has connected to Discord!')
    print(f'Logged in as {bot.user}')

# Command to purge messages from the channel
@bot.command(name='purge')
async def purge(ctx, amount: int):
    try:
        if ctx.author.guild_permissions.manage_messages:
            await ctx.channel.purge(limit=amount + 1)  # +1 to delete the command message itself
            logging.info(f'{ctx.author} purged {amount} messages in {ctx.channel}')
            await ctx.send(f'{amount} messages have been deleted!', delete_after=5)
        else:
            await ctx.send("You do not have permission to purge messages.", delete_after=5)
    except Exception as e:
        logging.error(f"Error during purge: {e}")
        await ctx.send("An error occurred while purging messages.", delete_after=5)

# Command to display avatar of a user
@bot.command(name='avatar')
async def avatar(ctx, member: discord.Member = None):
    member = member or ctx.author  # If no member is provided, use the command author
    await ctx.send(member.avatar_url)

# Command to schedule message cleanup
@bot.command(name='autoclean')
async def autoclean(ctx, channel: discord.TextChannel, time: str):
    # Validate time format (HH:MM)
    if not re.match(r'^[0-9]{2}:[0-9]{2}$', time):
        await ctx.send("Invalid time format. Use HH:MM.")
        return

    # Parse time and convert to IST
    hour, minute = map(int, time.split(':'))
    now = datetime.now(IST)
    cleanup_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
    
    # If cleanup_time is in the past, schedule it for the next day
    if cleanup_time < now:
        cleanup_time += timedelta(days=1)

    # Store scheduled cleanup task
    cleanup_schedule[channel.id] = cleanup_time

    await ctx.send(f"Scheduled cleanup for {channel.mention} at {cleanup_time.strftime('%H:%M IST')}.")

# Scheduled task to perform cleanup
@tasks.loop(minutes=1)
async def cleanup_task():
    now = datetime.now(IST)
    for channel_id, cleanup_time in cleanup_schedule.items():
        if now >= cleanup_time:
            channel = bot.get_channel(channel_id)
            if channel:
                await channel.purge(limit=100)  # Purge the last 100 messages
                logging.info(f"Purged messages in {channel.name} at {now.strftime('%H:%M IST')}")
                # Reset cleanup schedule
                cleanup_schedule[channel_id] = cleanup_time + timedelta(days=1)

# Start the cleanup task when the bot is ready
@bot.event
async def on_ready():
    cleanup_task.start()

# Command to shutdown the bot (Owner only)
@bot.command(name='shutdown')
async def shutdown(ctx):
    if ctx.author.id == YOUR_DISCORD_ID:  # Replace with your Discord ID
        await ctx.send("Shutting down bot...")
        await bot.close()
    else:
        await ctx.send("You do not have permission to shut down the bot.", delete_after=5)

# Command to send a welcome message when a member joins
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(WELCOME_CHANNEL_ID)
    if channel:
        await channel.send(f"Welcome {member.mention} to the server! We are glad to have you here.")

# Command to send a farewell message when a member leaves
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(FAREWELL_CHANNEL_ID)
    if channel:
        await channel.send(f"Goodbye {member.name}, we hope to see you again soon.")

# Run the bot with your token
bot.run('YOUR_BOT_TOKEN')  # Replace with your bot token
