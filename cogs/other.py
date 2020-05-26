import discord
import asyncio
from discord.ext import commands
from utils.crawler import getReqTEXT
from bs4 import BeautifulSoup
from config import BOT_NAME_TAG_VER, color_code, BOT_NAME, BOT_ID
import random
import platform
import psutil
from utils.misc import footer

class Other (commands.Cog) :
    def __init__ (self, bot) :
        self.bot = bot
    
    @commands.command (name = '초대', aliases = ['invite'])
    async def invite(self, ctx):
        link = 'https://discord.com/oauth2/authorize?client_id=%s&permissions=3165184&scope=bot' %BOT_ID
        embed=discord.Embed(title="**절 당신이 관리하는 서버에 초대해주시다니!**", description="정말 감사합니다! [여기](<%s>)를 눌러 서버에 초대해주세요!" %link, color=color_code)
        embed.set_footer(text=BOT_NAME_TAG_VER)
        await ctx.send(embed=embed)

    @commands.command (name = 'serverinfo', aliases = ['서버현황', '서버상태', '서버'])
    async def serverinfo(self, ctx) :
        embed=discord.Embed(title="**봇 서버 현황**", color=color_code)
        embed.add_field(name="Platform", value=platform.platform(), inline=False)
        embed.add_field(name="Kernel", value=platform.version(), inline=False)
        embed.add_field(name="Architecture", value=platform.machine(), inline=False)
        embed.add_field(name="CPU Usage", value=str(psutil.cpu_percent()) +"%", inline=False)
        memorystr = str(round((psutil.virtual_memory().used / (1024.0 ** 3)), 1)) + "GB" + " / " + str(round((psutil.virtual_memory().total / (1024.0 ** 3)), 1)) + "GB"
        embed.add_field(name="Memory Usage", value=memorystr, inline=False)
        embed.add_field(name="Python Ver", value=platform.python_implementation(), inline=False)
        embed.add_field(name="Ping", value=str(round(self.bot.latency * 1000)) + "ms", inline=False)
        embed.set_footer(text=BOT_NAME_TAG_VER)
        await ctx.send(embed=embed)

def setup (bot) :
    bot.add_cog (Other (bot))
    print ('Other loaded!')
