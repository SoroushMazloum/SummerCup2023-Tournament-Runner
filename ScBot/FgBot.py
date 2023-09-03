import discord
import asyncio
import datetime

TOKEN = '...'

client = discord.Client()

@client.event
async def on_ready():
    print('Bot is ready')

    server = discord.utils.get(client.guilds, name='SummerCup2023')
    if server is None:
        print('Server not found')
        exit()

    channel = discord.utils.get(server.channels, name='results')
    if channel is None:
        print('Channel not found')
        exit()
    file = open('Result.txt', 'r')
    Game = file.readline()
    ut = datetime.datetime.utcnow()
    utc = ut.strftime('%H:%M:%S')
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime('%H:%M:%S')
    await channel.send('🟢' + ' Game End: ' + Game + '  ⏱ ' + formatted_time + ' (IR)  ' + '🌐 ' + utc + ' (UTC)')
    await channel.send('---------------------')
    exit()

client.run(TOKEN)
