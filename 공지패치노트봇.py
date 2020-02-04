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
    if message.content.startswith('!!!오늘의 공지'):
        embed = discord.Embed()
        embed.add_field(name="오늘의 공지!", value="배고프다.")
        await message.channel.send(embed=embed)
    if message.content.startswith('!!!패치노트'):
        embed = discord.Embed()
        embed.add_field(name="#[패치버전]", value="[패치내용]")
        await message.channel.send(embed=embed)

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
