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
    ut = datetime.datetime.utcnow()
    utc = ut.strftime('%H:%M:%S')
    file = open('Mg', 'r')
    Game = file.readline()
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime('%H:%M:%S')
    await channel.send('🔵' + ' Game Start: ' + Game + '  ⏱ ' + formatted_time + ' (IR)  ' + '🌐 ' + utc + ' (UTC)')
    exit()

client.run(TOKEN)
