  def roomDivision(self, ctx, room_url):
        print(self.guilds)
        if not ctx.guild.id in self.guilds:
            self.guilds[ctx.guild.id] = [room_url]
        else:
            self.guilds[ctx.guild.id].append(room_url)
        print(self.guilds)

    # Room creation with Watch2Gether API
    def roomCreation(self, ctx, video_url):
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

            self.roomDivision(ctx, room_url)

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

        result = self.roomCreation(ctx, url)

        await ctx.send(embed=result)
