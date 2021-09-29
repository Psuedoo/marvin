import os
import discord
import asyncio
from discord.ext.commands.core import guild_only
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

token = os.getenv('TOKEN')

intents = discord.Intents.default()

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print("Logged in")

    await bot.change_presence(status=discord.Status.online, activity=discord.Game('Operating on myself'))

@bot.event
async def on_member_join(member):
    guild = member.guild
    if guild.system_channel:
        await guild.system_channel.send(f'Welcome {member.mention} to {guild.name}!')

initial_extensions = [
    "cogs.basic"
]

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

bot.run(token)