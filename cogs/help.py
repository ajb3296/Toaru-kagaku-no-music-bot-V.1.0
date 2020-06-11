import discord
import asyncio
from discord.ext import commands
from config import BOT_NAME_TAG_VER, color_code, commandInt, BOT_NAME, OWNERS, EXTENSIONS

class Help (commands.Cog) :
    def __init__ (self, bot) :
        self.bot = bot

    @commands.command (name = 'help', aliases = ['도움', '도움말', '명령어', '헬프', '?'])
    async def help (self, ctx, *, arg : str  = None) :
        if not arg == None:
            arg = arg.upper()
        if arg == "GENERAL" or arg == "일반":
            embed=discord.Embed(title="**기본적인 명령어**", description='명령어 뒷쪽의 모든 괄호는 빼주세요!', color=color_code)

            if "cogs.about" in EXTENSIONS:
                embed.add_field(name="`%sabout`" %commandInt, value="저에 대한 정보를 알려드려요!", inline=True)

            if "cogs.other" in EXTENSIONS:
                embed.add_field(name="`%s초대`" %commandInt, value="저랑 다른 서버에서 놀고싶으세요? 당신이 서버의 관리자라면 저를 서버에 초대할 수 있어요!", inline=True)
                embed.add_field(name="`%sjava`" %commandInt, value="서버에 설치된 자바 버전을 알려드려요!", inline=True)
                embed.add_field(name="`%suptime`" %commandInt, value="서버가 부팅으로부터 얼마나 지났는지를 알려드려요!", inline=True)
            
            if "cogs.Naver_real_time_search_term" in EXTENSIONS:
                embed.add_field(name="`%s네이버실검`" %commandInt, value="네이버 실시간 검색어 순위를 알려드려요.", inline=True)

            if "cogs.melon" in EXTENSIONS:
                embed.add_field(name="`%s멜론차트`" %commandInt, value="멜론차트 1위부터 10위까지 알려드려요.", inline=True)

            if "cogs.ping" in EXTENSIONS:
                embed.add_field(name="`%sping`" %commandInt, value="핑 속도를 측정해요!", inline=True)
            embed.set_footer(text=BOT_NAME_TAG_VER)
            await ctx.send(embed=embed)

        elif arg == "MUSIC" or arg == "음악":
            if "cogs.music" in EXTENSIONS:
                embed=discord.Embed(title="**음악 명령어**", description='소괄호 () 은(는) 옵션인 경우 쓰입니다. 명령어 뒷쪽의 모든 괄호는 빼주세요!', color=color_code)
                embed.add_field(name=":arrow_forward: | `%splay` [*음악 이름 혹은 Youtube 링크*]" %commandInt, value="> 음악을 재생해요!\n> `%sp`, `%s재생`, `%sㅔ`  을(를) 사용할 수도 있어요." %(commandInt, commandInt, commandInt), inline=False)
                embed.add_field(name=":x: | `%sdisconnect`" %commandInt, value="> 음성 채널을 나갑니다.\n> `%sdc`, `%s연결해제`, `%s나가` 을(를) 사용할 수도 있어요." %(commandInt, commandInt, commandInt), inline=False)
                embed.add_field(name=":track_next: | `%sskip`" %commandInt, value="> 다음 곡으로 넘어갑니다!\n> `%s스킵`, `%ss`, `%sㄴ` 을(를) 사용할 수도 있어요." %(commandInt, commandInt, commandInt), inline=False)
                embed.add_field(name=":loud_sound: | `%svol` *(1~1000)*" %commandInt, value="> 음량을 조절합니다!\n> `%sv`, `%sㅍ`, `%s음량`, `%s볼륨`  을(를) 사용할 수도 있어요." %(commandInt, commandInt, commandInt, commandInt), inline=False)
                embed.add_field(name=":arrow_down_small: | `%snow`" %commandInt, value="> 현재 재생중인 곡을 알려드려요!\n> `%sn`, `%snp`, `%s현재재생중`, `%sㅜ` 을(를) 사용할 수도 있어요." %(commandInt, commandInt, commandInt, commandInt), inline=False)
                embed.add_field(name=":regional_indicator_q: | `%sq` *(페이지 수)*" %commandInt, value="> 재생목록 리스트의 *(페이지 수)*의 페이지에 있는 재생목록을 알려드려요!\n> `%s큐`, `%sㅂ` 을(를) 사용할 수도 있어요." %(commandInt, commandInt), inline=False)
                embed.add_field(name=":play_pause: | `%spause`" %commandInt, value="> 음악을 일시정지해요!\n> `%s일시정지` 을(를) 사용할 수도 있어요." %commandInt, inline=False)
                embed.add_field(name=":twisted_rightwards_arrows: | `%sshuffle`" %commandInt, value="> 다음 곡부터 재생목록의 음악들이 랜덤으로 나와요\n> `%s셔플` 을(를) 사용할 수도 있어요." %commandInt, inline=False)
                embed.add_field(name=":repeat: | `%srepeat`" %commandInt, value="> 현재 듣고 계시는 노래를 포함한 재생목록의 모든 노래를 반복해서 들려드려요!\n> `%sloop`,`%sl`, `%s반복`, `%sㅣ` 을(를) 사용할 수도 있어요." %(commandInt, commandInt, commandInt, commandInt), inline=False)
                embed.add_field(name=":stop_button: | `%sstop` *(분)*" %commandInt, value="> 듣고 계시는 음악을 끄고 재생목록을 제거해요!\n> 분 에 분단위 시간을 넣으시면 해당 분 후 음악이 자동으로 멈춥니다!\n> `%s중지`, `%s정지` 을(를) 사용할 수도 있어요." %(commandInt, commandInt), inline=False)
                embed.add_field(name=":clock: | `%sseek` [*+(초) 혹은 -(초)*]" %commandInt, value="> 음악을 명령어 뒤의 숫자만큼 초단위로 진행시간을 조절해요!\n> `%s탐색` 을(를) 사용할 수도 있어요." %commandInt, inline=False)
                embed.add_field(name=":asterisk: | `%sremove` [*재생목록에서의 음악 순서 번호*]" %commandInt, value="> 재생목록에서 음악을 제거해요!\n> `%s제거` 을(를) 사용할 수도 있어요." %commandInt, inline=False)
                embed.add_field(name=":globe_with_meridians: | `%sfind` [*검색하실 음악명*]" %commandInt, value="> Youtube 에서 음악을 검색하고 결과를 알려드려요!", inline=False)
                embed.set_footer(text=BOT_NAME_TAG_VER)
                await ctx.send(embed=embed)

        elif arg == "DEV" or arg == "개발" or arg == "개발자":
            if ctx.author.id in OWNERS:
                embed=discord.Embed(title="**개발자 명령어**", description='명령어 뒷쪽의 모든 괄호는 빼주세요!', color=color_code)
                embed.add_field(name="`%s서버목록`" %commandInt, value="> 제가 들어가 있는 총 서버수, 총 서버의 계정개수 합, 서버 리스트를 출력해요!", inline=False)
                embed.add_field(name="`%smodules`" %commandInt, value="> 모든 모듈의 이름을 알려줘요!", inline=False)
                embed.add_field(name="`%sload` [*모듈명*]" %commandInt, value="> 모듈을 로드해요!", inline=False)
                embed.add_field(name="`%sunload` [*모듈명*]" %commandInt, value="> 모듈을 언로드해요!", inline=False)
                embed.add_field(name="`%sreload` [*모듈명*]" %commandInt, value="> 모듈을 리로드해요!", inline=False)
                embed.add_field(name="`%sserverinfo`" %commandInt, value="봇 서버의 사양을 알려줘요!", inline=False)
                embed.set_footer(text=BOT_NAME_TAG_VER)
                await ctx.send(embed=embed)

        else:
            embed=discord.Embed(title="**도움말**", description='안녕하세요! 전 %s 에요! 아래에 있는 명령어들을 이용해 도움말을 보세요!' %BOT_NAME, color=color_code)
            embed.add_field(name="`%shelp general`" %commandInt, value="> 기본적인 명령어들을 보내드려요!", inline=False)

            if "cogs.music" in EXTENSIONS:
                embed.add_field(name="`%shelp music`" %commandInt, value="> 음악 관련 명령어들을 보내드려요!", inline=False)

            if ctx.author.id in OWNERS:
                embed.add_field(name="`%shelp dev`" %commandInt, value="> 개발자님이 사용가능한 명령어들을 보내드려요!", inline=False)
            embed.set_footer(text=BOT_NAME_TAG_VER)
            await ctx.send(embed=embed)
            

def setup (bot) :
    bot.add_cog (Help (bot))
    print ('Help loaded!')
