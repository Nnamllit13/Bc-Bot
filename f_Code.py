import datetime
from discord.ext import commands, tasks
import discord
from dataclasses import dataclass

BOT_TOKEN = '-'
#CHANNEL_ID = 695915954621906955

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot is ready")
#    channel = bot.get_channel(CHANNEL_ID)
#    await channel.send("Bot has loaded")

@bot.command()
async def Test(ctx):
    await ctx.reply("Test erfolgreich")
    print("Es Geht :)")

@bot.command()
async def test(ctx):
    await ctx.reply("Test erfolgreich")
    print("Es Geht :)")

@bot.command()
async def about(ctx):
    await ctx.reply(f"Made by Nnamllit11#9847 (V1.2)")
    await ctx.send(f"No longer suport for prefix commands :(")
    print("Es Geht :)")





bot.run(BOT_TOKEN)