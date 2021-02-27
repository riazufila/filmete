#!/usr/bin/env python

import os
from discord.ext import commands
from dotenv import load_dotenv

if __name__ == "__main__":
    # Get secrets
    load_dotenv()
    TOKEN = os.getenv("DISCORD_TOKEN")

    # Discord command prefix
    help_command = commands.DefaultHelpCommand(no_category="Commands",
                                               indent=4)
    bot = commands.Bot(
        command_prefix=";",
        description=
        'A Discord Bot to create a virtual room for synced streaming.',
        help_command=help_command)

    # Remove default help command
    bot.remove_command("help")

    # Load extensions (cog)
    extensions = ["cogs.room", "cogs.help"]

    for extension in extensions:
        bot.load_extension(extension)

    @bot.event
    async def on_ready():
        print(f"{bot.user} is now ready to rock and roll!")

    # Run bot with TOKEN
    bot.run(TOKEN)
