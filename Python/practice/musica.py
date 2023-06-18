import youtube_dl

# Establece la URL del video y la ruta de descarga
video_url = 'https://www.youtube.com/watch?v=ZyDUc1h582U'
download_path = 'D:\Fotos\Videos descargados de youtube por python\Musica_trans'


# Set the download options
options = {
    'format': 'bestaudio/best',
    'outtmpl': f'{download_path}/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

# Download the audio
with youtube_dl.YoutubeDL(options) as ydl:
    info_dict = ydl.extract_info(video_url, download=False)
    ydl.download([video_url])

print(f'Audio from video "{info_dict["title"]}" downloaded in .mp3 format at "{download_path}"')