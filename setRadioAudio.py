import requests
import subprocess
import os
# ダウンロード対象リスト読み込み
with open('nhk_downloader.txt') as f:
    urls = f.readlines()
for url in urls:
    url = url.strip()
    if url == '':
        continue
    resp = requests.get(url)
    js = resp.json()
    # フォルダの作成
    program_title = js['main']['program_name']
    if not os.path.exists(program_title):
        os.makedirs(program_title)
    # 音声ファイルダウンロード
    for d1 in js['main']['detail_list']:
        for d2 in d1['file_list']:
            title = d2['file_title']
            date = d2['onair_date']
            file = d2['file_name']
            print(program_title,title,file,date)
            if not os.path.exists(f'{program_title}\{title}.mp3'):
                cmd = f'ffmpeg -y -vn -v verbose -http_seekable 0 -i "{file}" -id3v2_version 3 -metadata artist="NHK" -metadata title="{date}" -metadata album="{program_title}" -metadata date="2022" -metadata track="236" -ab 48k -ar 24000 -ac 1 "{program_title}\{title}.mp3"'
                result = subprocess.run(cmd)
                print(f'{title}', 'ダウンロード', result.returncode, result.stdout)
            else:
                print(f'{title}', 'キャンセル')
