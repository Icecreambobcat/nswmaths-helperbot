import discord
import os
from dotenv import load_dotenv

load_dotenv()


class Bot:
    instance = discord.Bot()
    token = os.getenv("TOKEN")


@Bot.instance.event
async def on_ready():
    print(f"Logged in as {Bot.instance.user}")


@Bot.instance.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond("Hey!")


Bot.instance.run(Bot.token)
