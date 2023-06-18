from pytube import YouTube

# Establece la URL del video y la ruta de descarga
video_url = 'https://www.youtube.com/watch?v=f1S2IvD6nRs'
download_path = 'D:\Fotos\Videos descargados de youtube por python\Musica_trans'

# Crea un objeto YouTube con la URL del video
yt = YouTube(video_url)

# Obtiene el stream de mayor resolución disponible
stream = yt.streams.get_highest_resolution()

# Descarga el video en la ruta especificada
stream.download(download_path)

print(f'Video "{yt.title}" descargado en "{download_path}"')