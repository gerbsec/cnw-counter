from discord.ext import commands
from models import User
bot = commands.Bot('.')
users = {}
@bot.event
async def on_message(message):
    if message.author.id not in users.keys():
        users[message.author.id] = User(message.author.name)


@bot.listen()
async def on_message(message):
    if 'wallah' in message.content.lower():
        users[message.author.id].wallah += 1
    elif 'fuck' in message.content.lower():
        users[message.author.id].fword += 1
    elif 'shit' in message.content.lower():
        users[message.author.id].sword += 1
    elif 'ass' in message.content.lower():
        users[message.author.id].aword += 1
    
bot.run('lol')