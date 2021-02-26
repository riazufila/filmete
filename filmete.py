#!/usr/bin/env python

import os
import json  # Handle json format data
import requests  # To handle HTTP requests
from discord.ext import commands
from dotenv import load_dotenv

# Load env file
load_dotenv()

# Initialize secrets
TOKEN = os.getenv("DISCORD_TOKEN")
W2G_API_KEY = os.getenv("W2G_API_KEY")

# Discord command prefix
bot = commands.Bot(command_prefix=">")


# Create rooms
@bot.command(name="create")
async def createRoom(ctx, video_url):
    # The url to POST
    api_url = "https://w2g.tv/rooms/create.json"

    # POST's body
    payload = {
        "w2g_api_key": W2G_API_KEY,
        "share": video_url,
        "bg_color": "#4A473F",
        "bg_opacity": "90"
    }

    # POST's header
    header = {"content-type": "application/json", "charset": "utf-8"}

    # POST request
    response = requests.post(api_url, data=json.dumps(payload), headers=header)
    streamkey = response.json().get("streamkey")
    room_url = f"https://w2g.tv/rooms/{streamkey}"

    await ctx.send(room_url)


@bot.command(name="remind-at")
async def remindAt(ctx, time):
    #TODO

    await ctx.send(f"I will remind you at {time}")


# Run bot with TOKEN
bot.run(TOKEN)
