import discord
from discord.ext import commands
from waste import reciclar
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.command()
async def clasificar(ctx, residuo: str):
    result = reciclar(residuo)
    await ctx.send(result)

bot.run("MTMyNjMzMjgyNjk5NTY1ODc3Mg.GmURYp.xqwUL2kPfgzQbnseAVAudk8rUWRHXIMjOecdk0")