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
        command_prefix=">",
        description=
        "A Discord Bot to create a virtual room to watch videos together via Watch2Gether API.",
        help_command=help_command)

    # Load extensions (cog)
    extensions = ["cogs.room"]

    for extension in extensions:
        bot.load_extension(extension)

    # Run bot with TOKEN
    bot.run(TOKEN)
