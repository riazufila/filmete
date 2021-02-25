#!/usr/bin/env python

import os
from discord.ext import commands
from dotenv import load_dotenv

# Load env file
load_dotenv()

# Assign variables
TOKEN = os.getenv("DISCORD_TOKEN")
bot = commands.Bot(command_prefix=">")


@bot.command(name='room')
async def createRoom(context):
    response = "Implement Watch2Gether API here."

    await context.send(response)


bot.run(TOKEN)
