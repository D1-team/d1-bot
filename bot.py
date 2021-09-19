import discord
from discord.ext.commands import Bot

from app import settings

intents = discord.Intents.default()

bot = Bot(command_prefix=settings.BOT_PREFIX, intents=intents)


@bot.command(
    name="ping",
    help="Uses come crazy logic to determine if pong is actually the correct value or not.",
    brief="Prints pong back to the channel.",
)
async def ping_command(context, *args):
    await context.channel.send("".join(args))


@bot.event
async def on_message(message):
    print(message.content)
    await bot.process_commands(message)


bot.run(settings.TOKEN)
