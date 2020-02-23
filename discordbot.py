import re
import textwrap
import discord
import asyncio
import random
from discord.ext import commands
import os

token = os.environ['DISCORD_BOT_TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='h?help | v1.0β'))

    # or, for watching:
    activity = discord.Activity(name='h?help | v1.0β', type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)

    channel = client.get_channel(680727914614095903)
    await channel.send('>>> **Hotdog bot** a ready!')

@client.event
async def on_message(message): 


    # Bot自身が送ったメッセージの場合は処理しない
    if message.author.bot:
            return

    # Helpコマンド
    if message.content == 'h?help':

        # ヘルプのメッセージを作成（ヒアドキュメントを使って視覚的に見やすくしました）
        help_msg = textwrap.dedent('''\
        **__Hotdog Bot__** **Help Menu**

        > `h?help` helpメニューを表示します
        > `h?pong` pong! と返してくれます。 **＊管理者権限が必要です。**
        > 挨拶してみてね！( ひらがなで)
            
        ''')

        await message.channel.send(help_msg)
#以下挨拶一覧
    if message.content == 'こん':
        await message.channel.send('こんにちは～')

    if message.content == 'なにしてる？':
        await message.channel.send('ホットドッグ食べてるよ～')    
    if message.content == 'ひま':
        await message.channel.send('ホットドッグ食べよう！')    
    if message.content == 'やっほー':
        await message.channel.send('やっほー')    
    if message.content == 'ただいま':
        await message.channel.send('おかえり！')        
    if message.content == 'いってきます':
        await message.channel.send('行ってらっしゃい！')
    if message.content == 'ぴえん':
        await message.channel.send('どうしたの？')
    if message.content == 'よろしく':
        await message.channel.send('よろしくね～')  
    if message.content == 'いえい':
        await message.channel.send('やったね！')        
    if message.content == 'どんなおんがくがすき？':
        await message.channel.send('ホットドッグの歌かなぁ')  
    if message.content == 'かくしこまんどみつけた！':
        await message.channel.send('みつかっちゃった！')  
    if message.content == 'Hi':
        await message.channel.send('こんにちは')
    if message.content == 'www':
        await message.channel.send('wwwwww')    
    if message.content == 'おつ':
        await message.channel.send('お疲れ様～')
    if message.content == 'おはよう':
        await message.channel.send('おはよう！')    
    if message.content == 'ほっとどっく':
        await message.channel.send('よんだ？')
    if message.content == 'わかめ':
        await message.channel.send('このBotの開発者だね！')
    if message.content == 'ぐぅ':
        await message.channel.send('だれそれ？') 
    if message.content == 'なんさい？':
        await message.channel.send('永遠のいちちゃい！')
    if message.content == 'みどり':
        await message.channel.send('プラグイン得意な人だ！')
    if message.content == 'ゆき':
        await message.channel.send('かわいいのじゃぁ～')
    if message.content == 'くうた':
        await message.channel.send('たべられちゃう！')
    if message.content == 'しろいひと':
       await message.channel.send('ふみつぶされちゃう！')      
    if message.content == 'らっだぁ':
        await message.channel.send('✗この発言は禁止されています')
    if message.content == 'れもん':
        await message.channel.send('おいしい！')
    if message.content == 'おい':
        await message.channel.send('こわいよぉ...')  
    if message.content == 'しね':
        await message.channel.send('ぴえん') 
    if message.content == 'h?invite':
        await message.channel.send('招待コードはこちら！ \n> https://discordapp.com/api/oauth2/authorize?client_id=680729935836479506&permissions=8&scope=bot')  

    try:
            print(1 / 0)
    except : KeyError



#pong command
    if message.content == 'h?pong':
        if message.author.guild_permissions.administrator:
            await message.channel.send('pong!')
        else:
            await message.channel.send('> あなたはこのコマンドを実行する権限がありません！')



client.run(token)
