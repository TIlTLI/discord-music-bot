import discord
from discord.ext import commands
import os

from help_cog import help_cog
from music_cog import music_cog
from bot_token import bot_token


BOT_TOKEN = bot_token

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

bot.remove_command('help')

async def main():
    async with bot:
        bot.add_cog(help_cog(bot))
        bot.add_cog(music_cog(bot))
        
        await bot.run(BOT_TOKEN)

if __name__ == "__main__":
    bot.run(BOT_TOKEN)