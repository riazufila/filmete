#!/usr/bin/env python

import os
from discord.ext import commands
from dotenv import load_dotenv

# Load env file
load_dotenv()

# Assign variables
TOKEN = os.getenv("DISCORD_TOKEN")
bot = commands.Bot(command_prefix=">")


@bot.command(name='create-room')
async def createRoom(context):
    response = "Get working and make sure the API is implemented!"

    await context.send(response)


bot.run(TOKEN)
