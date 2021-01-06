# Libraries
import youtube_dl
import os
import sys
import win32.lib.win32con as win32con
import win32gui, win32con

# var
url = ""

ydl_opts = {
    'writesubtitles': True,
    'subtitle': '--all-subs',
    }

# funckcija koja uzima ydl_opts kao parametre
def dwl_vid():
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

url = sys.argv[1] # uzima sys argument dobijen sa CMD-a

link = url.strip() #skida '' sa link za dalje koristenje

dwl_vid() #skida video sa prije dobijenog linka

# kod sa skrivanje
the_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)
