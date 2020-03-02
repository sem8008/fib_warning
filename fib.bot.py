import discord
import os
client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("!명령어")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("!명령어"):
        await message.channel.send("서버주소 관리자 OP모집(모든 명령어는 !를 붙혀주세요!)")
    if message.content.startswith("하"):
        await message.channel.send("악")
    if message.content.startswith("!서버주소"):
        await message.channel.send("FIB WARNING님께 갠디하시면 빠른 시일내에 연락주실거에요 !")
    if message.content.startswith("안녕하세요"):
        await message.channel.send("어서오세요!")
    if message.content.startswith("!관리자"):
        await message.channel.send("FIB WARNING,하이원,무너,지성님이 관리자이십니다.")
    if message.content.startswith("!OP모집"):
        await message.channel.send("관리자 모집은 재능이 있으시다고 생각되시면 FIB WARNING으로 연락해주세요!")


access_token = os.environ["BOT_TOKEN"]
client.run("access_token")
