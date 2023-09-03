import discord
import asyncio
import time

TOKEN = '...'

GUILD_NAME = 'SummerCup2023'

CHANNEL_NAME = 'results'

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord')
    guild = discord.utils.get(client.guilds, name=GUILD_NAME)
    channel = discord.utils.get(guild.channels, name=CHANNEL_NAME)
    await delete_all_messages(channel)

async def delete_all_messages(channel):
    async for message in channel.history(limit=None):
        await message.delete()
        time.sleep(0.05)
        
    exit()

client.run(TOKEN)
