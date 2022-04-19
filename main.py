import discord
from models import User
import os

userid = []
users = []

class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}")

    async def on_message(self, message):
        if message.author.id not in userid:
            userid.append(message.author.id)
            users.append(message.author.name)

        test = User('gerbsec')
        test.add_fword()
        print(test.fword)

client = MyClient()
client.run(os.environ['BOT'])