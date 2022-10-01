import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

from video_request import get_newest_video

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD_ID')
ASPEN_TRIGGER = 'hi dom'

intents = discord.Intents(messages=True, message_content=True, members=True)
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.command()
async def dunk(ctx):
    response = get_newest_video()
    for count in range(5):
        await ctx.send(response)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if ASPEN_TRIGGER in message.content.lower():
        if message.author.id == 435230519735877653:
            file_path = os.getcwd() + '/app/img/spen.jpeg'
            file_ = discord.File(file_path)
            await message.channel.send(file=file_, content="SPEN")

    await bot.process_commands(message)

bot.run(TOKEN)