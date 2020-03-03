import re
import textwrap
import discord
import asyncio
import random
from discord.ext import commands
import os

token = os.environ['DISCORD_BOT_TOKEN']

client = commands.Bot(command_prefix="h?",help_command=None)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='h?help | v2.0.2'))

    # or, for watching:
    activity = discord.Activity(name='h?help | v2.0.2', type=discord.ActivityType.playing)
    await client.change_presence(activity=activity)

    channel = client.get_channel(680727914614095903)
    await channel.send('>>> **Hotdog bot** a ready!')

@client.event
async def on_message(message): 


    # Bot自身が送ったメッセージの場合は処理しない
    if message.author.bot:
            return
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
    if message.content == 'h?hp':
        await message.channel.send('ホームページはこちら！ \n> https://hotdog.theblog.me')
    if message.content == 'h?sd':
        await message.channel.send('サポートサーバーはこちら！ \n> https://discord.gg/STybFbM') 
    if message.content == 'ほっとどっくたべる？':
        await message.channel.send('ともぐいはしないよ！')
    if message.content == 'おかね':
        await message.channel.send('もぐもぐ...') 
    try:
            print(1 / 0)
    except : KeyError



#pong command
    if message.content == 'h?pong':
        if message.author.guild_permissions.administrator:
            await message.channel.send('pong!')
        else:
            await message.channel.send('> あなたはこのコマンドを実行する権限がありません！')
    await client.process_commands(message)

#help
@client.command()
@commands.has_permissions()
async def help(ctx):
        embed=discord.Embed(title="**__Hotdog Bot__** **HelpMenu**", color=0xff8000)
        embed.add_field(name="↓権限指定なしコマンド↓", value="None", inline=False)
        embed.add_field(name="h?help", value="ヘルプメニューを表示します", inline=False)
        embed.add_field(name="h?invite", value="招待を表示します", inline=False)
        embed.add_field(name="h?hp", value="ホームページを表示します", inline=False)
        embed.add_field(name="h?sd", value="サポートディスコードサーバーを表示します", inline=False)
        embed.add_field(name="色々挨拶してみてね！", value="None", inline=False)
        embed.add_field(name="↓管理者権限のみ使用可能コマンド↓", value="None", inline=True)
        embed.add_field(name="h.ping", value="pong!", inline=False)
        embed.add_field(name="h.kick <ID or mention> <reason>", value="対象者をkickします", inline=False)
        embed.add_field(name="h.ban <ID or mention> <reason>", value="対象者をbanします", inline=False)
        embed.add_field(name="h.unban <○○○#○○○○>", value="対象者のbanを解除します", inline=False)
        embed.add_field(name="None", value="v2.0.0", inline=True)
        await ctx.send(embed=embed)
#kick  
@client.command()
@commands.has_permissions()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention}をKickしました。')
#ban
@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention}をBanしました。')
#unban
@client.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')[0], member.split('#')[1]

    for ban_entry in banned_users:
        user = ban_entry.user
        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'{user.name}#{user.discriminator}のBanを解除しました。')
            return



client.run(token)
