from __future__ import unicode_literals
import youtube_dl
num_array = list()
data = []

for i in range(0, 16):
    x = raw_input()
    data.append(x)
   

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192',
    }],
}
for link in data:
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
   		 ydl.download(['https://www.youtube.com/watch?v=0GDdLY4nLuA'])

