import discord
import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv()

secretToken = os.environ.get("TOKEN")


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

client = MyClient()
client.run(secretToken)
