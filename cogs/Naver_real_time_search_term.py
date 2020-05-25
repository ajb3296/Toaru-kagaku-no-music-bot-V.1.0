import discord
import asyncio
import json
import urllib.parse
from utils.crawler import getReqJSON
from discord.ext import commands
from config import BOT_NAME_TAG_VER, color_code

class Naver_real_time_search_term (commands.Cog) :
    def __init__ (self, bot) :
        self.bot = bot
        self.url = 'https://www.naver.com/srchrank?frm=main&ag=20s&gr=0&ma=0&si=0&en=0&sp=0'

    @commands.command(name = '네이버실검', aliases = ['Naver_real_time_search_term'])
    async def Naver_real_time_search_term(self, ctx) :
        embed=discord.Embed(title="**네이버 실시간 검색어 현황**", description="오늘자 네이버 실검 현황이에요!", color=color_code)
        res = await getReqJSON (self.url)
        rank = [*map(lambda item: item['keyword'], res['data'])]
        idx = 1
        for i in rank:
            if idx == 11:
                break
            else: 
                i1=urllib.parse.quote(i)
                i2 = "https://search.naver.com/search.naver?query={}".format(i1)
                embed.add_field(name=f'{idx}위', value="[%s](<%s>)" %(i, i2), inline=False)
                idx += 1
        embed.set_footer(text=BOT_NAME_TAG_VER)
        await ctx.send(embed=embed)

def setup (bot) :
    bot.add_cog (Naver_real_time_search_term (bot))
    print ('Naver_real_time_search_term loaded!')
