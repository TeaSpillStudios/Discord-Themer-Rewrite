from tkinter import ttk
from ttkthemes import ThemedTk
import tkinter as tk
import os

isUnix = False

if os.name == "posix":
    isUnix = True

def runTheme(themeName):
    if isUnix:
        os.system(f"python3 Theming-scripts\/{themeName}.py")
    else:
        os.system(f"python3 Theming-scripts\\{themeName}.py")

root = ThemedTk()
root.geometry("320x250")
root.title("Discord Theme Rewrite")

style = ttk.Style(root)
root.tk.call("source", "azure dark.tcl")
style.theme_use("azure")

spacer1 = tk.Label(root, text="  ")
spacer2 = tk.Label(root, text="  ")
spacer3 = tk.Label(root, text="  ")
spacer4 = tk.Label(root, text="  ")

title = ttk.Label(root, text="This is a discord themer that doesn't break ToS", style='my.TButton').pack()
spacer1.pack()

material = ttk.Button(root, text="Material", command = lambda: runTheme("material")).pack()
spacer2.pack()
forest = ttk.Button(root, text="Forest", command=lambda: runTheme("forest")).pack()
spacer3.pack()
peachy = ttk.Button(root, text="Night", command=lambda: runTheme("night")).pack()
spacer4.pack()
stormy = ttk.Button(root, text="Stormy", command=lambda: runTheme("stormy")).pack()

root.mainloop()
