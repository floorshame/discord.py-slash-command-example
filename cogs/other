import discord
from discord.ext import commands
from discord import app_commands


class ping(commands.Cog, name="ping"):
    def __init__(self, bot : commands.Bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Test Command")
    async def ping(self, interaction : discord.Interaction):
        await interaction.response.send_message("Pong")

async def setup(client:commands.Bot) -> None:
    await client.add_cog(ping(client))
