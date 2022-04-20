from discord.ext import commands
from models import User
bot = commands.Bot('.')
users = {}
words = ['wallah', 'fword', 'sword', 'aword']
badwords = ['wallah', 'fuck', 'shit', 'ass']
@bot.event
async def on_message(message):
    if message.author.id not in users.keys():
        users[message.author.id] = User(message.author.name)


@bot.listen()
async def on_message(message):
    for index, badword in enumerate(badwords):
        if badword in message.content.lower():
            users[message.author.id].__dict__[words[index]] += 1
    for word in words:
        if users[message.author.id].__dict__[word] >=25:
            await message.author.send(f"Stop saying {word}, you have said it {users[message.author.id].__dict__[word]} times. Clearing your counter now!")
            users[message.author.id].__dict__[word] = 0
bot.run('test') 