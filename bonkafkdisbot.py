import discord
from datetime import datetime
from PIL import ImageGrab

token = 'ODc5NzczMzIyNTgwMjA1NjA4.G-cp4k.aLqTurQfNAZS-feCnJgtNDJTcBjEhLL8bhGEvU'
intents=discord.Intents.default()
intents.members = True
intents.message_content = True
client = discord.Client(intents=intents, activity=discord.Game(name='bonk'))

now = datetime.now()
starttime_string = now.strftime("%m/%d/%Y %H:%M")
print('started at--- ', starttime_string)

@client.event
async def on_ready():
    print(f"Bot logged in as {client.user}")

@client.event
async def on_message(message):
    user_message = str(message.content)
    author = str(message.author)
    if author == client.user:
        return
    if user_message == '?info':
        print('info command used by', author)
        now = datetime.now()
        datetimenow = now.strftime("%m/%d/%Y %H:%M")
        my_files = [
            discord.File('C:/Users/clari/Documents/code/info1.png'),
            discord.File('C:/Users/clari/Documents/code/info2.png'),
        ]
        await message.channel.send(files=my_files)
        uptime_stats = ('AFK bot has been online since', starttime_string,  'current time is', datetimenow)
        await message.channel.send(uptime_stats)

client.run(token)