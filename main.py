import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ 봇 로그인됨: {bot.user}")

@bot.command()
async def 안녕(ctx):
    await ctx.send("안녕하세요, 디스코드 봇이에요!")

bot.run("")
