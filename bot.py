import platform
import os
import discord
from discord.ext.commands import Bot
from discord.ext import tasks

from app import settings

intents = discord.Intents.default()

bot = Bot(command_prefix=settings.BOT_PREFIX, intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    print(f"Discord.py API version: {discord.__version__}")
    print(f"Python version: {platform.python_version()}")
    print(f"Running on: {platform.system()} {platform.release()} ({os.name})")
    status_task.start()


@tasks.loop(minutes=1.0)
async def status_task():
    await bot.change_presence(activity=discord.Game(""))


@bot.command(
    name="ping",
    help="Uses come crazy logic to determine if pong is actually the correct value or not.",
    brief="Prints pong back to the channel.",
)
async def ping_command(context, *args):
    await context.channel.send(" ".join(args))


@bot.event
async def on_message(context):
    """
    The code in this event is executed every time someone sends a message, with or without the prefix
    """
    message = context.content
    if "carlos" in message.lower() and not context.author.bot:
        await context.channel.send("carlos es joto :olv:")
    command_list = []
    for command in bot.commands:
        command_list.append(f"{settings.BOT_PREFIX}{command.name}")
    first_message = message.split(" ")[0]
    if first_message in command_list:
        print(f"I will execute the command: {first_message}")
        await bot.process_commands(context)


bot.run(settings.TOKEN)
