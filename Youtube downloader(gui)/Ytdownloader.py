import PySimpleGUI as sg
import youtube_dl
import os

sg.theme('DarkAmber')

layout = [  [sg.Text('U sljedecem redu upisi URL ')],
            [sg.Text('Video URL: '), sg.InputText()],
            [sg.Button('Download'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('YT Video downloader', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    url = values[0]
    link = url.strip()
    os.system("start cmd /k python downloader.py " + link)

    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break

window.close()
