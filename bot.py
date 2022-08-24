import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"{client.user} has established connection to Discord...")


client.run(TOKEN)
