#!/usr/bin/env python

import os
from discord.ext import commands
from dotenv import load_dotenv

if __name__ == "__main__":
    # Get secrets
    load_dotenv()
    TOKEN = os.getenv("DISCORD_TOKEN")

    # Bot setup
    bot = commands.Bot(
        command_prefix="filmete;",
        description='Filmete creates virtual room for synced streaming.')

    bot.remove_command("help")

    # Load extensions (cog)
    extensions = ["cogs.help", "cogs.room", "cogs.search"]

    for extension in extensions:
        bot.load_extension(extension)

    # Bot on_ready event
    @bot.event
    async def on_ready():
        print(f"{bot.user} is now ready to rock and roll!")

    # Run bot
    bot.run(TOKEN)
