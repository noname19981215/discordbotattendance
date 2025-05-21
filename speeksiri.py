# インストールした discord.py を読み込む
import discord

# 自分のBotのアクセストークンに置き換えてください
TOKEN = "トークンID"

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')
    channel = client.get_channel(435059680360923140)
    await channel.send('おはよ～')



# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃ～ん')

        # 話しかけた人に返信する
    if client.user in message.mentions: # 話しかけられたかの判定
        reply = f'{message.author.mention} メッセージ１'
        await message.channel.send(reply)

    if message.content == 'メッセージ２宣言符':
        await message.channel.send('メッセージ２'+message.author.name+'メッセージ２')

    if message.content == 'メッセージ３宣言符':
        await message.channel.send('メッセージ３宣言符'+message.author.name)



    if message.content == 'speak':
        await message.channel.send('/neko,メッセージ２宣言符,メッセージ３宣言符')

    if message.content.startswith('権限付与の宣言符'):
        role = discord.utils.get(message.guild.roles, name='member')
        await message.author.add_roles(role)
        reply = f'{message.author.mention} 権限付与'
        await message.channel.send(reply)

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
