import discord
from discord.ext import tasks
from discord.channel import TextChannel
from datetime import datetime
import time
import random

TOKEN = ""
CHANNEL_ID = 
SERVER_ID = 

client = discord.Client()

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@tasks.loop(seconds=1)
async def loop():

    # start client
    await client.wait_until_ready()

    # get channel
    channel = client.get_channel(CHANNEL_ID)

    now = datetime.now()
    now = now.strftime('%H:%M')

    if now == now:
        
        # test time
        for x in range(14400, 0, -1):
            await channel.send(x)
            time.sleep(1)

            # debug
            print(x)

            if x == 0:
                channel.send("dummy text")
                break

loop.start()
loop.stop()

client.run(TOKEN)