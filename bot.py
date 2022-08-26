import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
SERVER = os.getenv("DISCORD_SERVER")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    # server = discord.utils.find(lambda s: s.name == SERVER, client.guilds)
    server = discord.utils.get(bot.guilds, name=SERVER)

    print(f"{bot.user} is connected to the following:\n"
          f"{server.name}(ID: {server.id})")

    members = "\n - ".join([member.name for member in server.members])
    print(f"Registered Members:\n - {members}")


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f"User authentication.../n"
        f"Inspector: {member.name}/n"
        f"Dominator usage approved./n"
        f"You are a valid user."
    )


@bot.command(name="activate", help=": Activates the Dominator")
async def activate(context):
    activation_quote = (
        f"Activating...\n"
        f"Dominator: Portable Psychological Diagnosis and Suppression System\n"
        f"is now online."
    )

    await context.send(activation_quote)


@bot.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise


bot.run(TOKEN)
