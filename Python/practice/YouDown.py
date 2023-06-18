from pytube import YouTube
from sys import argv

rutaVideos ="D:\Fotos\Videos descargados de youtube por python"
rutaMusica = "D:\Fotos\Videos descargados de youtube por python\Musica_trans"

video_A_Descargar = "https://www.youtube.com/watch?v=f1S2IvD6nRs"

link = argv[0]

yt = YouTube(video_A_Descargar)

print("Title " , yt.title)

print("Views:" , yt.views)

yd = yt.streams.get_highest_resolution()



yd.download(rutaVideos)

# re.match("^[a-zA-ZáéíóúñÁÉÍÓÚÑ,]+$", yt.title)

# os.rename(yt.title, "Lo hice te deje - Daniel Me Estas Matando")

# sound = yt.streams.filter(only_audio=True).first()

# sound.download( rutaMusica )

# base, ext = os.path.splitext(sound)
# new_file = base + ".mp3"
# os.rename(sound,new_file)

# video = VideoFileClip(rutaVideos + "\\" + yt.title + ".mp4")
# audio = video.audio
# audio.write_audiofile(rutaMusica + "\\" + yt.title + ".mp3")
# video.close()
# audio.close()

# video = askopenfile()
# video = moviepy.editor.VideoFileClip(video)
# audio = video.audio

# audio.write_audiofile(rutaMusica + "\\" + yt.title + ".mp3")

# print("ya Estuvo dijo la teibolera")