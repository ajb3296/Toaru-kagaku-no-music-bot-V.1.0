import discord
import asyncio
import logging
import sys
import time
import multiprocessing
from lavalinkstart import *
from discord.ext import commands
from config import *
from utils import *

async def status_task():
    while True:
        try:
            await bot.change_presence(
                activity = discord.Game ("%shelp : 도움말" %commandInt)
            )
            await asyncio.sleep(10)
            await bot.change_presence(
                activity = discord.Game ("%d 개의 서버에서 놀고있어요!" %len(bot.guilds))
            )
            await asyncio.sleep(10)
            await bot.change_presence(
                activity = discord.Game ("%d 명의 유저들과 놀고있어요!" %len(bot.users))
            )
            await asyncio.sleep(10)
        except:
            pass

class  Toaru_kagaku_no_music_bot (commands.Bot) :
    def __init__ (self) :
        super().__init__ (
            command_prefix=commandInt
        )
        self.remove_command("help")
      
        # enable logging
        logging.basicConfig(
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            level=logging.INFO)

        LOGGER = logging.getLogger(__name__)

        # if version < 3.6, stop bot.
        if sys.version_info[0] < 3 or sys.version_info[1] < 6:
            LOGGER.error("3.6 버전 이상의 Python 이 있어야 합니다. 여러 기능이 해당 Python3.6 버전을 따릅니다. 봇 종료.")
            quit(1)
      
        process = multiprocessing.Process(target=child_process, args=(lavalinklink, ))
        process.start()
        time.sleep(20)

        for i in EXTENSIONS :
            self.load_extension (i)

    async def on_ready (self) :
        print(BOT_NAME_TAG_VER)
        print('Logged on as ' + self.user.name)
        await self.change_presence(
            activity = discord.Game ("%shelp : 도움말" %commandInt), 
            status = discord.Status.online,  
            afk = False
        )
        bot.loop.create_task(status_task())
    
    
    async def on_message (self, message) :
        if message.author.bot :
            return
        else :
            await self.process_commands (message)

bot = Toaru_kagaku_no_music_bot ()
bot.run (TOKEN, bot=True)
