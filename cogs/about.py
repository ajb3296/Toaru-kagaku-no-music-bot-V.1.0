import discord
import asyncio
from discord.ext import commands
from config import BOT_NAME_TAG_VER, color_code, commandInt, BOT_NAME, OWNERS

class About (commands.Cog) :
    def __init__ (self, bot) :
        self.bot = bot

    @commands.command (aliases = ['봇', '개발자', '기부', '봇정보', '봇관련', '관련', '정보'])
    async def about (self, ctx) :
        about_cmd = """Chiyo(치요)#0720 에서 파생된 속도를 중시한 음악봇!

저의 자세한 사용법에 대해서는 `%shelp` 을(를) 사용해 주세요.
Github : 는 무슨 코드공개 아직 안합니다.
Chiyo(치요)#0720 의 발전을 위한 랜선 혹은 다른 기부문의는? <@%s> 에게!""" %(commandInt, str(OWNERS).replace("[", "").replace("]", ""))
        embed=discord.Embed(title="**봇에 대한 정보**", description=about_cmd, color=color_code)
        embed.add_field(name="서버수", value=len(self.bot.guilds), inline=True)
        embed.add_field(name="유저수", value=len(self.bot.users), inline=True)
        embed.set_footer(text=BOT_NAME_TAG_VER)
        await ctx.send(embed=embed)
        

def setup (bot) :
    bot.add_cog (About (bot))
    print ('About loaded!')
