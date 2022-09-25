import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD_ID')

intents = discord.Intents(messages=True, message_content=True)
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.command()
async def ping(ctx):
    for count in range(5):
        await ctx.send("Pong")

bot.run(TOKEN)