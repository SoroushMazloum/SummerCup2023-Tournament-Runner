import discord
import asyncio

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
    msg = input("Your msg: ")
    await channel.send(msg)
    exit()

client.run(TOKEN)
