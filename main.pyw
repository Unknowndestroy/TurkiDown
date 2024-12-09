import tkinter as tk
from tkinter import messagebox
from yt_dlp import YoutubeDL
import os

def download_media():
    url = url_entry.get()
    if not url:
        messagebox.showwarning("Error - Warning - No Input", "Please input a link!")
        return

    try:
        download_path = os.path.expanduser("~/Downloads")  
        options = {
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
            'format': 'bestvideo+bestaudio/best',  
            'merge_output_format': 'mp4',  
            'postprocessors': [
                {'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'},  
                {'key': 'FFmpegVideoConvertor', 'preferedformat': 'mp4'},  
            ],
        }
        

        with YoutubeDL(options) as ydl:
            ydl.download([url])

        messagebox.showinfo("Successful", f"File downloaded successfully to {download_path}")
    
    except Exception as e:
        messagebox.showerror("Error", f"Can't download the file, Error Code: {e}")


root = tk.Tk()
root.title("Social Media Downloader")
root.geometry("400x250")
root.resizable(False, False)


title_label = tk.Label(root, text="TurkiDown", font=("Arial", 18, "bold"))
title_label.pack(pady=10)


url_label = tk.Label(root, text="Link here:", font=("Arial", 12))
url_label.pack(pady=5)

url_entry = tk.Entry(root, width=40, font=("Arial", 12))
url_entry.pack(pady=5)


download_button = tk.Button(root, text="Download", font=("Arial", 14), command=download_media)
download_button.pack(pady=10)


platform_label = tk.Label(root, text="Remove the barriers, feel the bass!", font=("Arial", 10, "italic"), fg="gray")
platform_label.pack(side=tk.BOTTOM, pady=10)


root.mainloop()
