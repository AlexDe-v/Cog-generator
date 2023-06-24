from discord.ext import commands
import discord

class Pong(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    # Event command from template
    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        member.send('Welcome!')
    
def setup(bot):
    bot.add_cog(Pong(bot))