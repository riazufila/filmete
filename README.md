# Filmete

Filmete is a simple discord bot that uses Watch2Gether API to create a room for a bunch of people in a server to watch videos together.

This is different compared to the normal share screen by Discord in which this bot allows any participant in the room to pause, play, and seek position. This is inclusive of adding videos into the queue.

## Deploy

Firstly, you will need to sign up a discord account prior of creating a bot. Then, you can retrieve the token. This can be done via https://discord.com/developers.

After that, you will need to follow the guide in https://community.w2g.tv/t/watch2gether-api-documentation/133767 to make use of Watch2Gether API that this bot will use for synced streaming.

Finally, clone the repository and execute Filmete.

## Bot Commands

Each command should be started with the prefix, ";".
Such that ";create \<url\>" or ";remind \<period\> \<url\>".

| Commands |     Parameters     | Description                   |
| :------: | :----------------: | ----------------------------- |
|  create  |      \<url\>       | Creates room in Watch2Gether. |
|  remind  | \<period\> \<url\> | Set a reminder.               |
