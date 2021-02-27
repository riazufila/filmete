#!/usr/bin/env python

import random
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
        if not "http" in video_url:
            return "Is that even a valid url?"
        else:
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

            embed = discord.Embed(
                title="Let's watch together?",
                description=
                "This is a room created in Watch2Gether for you to watch together with you friends.",
                color=0x000000)
            embed.add_field(name="Room's URL", value=room_url)

            return embed

    # Create room command
    @commands.command(name="create", help="Creates room in Watch2Gether.")
    async def create(self, ctx, url):

        result = self.roomCreation(url)

        await ctx.send(embed=result)

    # Reminder command
    @commands.command(name="remind", help="Set a reminder.")
    async def remind(self, ctx, period, url):

        local_time = 0

        # if int(period) < 10:
        #     await ctx.send("What are you doing? Set up a proper period!")
        # elif int(period[:-1]) < 1:
        #     await ctx.send("What are you doing? Set up a proper period!")
        if (period.lower().endswith("s") or period.lower().endswith("m")
                or period.lower().endswith("h")) and len(period) > 1:
            if (period[-2:-1] >= "a"
                    and period[-2:-1] <= "z") or (period[-2:-1] >= "A"
                                                  and period[-2:-1] <= "Z"):
                await ctx.send(
                    f"I'm getting tired of these wrong commands, <@{ctx.author.id}>"
                )
            elif int(period[:-1]) > 0:
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
                else:
                    local_time = int(period[:-1]) * 60 * 60

                    if int(period[:-1]) > 1:
                        period = period[:-1] + " hours"
                    else:
                        period = period[:-1] + " hour"
            else:
                await ctx.send(
                    "You need to enter a real value for time. Guess what? 0 is not one of them."
                )
        elif len(period) > 1:
            if (period[len(period) - 1] >= "a" and period[len(period) - 1] <=
                    "z") or (period[len(period) - 1] >= "A"
                             and period[len(period) - 1] <= "Z"):
                reply = [
                    f"Hey, <@{ctx.author.id}>. Please specify whether to use seconds, minutes, or hours such as ';remind 1h'.",
                    f"<@{ctx.author.id}>, maybe you don't know this.. But you should specify if its seconds, minutes, or hours. ';remind 5m for example?'",
                    f"Check the docs, <@{ctx.author.id}>!",
                    f"Wrong command! Wrong! Wrong! Wrong! <@{ctx.author.id}>, you're wrong!",
                    f"Use 's' for seconds, 'm' for minutes, and 'h' for hours. For example, 10m. Please, get in the game, <@{ctx.author.id}>."
                ]
                await ctx.send(random.choice(reply))
        else:
            reply = [
                f"That's only one character. Don't mess with me, <@{ctx.author.id}>.",
                f"You, <@{ctx.author.id}>! You really think that one digit is enough to make a reminder?",
                f"Don't make me go out there and smack you, <@{ctx.author.id}>!"
            ]
            await ctx.send(random.choice(reply))

        if local_time:
            reply = [
                f"Sure, <@{ctx.author.id}>. I will remind you soon. *smirks*",
                f"I know you always forget things, <@{ctx.author.id}>.. I got you!",
                f"I'm getting tired of always reminding <@{ctx.author.id}>",
                f"Sigh.. Please, <@{ctx.author.id}>. I'm getting annoyed.",
                f"This must be so important for you to disturb me, <@{ctx.author.id}>!"
            ]
            await ctx.send(random.choice(reply))
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
                await ctx.send(embed=result)
        else:
            reply = [
                f"Are you drunk, <@{ctx.author.id}>?",
                f"<@{ctx.author.id}>.. You..  alright?",
                f"Ahahahaha. Funny, <@{ctx.author.id}>.",
                f"DON'T DARE ENTER THE WRONG COMMAND, <@{ctx.author.id}>!",
                f"LOL WRONG HAHA, <@{ctx.author.id}>!"
            ]
            await ctx.send(random.choice(reply))


def setup(bot):
    bot.add_cog(Room(bot))
