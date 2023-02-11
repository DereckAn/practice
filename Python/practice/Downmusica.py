from pytube import YouTube
import os 
url = "https://www.youtube.com/watch?v=3xoy3xT3nqE"
video = YouTube(url)
# print("title :" , video.title)
out_path = video.streams.filter(only_audio=True).first().download("D:\Fotos\Videos descargados de youtube por python\Musica_trans")

new_name = os.path.splitext(out_path) #[0] + ".mp3"
os.rename(out_path, new_name[0] + ".mp3")
print("done")

