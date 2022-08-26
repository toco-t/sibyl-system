import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from random import random


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
SERVER = os.getenv("DISCORD_SERVER")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix=".", intents=intents)


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


@bot.command(name="scan", help=": Scan a target's Psycho-Pass")
async def scan(context, target):
    crime_coefficient = round(random() * 400, 1)

    if crime_coefficient < 100:
        enforcement_action = (
            f"Enforcement action not required.\n"
            f"The trigger is now locked..."
        )
    elif crime_coefficient < 300:
        enforcement_action = (
            f"Enforcement mode: Non-lethal Paralyzer\n"
            f"Please aim carefully and subdue the target..."
        )
    else:
        enforcement_action = (
            f"Enforcement mode: Lethal Eliminator\n"
            f"Please aim carefully and eliminate the target..."
        )

    cymatic_scan_quote = (
        f"{target}'s crime coefficient: {crime_coefficient} "
        f"- {'under' if crime_coefficient < 100 else 'over'} {round(crime_coefficient)}\n"
        f"{enforcement_action}"
    )

    await context.send(cymatic_scan_quote)


@bot.command(name="destroy", help=": Destroy the target")
@commands.has_role("Inspector")
async def destroy(context, target):
    decomposer_quote = (
      f"{target}'s threat judgement has been reappraised.\n"
      f"Enforcement mode: Destroy Decomposer\n"
      f"Target will be completely annihilated.\n"
      f"Please proceed with maximum caution..."
    )

    await context.send(decomposer_quote)


@bot.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise


@bot.event
async def on_command_error(context, error):
    if isinstance(error, commands.errors.CheckFailure):
        await context.send('You are an invalid user.')


bot.run(TOKEN)
