import flet as ft
import os
from pytube import YouTube
import moviepy.editor as mp
import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment

# Proporciona la URL del video de YouTube
video_url = 'https://www.youtube.com/watch?v=8mYaXZux9-Y&list=PL6rBgWg-kgDejE04y_J8ygAwMGmte4lkc&index=7'
yt = YouTube(video_url)

# Obtiene información sobre el video
print(f'Título: {yt.title}')
print(f'Duración: {yt.length} segundos')

# Obtiene la corriente de audio en formato MP4 (si está disponible)
stream = yt.streams.get_highest_resolution()

# Descarga el audio en formato MP4
download_path = filedialog.askdirectory(title="Seleccionar carpeta de destino")
#audio_path = os.path.join(download_path, f'{yt.title}.mp4')
stream.download(download_path)

relative_path = selected_file = filedialog.askopenfilename(title="Seleccionar archivo")
name = os.path.abspath(relative_path)

# Cargamos el fichero .mp4
clip = mp.VideoFileClip(name)

# Construir la ruta completa para el archivo MP3
mp3_filename = os.path.join(download_path, os.path.splitext(os.path.basename(name))[0] + ".mp3")

# Lo escribimos como audio y `.mp3`
clip.audio.write_audiofile(mp3_filename)
