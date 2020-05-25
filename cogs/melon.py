import discord
import asyncio
import json
from bs4 import BeautifulSoup
import urllib.parse
import requests
from utils.crawler import getReqTEXT
from discord.ext import commands
from config import BOT_NAME_TAG_VER, color_code

class Melon_chart (commands.Cog) :
    def __init__ (self, bot) :
        self.bot = bot
        self.url = 'https://www.melon.com/chart/index.htm'
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}

    @commands.command(name = '멜론', aliases = ['멜론차트', 'melon', 'melonchart'])
    async def 멜론차트(self, ctx) :
        data = await getReqTEXT (self.url, self.header)
        parse = BeautifulSoup(data, 'lxml')
        titles = parse.find_all("div", {"class": "ellipsis rank01"})
        songs = parse.find_all("div", {"class": "ellipsis rank02"})
        title = []
        song = []
        for t in titles:
            title.append(t.find('a').text)
        for s in songs:
            song.append(s.find('span', {"class": "checkEllipsis"}).text)
        embed=discord.Embed(title="**멜론 차트**", description="오늘의 멜론 차트에요!", color=color_code)
        num = 1
        for i in range(0, 10) :
            embed.add_field(name=str(num) + "위", value = f"{title[i]} - {song[i]}", inline=False)
            num += 1
        embed.set_footer(text=BOT_NAME_TAG_VER)
        await ctx.send(embed=embed)

def setup (bot) :
    bot.add_cog (Melon_chart (bot))
    print ('Melon_chart loaded!')
