
    # Print room lists with Watch2Gether API
    def roomList(self, ctx, room_url):
        print("hELLO")    


    # Print list command
    @commands.command(name="list", help="List rooms in Watch2Gether.")
    async def list(room_url):

        result = self.roomList(room_url)

        await ctx.send(embed=result)

 for user in bot.user.friends:
        print (user.name)