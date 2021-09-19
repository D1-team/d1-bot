import os
import platform
import random
from app import settings
import discord
from discord.ext import tasks
from discord.ext.commands import Bot
from discord_slash import SlashCommand, SlashContext

from cogs.template import Template

intents = discord.Intents.default()

bot = Bot(command_prefix=settings.BOT_PREFIX, intents=intents)
bot.add_cog(Template(bot))
slash = SlashCommand(bot, sync_commands=True)


# The code in this even is executed when the bot is ready
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    print(f"Discord.py API version: {discord.__version__}")
    print(f"Python version: {platform.python_version()}")
    print(f"Running on: {platform.system()} {platform.release()} ({os.name})")
    print("-------------------")
    status_task.start()


# Setup the game status task of the bot
@tasks.loop(minutes=1.0)
async def status_task():
    statuses = [
        "with you!",
        "with Krypton!",
        f"{settings.BOT_PREFIX}help",
        "with humans!",
    ]
    await bot.change_presence(activity=discord.Game(random.choice(statuses)))


# Removes the default help command of discord.py to be able to create our custom help command.
bot.remove_command("help")

if __name__ == "__main__":
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                bot.load_extension(f"cogs.{extension}")
                print(f"Loaded extension '{extension}'")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                print(f"Failed to load extension {extension}\n{exception}")


# The code in this event is executed every time someone sends a message, with or without the prefix
@bot.event
async def on_message(message):
    # Ignores if a command is being executed by a bot or by the bot itself
    if message.author == bot.user or message.author.bot:
        return
    await bot.process_commands(message)


# The code in this event is executed every time a command has been *successfully* executed
@bot.event
async def on_slash_command(ctx: SlashContext):
    fullCommandName = ctx.name
    split = fullCommandName.split(" ")
    executedCommand = str(split[0])
    print(
        f"Executed {executedCommand} command in {ctx.guild.name} (ID: {ctx.guild.id}) by {ctx.author} (ID: {ctx.author.id})"
    )


# The code in this event is executed every time a valid commands catches an error
@bot.event
async def on_command_error(context, error):
    raise error


# Run the bot with the token
bot.run(settings.TOKEN)
