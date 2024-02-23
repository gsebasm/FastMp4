import os
from pytube import YouTube
import moviepy.editor as mp
import tkinter as tk
from tkinter import filedialog

# Crear una instancia de Tkinter sin mostrar la ventana principal
root = tk.Tk()
root.withdraw()

# Ruta relativa al archivo .mp4
relative_path = "C:/Users/Ismael/Desktop/FastMp3/pruebaV/One Piece - Opening 21  Super Powers.mp4"

# Obtener la ruta absoluta
name = os.path.abspath(relative_path)

# Cargamos el fichero .mp4
clip = mp.VideoFileClip(name)


# Mostrar el cuadro de diálogo para seleccionar una carpeta
selected_folder = filedialog.askdirectory(title="Seleccionar carpeta de destino")

# Verificar si el usuario ha seleccionado una carpeta
if selected_folder:
    print(f'Carpeta seleccionada: {selected_folder}')
else:
    print('No se seleccionó ninguna carpeta.')

# Si la carpeta no existe, créala
if not os.path.exists(selected_folder):
    os.makedirs(selected_folder)

# Construir la ruta completa para el archivo MP3
mp3_filename = os.path.join(selected_folder, os.path.splitext(os.path.basename(name))[0] + ".mp3")

# Lo escribimos como audio y `.mp3`
clip.audio.write_audiofile(mp3_filename)