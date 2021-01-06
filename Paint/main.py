import tkinter as tk

tk = tk.Tk()


tk.title("Paint python")
tk.geometry("900x400") #velicina default window
tk.columnconfigure(0, weight=1)
tk.columnconfigure(1, weight=2)


tk.mainloop() #uvjek na zadnjoj liniji
