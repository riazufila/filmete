#!/usr/bin/env python

import os
import json
import requests
from discord.ext import commands
from dotenv import load_dotenv

# Load env file
load_dotenv()

# Initialize secrets
TOKEN = os.getenv("DISCORD_TOKEN")
W2G_API_KEY = os.getenv("W2G_API_KEY")

# Discord command prefix
bot = commands.Bot(command_prefix=">")


# Bot commands
@bot.command(name="create")
async def createRoom(context):
    url = "https://w2g.tv/rooms/create.json"
    payload = {
        "w2g_api_key": W2G_API_KEY,
        "share": "https://youtu.be/wQLylDQtvac",
        "bg_color": "#00ff00",
        "bg_opacity": "50"
    }
    header = {"content-type": "application/json", "charset": "utf-8"}

    response = requests.post(url, data=json.dumps(payload), headers=header)
    streamkey = response.json().get("streamkey")
    room_url = f"https://w2g.tv/rooms/{streamkey}"

    await context.send(room_url)


# Run bot with TOKEN
bot.run(TOKEN)
