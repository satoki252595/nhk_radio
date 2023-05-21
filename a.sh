ffmpeg -i {url} -c copy -bsf:a aac_adtstoasc {output}

ffmpeg -y -vn -v verbose -http_seekable 0 -i "https://vod-stream.nhk.jp/radioondemand/r/916/s/stream_916_22cdbc9fcbec9aa16bf99cc6c3be6aef/index.m3u8" -id3v2_version 3 -metadata artist="NHK" -metadata title="{date}" -metadata album="{program_title}" -metadata date="2022" -metadata track="236" -ab 48k -ar 24000 -ac 1 "a.mp3"