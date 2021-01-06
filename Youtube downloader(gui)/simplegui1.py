import PySimpleGUI as sg
import youtube_dl
import os

sg.theme('DarkAmber')

layout = [  [sg.Text('U sljedecem redu upisi ')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('YT Video downloader', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    url = values[0]
    link = url.strip()
    os.system("start cmd /k python main.py " + link)
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()
