import discord
import asyncio
import datetime
import os
import lupa
from lupa import LuaRuntime
lua = LuaRuntime(unpack_returned_tuples=True)
import sys, traceback

client = discord.Client()
url=''
botOwner = "266640111897149440"

@client.event
async def on_ready():
    now = datetime.datetime.now()
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name="!help", type=1))
    f = open("refresh.txt", "r")
    a = f.read().split(" ")
    if len(a) > 1:
        if a[0] == "true":
            channel = discord.Object(id=int(a[1]))
            embed=discord.Embed(title="<:Lua:484461968640573450> AR Lua Developers", description="لقد تم تحديث البوت", color=0x000080)
            embed.set_footer(text=now.strftime("%Y/%m/%d %H:%M:%S"))
            n = await client.send_message(channel, embed=embed)
            await asyncio.sleep(2)
            await client.delete_message(n)
            f = open("refresh.txt", "r+")
            f.write("")
            f.close()

bot_prints={}

def clear():
    global bot_prints
    bot_prints={}

def printd(msg, channel="my_ch"):
    ##bot_prints.append(msg)
    bot_prints[len(bot_prints)] = [msg,channel]

@client.event
async def on_message(message):
    global bot_prints
    now = datetime.datetime.now()
    args = message.content.split(" ")
    roleChannelId = '484460279770513410'
    if message.channel.id == roleChannelId:
        if message.content.startswith('<:Lua:484461968640573450>'):
            role = discord.utils.get(message.author.server.roles, name='Student')
            await client.add_roles(message.author, role)
            embed=discord.Embed(title="<:Lua:484461968640573450> AR Lua Developers", color=0x000080)
            embed.add_field(name="مُبارك", value=":white_check_mark: !لقد حصلت على رتبة طالب بنجاح", inline=False)
            embed.set_footer(text=now.strftime("%Y/%m/%d %H:%M:%S"))
            await client.send_message(message.author, embed=embed)
            await client.delete_message(message)
        else:
            embed=discord.Embed(title="<:Lua:484461968640573450> AR Lua Developers", color=0x000080)
            embed.add_field(name=":مُلاحظة", value="<#484460279770513410> في قناة `:Lua:` للحصول على رتبة طالب، أكتب", inline=False)
            embed.set_footer(text=now.strftime("%Y/%m/%d %H:%M:%S"))
            await client.send_message(message.author, embed=embed)
            await client.delete_message(message)

    if message.content.startswith(client.user.mention):
        embed=discord.Embed(title="<:Lua:484461968640573450> AR Lua Developers", description=".مرحبًا، أنا بوت خادم مُبرمجين لوا العرب\n`!` :رمز بداية الايعازات الخاصة بي هو\n`!help`:لرؤية قائمة الايعازات الخاصة بي اكتب\n", color=0x000080)
        embed.set_footer(text=now.strftime("%Y/%m/%d %H:%M:%S"))
        await client.send_message(message.author, embed=embed)
        await client.delete_message(message)

    if message.content.startswith("!topics"):
        embed=discord.Embed(title="<:Lua:484461968640573450> AR Lua Developers", color=0x000080)
        embed.add_field(name="<:postit:484789760292945933>  البرمجيات التركيبية - القوانين والمبادئ التوجيهية" , value="https://atelier801.com/topic?f=6&t=782400", inline=False)
        embed.add_field(name="<:postit:484789760292945933>  البرمجيات التركيبية", value="https://atelier801.com/topic?f=6&t=779696", inline=False)
        embed.add_field(name="<:postit:484789760292945933>  ! طلب لعبةٍ صغيرةٍ" , value="https://atelier801.com/topic?f=6&t=820736", inline=False)
        embed.add_field(name="<:postit:484789760292945933>  مساعدة] الأخطاء]" , value="https://atelier801.com/topic?f=6&t=852486", inline=False)
        embed.add_field(name="<:postit:484789760292945933> تعليم] لوا والالعاب الصغيرة ]", value="https://atelier801.com/topic?f=6&t=852781", inline=False)
        embed.set_footer(text=now.strftime("%Y/%m/%d %H:%M:%S"))
        await client.send_message(message.author, embed=embed)
        await client.delete_message(message)
    if "484462534154256395" in [y.id for y in message.author.roles]:
        if message.content.startswith("!clear"):
            mm=message.content.split('!clear ')[1]
            nn=0
            async for m in client.logs_from(message.channel, limit=int(mm)):
                await client.delete_message(m)
                nn+=1
            embed=discord.Embed(title="<:Lua:484461968640573450> AR Lua Developers", description=".لقد تم حذف "+str(nn)+" رسالة", color=0x000080)
            embed.set_footer(text=now.strftime("%Y/%m/%d %H:%M:%S"))
            n = await client.send_message(message.channel, embed=embed)
            await asyncio.sleep(2)
            await client.delete_message(n)

    if message.author.id == botOwner:
        if message.content.startswith("!refresh"):
            f = open("refresh.txt", "r+")
            f.write("true "+str(message.channel.id))
            f.close()
            await client.delete_message(message)
            await client.logout()
            os.system("python LuaDev.py")
            exit()
    else:
        if message.content.startswith("!refresh"):
            embed=discord.Embed(title="<:Lua:484461968640573450> AR Lua Developers", color=0x000080)
            embed.add_field(name=":مُلاحظة", value=":x: لا يُمكنك استخدام هذا الايعاز", inline=False)
            embed.set_footer(text=now.strftime("%Y/%m/%d %H:%M:%S"))
            await client.send_message(message.author, embed=embed)
            await client.delete_message(message)

    if message.channel.id == "484820738830761984":
        if message.content.startswith('!lua') and ("```lua" in message.content):
            if message.author.id != client.user.id:
                try:
                    print("new script loaded :")
                    logs = client.logs_from(message.channel)
                    script = message.content.split("!lua")[1].split("```lua")[1].split("```")[0]
                    lua.execute("""
                    print = python.eval("printd")
                    """+script)
                    for p in bot_prints:
                        if bot_prints[p][1] == "my_ch":
                            await client.send_message(message.channel, str(bot_prints[p][0]))
                        else:
                            await client.send_message(discord.Object(id=bot_prints[p][1]), str(bot_prints[p][0]))
                    clear()
                except Exception as err:
                    error = str(traceback.format_exc())
                    #error = error[error.find('File "<string>"'):]
                    await client.send_message(message.channel, "```"+str(error)+"```")
                    clear()
        else:
            embed=discord.Embed(title="<:Lua:484461968640573450> AR Lua Developers", color=0x000080)
            embed.add_field(name=":مُلاحظة", value="<#484820738830761984> يُمكنك فقط تشغيل سكربتات لوا في قناة\nللدردشة <#484460318941118486> يرجى استخدام قناة", inline=False)
            embed.set_footer(text=now.strftime("%Y/%m/%d %H:%M:%S"))
            await client.send_message(message.author, embed=embed)
            await client.delete_message(message)

    if message.content.startswith('!help'):
        embed=discord.Embed(title="<:Lua:484461968640573450> AR Lua Developers", color=0x000080)
        embed.add_field(name="● !help" , value="يظهر الايعازات الخاصة بالبوت", inline=False)
        embed.add_field(name="● !lua` ```lua\ncode``` `" , value="<#484820738830761984> يشغل سكربت لوا في قناة", inline=False)
        embed.add_field(name="● !topics" , value="يعرض بعض المواضيع المفيدة المتعلقة بلوا", inline=False)
        embed.add_field(name="● !clear `X`" , value="يحذف العدد الذي عينته من الرسائل", inline=False)
        embed.add_field(name="● !refresh" , value="يعيد تشغيل البوت", inline=False)
        embed.set_footer(text=now.strftime("%Y/%m/%d %H:%M:%S"))
        await client.send_message(message.author, embed=embed)
        await client.delete_message(message)

@client.event
async def on_message_delete(message):
    now = datetime.datetime.now()
    if message.author.id != client.user.id:
        channel = discord.Object(id=485103216212836355)
        embed=discord.Embed(description=str(message.content))
        embed.add_field(name="**Message:**" , value=str(message.content), inline=False)
        embed.set_author(name=str(message.author), icon_url=str(message.author.avatar_url))
        embed.set_footer(text="Deleted message in <"+str(message.channel.id)+"> at "+now.strftime("%Y/%m/%d %H:%M:%S"))
        await client.send_message(channel, embed=embed)

client.run('NDg0NDkyMDI2NTQxMjQ0NDI4.Dmi1gQ.mbPIA1wdo7XXzoPSksrwF3oqvmQ')
