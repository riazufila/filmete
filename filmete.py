#!/usr/bin/env python

import os
import discord
from dotenv import load_dotenv

# Load env file
load_dotenv()

# Assign variables
TOKEN = os.getenv("DISCORD_TOKEN")
client = discord.Client()


@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")


client.run(TOKEN)
