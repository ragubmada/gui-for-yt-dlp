import os
import tkinter as tk
from tkinter import scrolledtext
from datetime import date

def start_download():
    links = input_box.get("1.0", tk.END).split("\n")
    today = date.today().strftime("%Y-%m-%d")
    download_folder = f"downloaded_music_{today}"
    os.makedirs(download_folder, exist_ok=True)

    for link in links:
        link = link.strip()
        if link:
            os.system(f'yt-dlp.exe --extract-audio --audio-format mp3 "{link}" -o "{download_folder}/%(title)s.%(ext)s"')

def clear_input():
    input_box.delete("1.0", tk.END)

def exit_program():
    window.destroy()

window = tk.Tk()
window.title("YouTube Audio Downloader")

input_label = tk.Label(window, text="Paste YouTube links below (one per line):")
input_label.pack()

input_box = scrolledtext.ScrolledText(window, width=60, height=10)
input_box.pack()

download_button = tk.Button(window, text="Start Download", command=start_download)
download_button.pack()

clear_button = tk.Button(window, text="Clear", command=clear_input)
clear_button.pack()

exit_button = tk.Button(window, text="Exit", command=exit_program)
exit_button.pack()

window.mainloop()
