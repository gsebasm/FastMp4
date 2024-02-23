import flet as ft
import os
from pytube import YouTube
import moviepy.editor as mp
import tkinter as tk
from tkinter import filedialog

def main(page):
    page.title = "FastMP3"
    page.window_width = 300       # Ancho de la ventana es 200 px
    page.window_height = 600      # Altura de la ventana es 200 px
    page.window_resizable = False # La ventana no es redimensionable
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
   

    c1= ft.Container(
        content=ft.Text("FastMP3"),
        alignment=ft.alignment.center,
        bgcolor=ft.colors.AMBER,
        margin=10,
        padding=10,
        border_radius=10,
        width=150,
        
    ) 
    t = ft.Text()
    h = ft.Text()
    tb1 = ft.TextField(
        border_radius=10,
        width=500,
        label="Youtube Link")

    def button_clicked(e):
        video_url = tb1.value
        try:
            yt = YouTube(video_url)
            title = yt.title
            duration = yt.length
            t.value = f"Título del video: '{title}' \nDuracion del video: '{duration}'"
            h.value = f"Tu audio a sido descargado!"
            #Aqui se descarga el audio 
            audio_stream = yt.streams.filter(only_audio=True, abr="128kbps").first()
            #Aqui seleccionas la carpeta
            download_path = filedialog.askdirectory(title="Seleccionar carpeta de destino")
            audio_stream.download(download_path)
        except Exception as ex:
            t.value = f"Error al obtener el título del video: Por favor vuelve a intentarlo"

        page.update()

    
    b = ft.ElevatedButton(text="Descargar", on_click=button_clicked,)    

   
    page.add(c1, tb1, b, t, h)

ft.app(target=main)