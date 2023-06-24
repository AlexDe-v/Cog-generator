from discord.ext import commands
import discord

class Pong(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    # Slash command from template
    @commands.slash_command(name='ping')
    async def ping(self, ctx):
        await ctx.respond('Pong!')
    
def setup(bot):
    bot.add_cog(Pong(bot))