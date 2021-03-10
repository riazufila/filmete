#/usr/bin/env python

import re
import requests
from discord.ext import commands


class Search(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="search", help="Searches for videos from YouTube.")
    async def search(self, ctx, text):
        payload = {"search_query": text}
        response = requests.get("http://www.youtube.com/results",
                                params=payload)
        search_results = re.findall(r'/watch\?v=(.{11})', response.text)

        await ctx.send(search_results)


def setup(bot):
    bot.add_cog(Search(bot))
