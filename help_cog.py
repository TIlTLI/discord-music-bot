import discord
from discord.ext import commands

CHANNEL_ID = 1297722465153450075

class help_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.help_message ="""
'''
Commands:
    !help - Displays this message
    !ytplay - Plays music
    !ytstop - Pauses music
    !r - Resumes music
    !s - Skips current song
    !q - Displays current queue
    !l - Leaves voice channel
'''
""" 
        self.text_channel_text = []
    
    @commands.Cog.listener()
    async def on_ready(self, msg):
        channel = self.bot.get_channel(CHANNEL_ID)
        await channel.send(msg)

    @commands.command(name="help", aliases=["h"], help="Display help message")
    async def help(self, ctx):
        await ctx.send(self.help_message)
