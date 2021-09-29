from discord.ext import commands

class Basic(commands.Cog):
    """*Boring basic commands for boring basic things*"""
    def __init__(self, bot):
        self.bot = bot
        self.hidden = False

    @commands.command(name="up")
    async def is_up(self, ctx):
        await ctx.send('I am alive!')

def setup(bot):
    bot.add_cog(Basic(bot))
