import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
SERVER = os.getenv("DISCORD_SERVER")

intents = discord.Intents.default()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    # server = discord.utils.find(lambda s: s.name == SERVER, client.guilds)
    server = discord.utils.get(client.guilds, name=SERVER)

    print(f"{client.user} is connected to the following:\n"
          f"{server.name}(ID: {server.id})")

    members = "\n - ".join([member.name for member in server.members])
    print(f"Registered Members:\n - {members}")


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f"User authentication.../n"
        f"Inspector: {member.name}/n"
        f"Dominator usage approved./n"
        f"You are a valid user."
    )


client.run(TOKEN)
