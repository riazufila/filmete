#!/usr/bin/env python

import os
import asyncio
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


# Reminder bot command
@bot.command()
async def remind(ctx, duration, subject):

    local_time = 0

    if int(duration[:-1]) < 1:
        await ctx.send("What are you doing? Set up a proper duration!")
    else:
        if duration.lower().endswith("s"):
            local_time = int(duration[:-1])

            if int(duration[:-1]) > 1:
                duration = duration[:-1] + " seconds"
            else:
                duration = duration[:-1] + " second"
        elif duration.lower().endswith("m"):
            local_time = int(duration[:-1]) * 60

            if int(duration[:-1]) > 1:
                duration = duration[:-1] + " minutes"
            else:
                duration = duration[:-1] + " minute"
        elif duration.lower().endswith("h"):
            local_time = int(duration[:-1]) * 60 * 60

            if int(duration[:-1]) > 1:
                duration = duration[:-1] + " hours"
            else:
                duration = duration[:-1] + " hour"
        else:
            await ctx.send(
                "Please specify whether to use seconds, minutes, or hours such as '>remind 1h'."
            )

    if local_time:
        await ctx.send(
            f"Sure, <@{ctx.author.id}>. I will remind you soon. *smirks*")
        await asyncio.sleep(local_time)
        await ctx.send(
            f"Yo, <@{ctx.author.id}>! It has already been {duration}!\n`{subject}`"
        )
    else:
        await ctx.send("Are you drunk?")


# Run bot with TOKEN
bot.run(TOKEN)
