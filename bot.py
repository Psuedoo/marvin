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

@bot.command(name="up")
async def is_up(ctx):
    await ctx.send('I am alive!')

bot.run(token)