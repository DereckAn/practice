from pytube import YouTube
from sys import argv

link = argv[0]

yt = YouTube("https://www.youtube.com/watch?v=yuFI5KSPAt4")

print("Title " , yt.title)

print("Views:" , yt.views)

yd = yt.streams.get_highest_resolution()
yd.download("D:\Fotos\Videos descargados de youtube por python")






