import discord
import asyncio
import os

client = discord.Client()



@client.event
async def on_ready():
    print(client.user.id)
    print('ready')
    game = discord.Game('!도움말 을쳐 명령어를 확인하세요.')
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith('!도움말'):
        embed = discord.Embed(title="도움말", color=0x00ff00)
        embed.add_field(name="맵", value="**사용법**: ``!맵 [맵]``", inline=True)
        await message.channel.send(embed=embed)
    if message.content.startswith('!맵 미라마'):
        embed = discord.Embed()
        embed.set_image(url="https://imgur.com/zpkQEYO")
        embed.add_field(name="설명", value="멕시코를 모티브로 만들어진 사막을 배경으로 한 계곡.", inline=True)
        await message.channel.send(embed=embed)
    if message.content.startswith('!맵 에란겔'):
        embed = discord.Embed()
        embed.set_image(url="https://imgur.com/E90E2Ek")
        embed.add_field(name="설명", value="러시아 콘셉트의 전장으로 흑해에 있는 가상의 섬.", inline=True)
        await message.channel.send(embed=embed)
    if message.content.startswith('!맵 사녹'):
        embed = discord.Embed()
        embed.set_image(url="https://imgur.com/9Dse5uk")
        embed.add_field(name="설명", value="풍성한 수풀과 수로 그리고 고유의 구조물과 마을이 있는 태국과 필리핀을 비롯한 동남아시아 지역의 섬.", inline=True)
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
        embed.add_field(name="설명", value="비켄디는 6x6km 크기의 맵으로, 기존 에란겔/미라마보다는 빠르고 사녹보다는 창의적인 전략을 펼칠 수 있는 전장입니다..", inline=True)
        await message.channel.send(embed=embed)
    if message.content.startswith('!!!오늘의 공지'):
        embed = discord.Embed()
        embed.add_field(name="오늘의 공지!", value="공식 서버가 될 날이 얼마 안남았습니다.\n조금만 더 기다려 주세요!")
        await message.channel.send(embed=embed)

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
