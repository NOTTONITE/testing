from threading import Thread
from discord.ext import commands
import socketListener

bot = commands.Bot(command_prefix='tb:')


@bot.event
async def on_ready():
    print('ready')

