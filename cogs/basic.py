from discord.ext import commands
from cogs.utils import checks

class Basic(commands.Cog):
    """*Boring basic commands for boring basic things*"""
    def __init__(self, bot):
        self.bot = bot
        self.hidden = False

    @commands.command(name="up")
    async def is_up(self, ctx):
        await ctx.send('I am alive!')

    @commands.command(name="add")
    async def add(self, ctx, num_one, num_two):
        if num_one and num_two:
            try:
                num_one = int(num_one)
                num_two = int(num_two)
                await ctx.send(num_one+num_two)
            except TypeError as e:
                print(e)
        else:
            print("Something's wrong")

def setup(bot):
    bot.add_cog(Basic(bot))
