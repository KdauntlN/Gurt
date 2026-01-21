import discord
from dotenv import load_dotenv
from discord.ext import commands
import logging
import os

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name} is lowkirkenuinely ready")

@bot.event
async def on_member_join(member: discord.member.Member):
    channel = discord.utils.get(member.guild.text_channels, name="greetings")
    if channel:
        await channel.send(f"Yo {member.mention}")
    else:
        channel = discord.utils.get(member.guild.text_channels, name="general")
        if channel:
            await channel.send(f"Yo {member.mention}")

bot.run(token, log_handler=handler, log_level=logging.DEBUG)