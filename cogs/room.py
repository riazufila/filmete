#!/usr/bin/env python

import requests
import json
import asyncio
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv


class Room(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.W2G_API_KEY = self.getSecrets()

    def getSecrets(self):
        # Get env data
        load_dotenv()
        W2G_API_KEY = os.getenv("W2G_API_KEY")

        return W2G_API_KEY

    # Room creation with Watch2Gether API
    def roomCreation(self, video_url):
        # The url to POST
        api_url = "https://w2g.tv/rooms/create.json"

        # POST's body
        payload = {
            "w2g_api_key": self.W2G_API_KEY,
            "share": video_url,
            "bg_color": "#4A473F",
            "bg_opacity": "90"
        }

        # POST's header
        header = {"content-type": "application/json", "charset": "utf-8"}

        # POST request
        response = requests.post(api_url,
                                 data=json.dumps(payload),
                                 headers=header)
        streamkey = response.json().get("streamkey")
        room_url = f"https://w2g.tv/rooms/{streamkey}"

        return room_url

    # Create room command
    @commands.command(name="create", help="Creates room in Watch2Gether.")
    async def create(self, ctx, url):

        result = self.roomCreation(url)

        await ctx.send(result)

    # Reminder command
    @commands.command(name="remind", help="Set a reminder")
    async def remind(self, ctx, period, url):

        local_time = 0

        if int(period[:-1]) < 1:
            await ctx.send("What are you doing? Set up a proper period!")
        else:
            if period.lower().endswith("s"):
                local_time = int(period[:-1])

                if int(period[:-1]) > 1:
                    period = period[:-1] + " seconds"
                else:
                    period = period[:-1] + " second"
            elif period.lower().endswith("m"):
                local_time = int(period[:-1]) * 60

                if int(period[:-1]) > 1:
                    period = period[:-1] + " minutes"
                else:
                    period = period[:-1] + " minute"
            elif period.lower().endswith("h"):
                local_time = int(period[:-1]) * 60 * 60

                if int(period[:-1]) > 1:
                    period = period[:-1] + " hours"
                else:
                    period = period[:-1] + " hour"
            else:
                await ctx.send(
                    "Please specify whether to use seconds, minutes, or hours such as '>remind 1h'."
                )

        if local_time:
            await ctx.send(
                f"Sure, <@{ctx.author.id}>. I will remind you soon. *smirks*")
            await asyncio.sleep(local_time)
            await ctx.send(
                f"Yo, <@{ctx.author.id}>! It has already been {period}!")

            if not "http" in url:
                url = '"' + url + '"'
                embed = discord.Embed(title="You forgetting something?",
                                      description=url,
                                      color=0x000000)
                await ctx.send(embed=embed)
            else:
                result = self.roomCreation(url)
                await ctx.send(result)
        else:
            await ctx.send("Are you drunk?")


def setup(bot):
    bot.add_cog(Room(bot))
