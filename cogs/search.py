#/usr/bin/env python

import re
import requests
from discord.ext import commands


class Search(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="search", help="Searches for videos from YouTube.")
    async def search(self, ctx, text: str):
        payload = {"search_query": text}
        response = requests.get("https://www.youtube.com/results",
                                params=payload)
        search_results = re.findall(r'/watch\?v=(.{11})', response.text)

        if search_results:
            await ctx.send(f"Yo, <@{ctx.author.id}>! We've got a hit!")
            await ctx.send(
                f"https://www.youtube.com/watch?v={search_results[0]}")
        else:
            await ctx.send(
                f"Sorry, <@{ctx.author.id}>. No results were found. Another keyword maybe?"
            )


def setup(bot):
    bot.add_cog(Search(bot))
