from discord.ext import commands
from discord_slash import cog_ext, SlashContext


# Here we name the cog and create a new class for the cog.
class Template(commands.Cog, name="template"):
    def __init__(self, bot):
        self.bot = bot

    # Here you can just add your own commands, you'll always need to provide "self" as first parameter.
    @cog_ext.cog_slash(
        name="testcommand", description="This is a testing command that does nothing."
    )
    async def testcommand(self, context: SlashContext):
        """
        This is a testing command that does nothing.
        """
        return 1


# And then we finally add the cog to the bot so that it can load, unload, reload and use it's content.
def setup(bot):
    bot.add_cog(Template(bot))
