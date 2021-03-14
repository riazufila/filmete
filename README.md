# Filmete

Filmete is a simple discord bot that uses Watch2Gether API to create a room for a bunch of people in a server to watch videos together.

This is different compared to the normal share screen by Discord in which this bot allows any participant in the room to pause, play, and seek position. This is inclusive of adding videos into the queue.

## Deploy

Firstly, you will need to sign up a discord account prior of creating a bot. Then, you can retrieve the token. This can be done via https://discord.com/developers.

After that, you will need to follow the guide in https://community.w2g.tv/t/watch2gether-api-documentation/133767 to make use of Watch2Gether API that this bot will use for synced streaming.

Then, clone the repository and create a new file named `.env` in the project folder that should contain the API key for Discord Bot and Watch2Gether labeled as DISCORD_TOKEN and W2G_API_KEY respectively.

For example:

```
DISCORD_TOKEN = bot_key
W2G_API_KEY = w2g_key
```

Finally, execute Filmete.

## Bot Commands

The character "filmete;" is our bot's prefix. Hence, every command is expected to start with the said prefix.

| Commands |     Parameters     | Description                       |
| :------: | :----------------: | --------------------------------- |
|  create  |      \<url\>       | Creates room in Watch2Gether.     |
|  remind  | \<period\> \<url\> | Set a reminder.                   |
|  search  |      \<text\>      | Searches for videos from YouTube. |
