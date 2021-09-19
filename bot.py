import discord
from discord.ext.commands import Bot

from app import settings

intents = discord.Intents.default()

bot = Bot(command_prefix=settings.BOT_PREFIX, intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready to go.")


@bot.command(
    name="ping",
    help="Uses come crazy logic to determine if pong is actually the correct value or not.",
    brief="Prints pong back to the channel.",
)
async def ping_command(context, *args):
    await context.channel.send(" ".join(args))


@bot.event
async def on_message(message):
    content = message.content
    if "carlos" in content and not message.author.bot:
        await message.channel.send("carlos es joto :)")
    await bot.process_commands(message)


bot.run(settings.TOKEN)
