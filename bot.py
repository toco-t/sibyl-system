import discord
import os
from discord.ext import commands, tasks
from discord_webhook import DiscordWebhook, DiscordEmbed
from dotenv import load_dotenv
from random import random, choice


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
SERVER = os.getenv("DISCORD_SERVER")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
IMG_URL = os.getenv("IMG_URL")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix=".", intents=intents)

quotes = [
    "*'A perfect plan doesn't mean having everything go within expectations. A perfect plan is achieved when it has "
    "the plasticity needed to flexibly deal with troubles...'*",
    "*'I wonder what sort of criteria you use to divide people into good and evil...'*",
    "*'I think the only time people really have value is when they act according to their own will...'*",
    "*'Everyone just lives in their own cell, and the system tames them by giving them each their own personal "
    "serenity...'*",
    "*'When a man faces fear, his soul is tested. What he was born to seek… what he was born to achieve… his true "
    "nature will become clear...'*",
    "*'Beautiful flowers, too, eventually wither and fall. That’s the fate of all living beings...'*",
    "*'Books are not something that you just read words in. They’re also a tool to adjust your senses...'*",
    "*'In order to measure a person’s worth, you must do more than push them. The real way to test their worth is to "
    "give them power. When they gain the freedom to act outside the boundaries of law and ethics, you can sometimes "
    "see their souls...'*",
    "*'What are human desires? What I think the most troublesome desire is for attention. It’s the source of jealousy "
    "and relationship problems, too...'*",
    "*'For some time researchers have understood that moderate stress has beneficial effects. It boosts the immune "
    "system for example. Stress motivates and prepares us for action. It compels our body to survive...'*",
    "*'The opposite of boredom is not pleasure…but excitement. People will gladly seek out any kind of excitement, "
    "even pain...'*"
]


@bot.event
async def on_ready():
    # server = discord.utils.find(lambda s: s.name == SERVER, client.guilds)
    server = discord.utils.get(bot.guilds, name=SERVER)

    print(f"{bot.user} is connected to the following:\n"
          f"{server.name}(ID: {server.id})")

    members = "\n - ".join([member.name for member in server.members])
    print(f"Registered Members:\n - {members}")

    await send_quotes.start()


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f"User authentication.../n"
        f"Enforcer: {member.name}/n"
        f"Dominator usage approved./n"
        f"You are a valid user."
    )


@bot.command(name="activate", help=": Activates the Dominator")
async def activate(context):
    activation_message = (
        f"Activating...\n"
        f"Dominator: Portable Psychological Diagnosis and Suppression System\n"
        f"is now online."
    )

    await context.send(activation_message)


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

    cymatic_scan_message = (
        f"{target}'s crime coefficient: {crime_coefficient} "
        f"- {'under' if crime_coefficient < 100 else 'over'} {round(crime_coefficient // 10) * 10}\n"
        f"{enforcement_action}"
    )

    await context.send(cymatic_scan_message)


@bot.command(name="destroy", help=": Destroy the target")
@commands.has_role("Inspector")
async def destroy(context, target):
    decomposer_message = (
      f"{target}'s threat judgement has been reappraised.\n"
      f"Enforcement mode: Destroy Decomposer\n"
      f"Target will be completely annihilated.\n"
      f"Please proceed with maximum caution..."
    )

    await context.send(decomposer_message)


@tasks.loop(minutes=2)
async def send_quotes():
    webhook = DiscordWebhook(WEBHOOK_URL, content="")

    embed = DiscordEmbed(title=choice(quotes))
    embed.set_author(name="Shogo Makishima")
    embed.set_image(url=IMG_URL)

    webhook.add_embed(embed)
    response = webhook.execute()


@bot.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as error_log:
        if event == 'on_message':
            error_log.write(f'Unhandled message: {args[0]}\n')
        else:
            raise


@bot.event
async def on_command_error(context, error):
    if isinstance(error, commands.errors.CheckFailure):
        await context.send('You are an invalid user.')


bot.run(TOKEN)
