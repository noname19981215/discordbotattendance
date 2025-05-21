import gspread
import datetime
import discord
import re
from time import sleep
# ServiceAccountCredentials：Googleの各サービスへアクセスできるservice変数を生成します。
from oauth2client.service_account import ServiceAccountCredentials

# 2つのAPIを記述しないとリフレッシュトークンを3600秒毎に発行し続けなければならない
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

# 認証情報設定
# ダウンロードしたjsonファイル名をクレデンシャル変数に設定（秘密鍵、Pythonファイルから読み込みしやすい位置に置く）
credentials = ServiceAccountCredentials.from_json_keyfile_name('jsonファイル名.json', scope)

# OAuth2の資格情報を使用してGoogle APIにログインします。
gc = gspread.authorize(credentials)
workbook = gc.open_by_key('1UvHSJi418D9ulJwzSm7M78f5EBm4UgeuZ-2SxzH5XZE')
worksheet_list = workbook.worksheets()
wks = workbook.worksheet("メンバー＆出欠表　スプレッドシートのシート名")
TOKEN = "トークンＩＤ"
client = discord.Client()



@client.event
async def on_ready():
    while True:
        date = datetime.date.today()
        timedate = datetime.datetime.now()
        now = timedate.strftime('%H:%M')
        print(now)
        print(date.weekday())
        if now == '00:00':
            CHANNEL_ID =435059680360923140
            channel = client.get_channel(CHANNEL_ID)
            await channel.send('お疲れ様です')
        if date.weekday() == 6:
            if now == '13:00':
                CHANNEL_ID =435059680360923140
                channel = client.get_channel(CHANNEL_ID)
                await channel.send('１３時のアナウンス')
        if date.weekday() == 5:
            if now == '17:40':
                CHANNEL_ID =435059680360923140
                channel = client.get_channel(CHANNEL_ID)
                await channel.send('退勤２０分前のアナウンス')

        if date.weekday() == 6:
            if now == '23:00':
                secondweekfriday = datetime.date.today() + datetime.timedelta(days=6)
                secondweekfriday=secondweekfriday.strftime("%m/%d")

                print(secondweekfriday)
                secondweeksunday = datetime.date.today() + datetime.timedelta(days=7)
                secondweeksunday=secondweeksunday.strftime("%m/%d")

                print(secondweeksunday)

                wks.update_acell('G3', secondweekfriday)
                wks.update_acell('H3', secondweeksunday)

                cell_list = wks.range('g4:h55')
                for cell in cell_list:
                    cell.value = ''
                    wks.update_cells(cell_list)
                    channel = client.get_channel(435059680360923140)
                await channel.send("スプレッドシートを更新、今週の記入をお願いします")
                sleep(50)
        if date.weekday() == 5:
            if now == '12:00':
               col_set = wks.col_values(18)
               r = re.compile('^[0-9]+$')
               result2 = [s for s in col_set if r.match(s)]
               result = [int(str) for str in result2]
               server_members_set = [member.id for member in client.get_all_members()]
               src_set = set(result)
               tag_set = set(server_members_set)
               matched_list = list(src_set & tag_set)
               X=matched_list
               for A in X:
                   print(A)
                   channel = client.get_channel(435059680360923140)
                   await channel.send("<@!"+str(A)+">""出席確認プログラム")
               sleep(10)
        sleep(50)
client.run(TOKEN)
