import discord
from discord import app_commands
from discord.ext import commands

BOT_TOKEN = '-'

bot = commands.Bot(command_prefix="!", intents = discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot is Up and Ready!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.tree.command(name="test")
async def test(interaction: discord.Integration):
    await interaction.response.send_message(f"Test {interaction.user.mention} It is a Test! :)")
    print("/test user")


@bot.tree.command(name="test2")
@app_commands.describe(thing_to_say = "It is a Test :)")
async def say(interaction: discord.Integration, thing_to_say: str):
    await interaction.response.send_message(f"{interaction.user.name} said: '{thing_to_say}'")
    print("/test2 user")

@bot.tree.command(name="test3")
@app_commands.describe(thing_to_say = "It is a Test :)")
async def say(interaction: discord.Integration, thing_to_say: str):
    await interaction.response.send_message(f"{interaction.user.mention} said: '{thing_to_say}'")
    print("/test3 user")

@bot.tree.command(name="about")
async def test(interaction: discord.Integration):
    await interaction.response.send_message(f"Made by Nnamllit11#9847 (V1.2)")
    print("/about user")













bot.run(BOT_TOKEN)