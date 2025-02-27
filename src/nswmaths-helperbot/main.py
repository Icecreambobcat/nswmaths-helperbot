import discord
from discord import Option, SlashCommandOptionType
import os
import asyncio
from dotenv import load_dotenv

load_dotenv()


class Bot:
    instance = discord.Bot()
    token = os.getenv("TOKEN")
    intents = discord.Intents.default()

    @staticmethod
    def setup_intents() -> None:
        # fine tune perms here
        pass


@Bot.instance.event
async def on_ready() -> None:
    print(f"Logged in as {Bot.instance.user}")


@Bot.instance.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx: discord.ApplicationContext) -> None:
    await ctx.respond("Hey!")


@Bot.instance.slash_command(name="schedule", description="Schedule an image")
async def schedule_image(
    ctx: discord.ApplicationContext,
    image: Option(
        SlashCommandOptionType.attachment,
        required=True,
        description="The image to schedule",
    ),
    delay: Option(
        SlashCommandOptionType.integer,
        required=True,
        description="Post the image in 0~1440 minutes",
        min_value=0,
        max_value=1440,
    ),
    desc: Option(
        SlashCommandOptionType.string,
        required=False,
        description="Image description (optional)",
    ),
) -> None:
    async def send_image(desc: str, delay: int, image: discord.Attachment) -> None:
        # await asyncio.sleep(delay * 60)
        await asyncio.sleep(delay)
        pic = await discord.Attachment.to_file(image)
        await ctx.channel.send(
            content=desc,
            file=pic,
        )

    if type(delay) == int:
        await ctx.send_response(
            content=f"Image scheduled in {delay} seconds",
            # content=f"Image scheduled in {timedelay} minutes",
            ephemeral=True,
        )

        await send_image(desc, delay, image)

    else:
        await ctx.send_response(
            content=f"{delay} is not a valid number!",
            ephemeral=True,
        )


def main() -> None:
    assert type(Bot.token) == str
    Bot.setup_intents()
    Bot.instance.run(Bot.token)


if __name__ == "__main__":
    main()
