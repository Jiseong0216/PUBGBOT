import discord
import asyncio
import os

client = discord.Client()



@client.event
async def on_ready():
    print(client.user.id)
    print('ready')
    game = discord.Game('!도움말 | PUBG BOT')
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith('!도움말'):
        embed = discord.Embed(title="도움말", color=0x555555)
        msg = '도움말입니다. {0.author.mention}'.format(message)
        embed.add_field(name="맵", value="**사용법**: ``!맵 [맵]``", inline=True)
        embed.set_footer(text = "PUBG-BOT")
        await message.channel.send(embed=embed)
    if message.content.startswith('!맵 미라마'):
        embed = discord.Embed()
        embed.set_image(url="https://imgur.com/zpkQEYO")
        embed.add_field(name="설명", value="사막을 테마로 한 미라마는, 전형적인 8x8 사이즈의 맵입니다. PUBG의 모든 맵 가운데서, 땅 면적이 가장 넓으며, 대부분의 지면은 땅이나 작은 도시로 이루어져 있습니다. 지면이 아주 험하기 때문에 오프로드 운전을 함에 있어서 난이도가 상당할 뿐만 아니라, 몸을 숨길 수 있는 나무의 수도 적어, 스나이퍼들에게는 마치 천국과도 같은 곳입니다.", inline=True)
        await message.channel.send(embed=embed)
    if message.content.startswith('!맵 에란겔'):
        embed = discord.Embed()
        embed.set_image(url="https://imgur.com/E90E2Ek")
        embed.add_field(name="설명", value="PUBG에 최초로 탄생한 맵인 에란겔은 다양한 도시, 마을, 높은 산맥, 탁 트인 풀밭 등 여러가지 형태의 지형적 특징을 가지고 있는 8x8 사이즈의 큰 섬입니다.밀리터리 베이스가 있는 남쪽의 작은 섬과 북쪽의 큰 섬을 잇는 2개의 다리는 매우 위험한 경로로 알려져 있습니다.", inline=True)
        await message.channel.send(embed=embed)
    if message.content.startswith('!맵 사녹'):
        embed = discord.Embed()
        embed.set_image(url="https://imgur.com/9Dse5uk")
        embed.add_field(name="설명", value=" PUBG에서 가장 작은 맵인 사녹은, 나무와 언덕으로 빽빽히 채워진 섬입니다. 섬을 가로지르는 강이 있는데, 이에 따라 맵이 세 구역으로 나뉘어 지게 되며 플레이어들은 많은 다리를 이용하여 건널지, 아니면 물을 통해 건널지 선택할 필요가 있습니다. 맵의 크기와 아이템 스폰량의 영향으로, 사녹 맵에서는다른 전형적인 맵에 비해 휘몰아치고 빠른 페이스의 전투를 더욱 더 풍부하게 경험할 수 있을 것입니다.", inline=True)
        await message.channel.send(embed=embed)
    if message.content.startswith('!맵 카라킨'):
        embed = discord.Embed()
        embed.set_image(url="https://imgur.com/IIuORZq")
        embed.add_field(name="설명", value="카라킨은 북아프리카 연안에 위치한 2x2 km 크기의 섬으로,탁 트인 건조한 바위 투성이의 지형으로 이루어져 매 순간 도전 의식을 불러일으킬 것입니다.", inline=True)
        await message.channel.send(embed=embed)
    if message.content.startswith('!맵 훈련장'):
        embed = discord.Embed()
        embed.set_image(url="https://imgur.com/pGhzpSt")
        embed.add_field(name="설명", value="PUBG 훈련장은 2x2km 크기의 새로운 맵 안에서 배틀그라운드의 각종 요소를 연습해 볼 수 있는 콘텐츠입니다.", inline=True)
        await message.channel.send(embed=embed)
    if message.content.startswith('!맵 비켄디'):
        embed = discord.Embed()
        embed.set_image(url="https://imgur.com/GJubKlw")
        embed.add_field(name="설명", value="6x6 사이즈의 눈 덮힌 맵인 비켄디는, 플레이어들에게 색다른 PUBG 경험을 선사합니다. 꽁꽁 얼어붙은 강물, 설원에 특화된 다양한 차량, 적을 추적할 수 있는 발자국과 바퀴자국 등.. 비켄디에서는 완전히 다른 PUBG를 경험할 수 있습니다.", inline=True)
        await message.channel.send(embed=embed)
    if message.content.startswith('!!!오늘의 공지'):
        embed = discord.Embed()
        embed.add_field(name="오늘의 공지!", value="공식 서버가 될 날이 얼마 안남았습니다.\n조금만 더 기다려 주세요!")
        await message.channel.send(embed=embed)

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
