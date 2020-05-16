from pytube import YouTube
import os
import sys
from progress.bar import Bar
import threading
import tkinter as tk
from tkinter import ttk
import io



# main application shows:
# label Loading..
# label which configure values when file is downloading
# inderterminate progress bar
class MainApplication(tk.Frame):
    def __init__(self, master=None, *args, **kwargs):
        tk.Frame.__init__(self, master)
        self.master = master

        self.master.grid_rowconfigure(0, weight=0)
        self.master.grid_columnconfigure(0, weight=1)

        self.youtubeEntry = "https://www.youtube.com/watch?v=3-Xq_Zz3nPA"
        self.FolderLoacation = "/home/vikki/Downloads/blog/"

        # pytube
        self.yt = YouTube(self.youtubeEntry)
        yt_title = self.yt.title
        yt_title = yt_title.replace(' ', '-')
        yt_title = yt_title.replace('|', '_')
        yt_title = yt_title.replace(',', '_')
        yt_title = yt_title.replace('.', '_')
        yt_title = yt_title.replace('(', '-')
        self.yt_title = yt_title.replace(')', '-')

        #video_type = self.yt.streams.filter(only_audio = True).first()

        # file size of a file
        #self.MaxfileSize = video_type.filesize

        # Loading label
        #self.loadingLabel = ttk.Label(self.master, text="Downloading...", font=("Agency FB", 30))
        #self.loadingLabel.grid(pady=(100,0))

        # loading precent label which must show % downloaded
        self.loadingPercent = tk.Label(self.master, text="0", fg="green", font=("Agency FB", 30))
        self.loadingPercent.grid(pady=(30,30))

        # indeterminate progress bar
        self.progressbar = ttk.Progressbar(self.master, orient="horizontal", length=500, mode='indeterminate')
        self.progressbar.grid(pady=(50,0))
        self.progressbar.start()

        threading.Thread(target=self.yt.register_on_progress_callback(self.show_progress_bar)).start()

        # call Download file func
        threading.Thread(target=self.DownloadFile).start()

    def DownloadFile(self):
        file_type = self.yt.streams.filter(file_extension='mp4', resolution="1080p").first()
        self.MaxfileSize = file_type.filesize
        self.loadingLabel = ttk.Label(self.master, text="Downloading Video...", font=("Agency FB", 30))
        self.loadingLabel.grid(pady=(100, 0))
        self.yt.streams.filter(file_extension='mp4', resolution="1080p").first().download(output_path=self.FolderLoacation, filename=self.yt_title, filename_prefix="video_")

        file_type = self.yt.streams.filter(only_audio=True, file_extension='mp4').first()
        self.MaxfileSize = file_type.filesize
        self.loadingLabel = ttk.Label(self.master, text="Downloading Audio...", font=("Agency FB", 30))
        self.loadingLabel.grid(pady=(100, 0))
        self.yt.streams.filter(only_audio=True, file_extension='mp4').first().download(output_path=self.FolderLoacation, filename=self.yt_title, filename_prefix="audio_")


    def show_progress_bar(self, stream=None, chunk=None, file_handle=None, bytes_remaining=None):
        self.loadingPercent.config(text=str(int(100 - (100 * (bytes_remaining / self.MaxfileSize)))))
        #text = io.TextIOWrapper(file_handle)
        #print(bytes_remaining)
        file_name = str(file_handle)
        file_name = file_name.split(self.FolderLoacation)
        file_name = file_name[1]
        file_name = file_name.split('_')
        file_name = file_name[0]
        #print(file_name)

        #print(file_handle.read(20))
        #text = str(text)
        #print(text)
        #print(file_handle)
'''
        if 'video' in file_name:
            self.loadingLabel = ttk.Label(self.master, text="Downloading Video...", font=("Agency FB", 30))
            
        else:
            self.loadingLabel = ttk.Label(self.master, text="Downloading Audio...", font=("Agency FB", 30))
'''


        # loadingPercent label configure value %


root = tk.Tk()
root.title("Vikki Youtube downloader")
root.geometry("800x450")
app = MainApplication(root)
root.mainloop()
'''

global path

def downloadyoutube(videourl, path):
    global size
    global yt

    yt = YouTube(videourl)
    video_title = yt.title
    video_title = video_title.replace(' ', '-')
    video_title = video_title.replace('|', '_')
    video_title = video_title.replace(',', '_')
    video_title = video_title.replace('.', '_')
    video_title = video_title.replace('(', '-')
    video_title = video_title.replace(')', '-')
#    for elem in yt.streams.all():
#        print(elem)
    #video_stream = yt.streams.filter(file_extension='mp4', resolution="1080p").first()
    #print('Downloading video file')
    #size = video_stream.filesize
    #video_stream.download(output_path=path, filename=video_title, filename_prefix="video_")
    #audio_stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()
    #print('Downloading audio file')
    #size = audio_stream.filesize
    #audio_stream.download(output_path=path, filename=video_title, filename_prefix="audio_")
    #audio_file = path + "audio_" + video_title + ".mp4"
    #video_file = path + "video_" + video_title + ".mp4"
    #merged_file = path + video_title + ".mp4"
    #print('Post processing video and audio files')
    #os.system("ffmpeg -i {} -i {} -codec copy -shortest {}".format(video_file, audio_file, merged_file))
    #print('Cleaning up files')
    #os.remove(video_file)
    #os.remove(audio_file)

    threading.Thread(target=yt.register_on_progress_callback(show_progress_bar)).start()
    threading.Thread(target=DownloadFile(path, video_title)).start()


def DownloadFile(path, video_title):

    yt.streams.filter(only_audio=True, file_extension='mp4').first().download(output_path=path, filename=video_title, filename_prefix="audio_")
    #audio_stream.download(output_path=path, filename=video_title, filename_prefix="audio_")


def show_progress_bar(stream, chunk , file_handle, bytes_remaining):
    size = yt.streams.filter(only_audio=True, file_extension='mp4').first()
    size = size.filesize
    percent = int((100 * (size - bytes_remaining)) / size)
    bar = Bar('Downloading', max=100, suffix='%(index)d/%(max)d - %(percent).1f%% - %(eta)ds')
    if percent < 100:
        bar.next(percent)
    bar.finish()


downloadyoutube('https://www.youtube.com/watch?v=3-Xq_Zz3nPA', '/home/vikki/Downloads/blog/')
'''
