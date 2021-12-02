import discord
import datetime
from discord import channel
from discord.activity import Game
import openpyxl
import requests
import asyncio
import os
from json import loads


client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    game = discord.Game("성진봇")
    await client.change_presence(status=discord.Status.online, activity=game)
    twitchwanana = "box930205"
    namewanana = "와나나"
    channel = client.get_channel(915863229832503337)
    awanana = 0
    while True:
        headers = {'Client-ID': 'yk4yp1h4y2dzw1voelnjibs25j3hk2'}
        responsewanana = requests.get("https://api.twitch.tv/helix/streams?user_login=" + twitchwanana, headers=headers)
        try:
            if loads(responsewanana.text)['data'][0]['type'] == "live" and awanana == 0:
                await channel.send(namewanana + "님이 방송중입니다.")
                awanana = 1
        except:
            awanana = 0
        await asyncio.sleep(2)



@client.event
async def on_message(message):
    if message.content.startswith("!청소"):
        number = int(message.content.split(" ")[1])
        await message.delete()
        await message.channel.purge(limit=number)
        await message.channel.send(f"{number}개의 메세지 삭제 완료!")

    if message.content == '!안녕':
        await message.channel.send("안녕하세요!전 성진봇이예요!)

    if message.content == '!내정보':
        user = message.author
        date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
        await message.channel.send(f"{message.author.mention}님의 가입일 : {date.year}/{date.month}/{date.day}")
        await message.channel.send(f"{message.author.mention}님의 이름 : {user.name} / 아이디 : {user.id} / 닉네임 : {user.display_name}")

    if message.content.startswith("!투표"):
        vote = message.content[4:].split("/")
        await message.channel.send("★투표 - " + vote[0])
        for i in range(1, len(vote)):
            choose = await message.channel.send("```" + vote[i] + "```")
            await choose.add_reaction('👍')

    if message.content.startswith("!추방"):
        member = message.guild.get_member(int(message.content.split(" ")[1]))
        await message.guild.kick(member, reason=' '.join(message.content.split(" ")[2:]))
        await message.guild.ban(member, reason=' '.join(message.content.split(" ")[2:]))
        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
