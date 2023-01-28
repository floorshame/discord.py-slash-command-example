from typing import Optional

import discord
from discord import app_commands
from discord.ext import commands
import os
from os.path import isfile, join
from os import listdir



class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(intents=discord.Intents().all(), command_prefix="$")

    async def setup_hook(self):
        
        # cogs go here
        for folder in os.listdir("cogs"):
            for file in listdir(f"cogs/{folder}"):
                if (isfile(f"cogs/{folder}/{file}")):
                    await self.load_extension(f'cogs.{folder}.{file.replace(".py", "")}')
                    
        synced = await self.tree.sync()        

    async def on_ready(self):
        
        print(f'Logged in as {bot.user} (ID: {bot.user.id})')
        for command in self:
            print(command)

            
intents = discord.Intents.default()
bot = MyBot()




bot.run('enter token here')   
