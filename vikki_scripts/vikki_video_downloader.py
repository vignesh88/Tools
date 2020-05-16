from pytube import YouTube
import os
# import sys


def downloadyoutube(videourl, path):
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
    video_stream = yt.streams.filter(file_extension='mp4', resolution="1080p").first()
    print('Downloading video file')
    video_stream.download(output_path=path, filename=video_title, filename_prefix="video_")
    audio_stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()
    print('Downloading audio file')
    audio_stream.download(output_path=path, filename=video_title, filename_prefix="audio_")
    audio_file = path + "audio_" + video_title + ".mp4"
    video_file = path + "video_" + video_title + ".mp4"
    merged_file = path + video_title + ".mp4"
    print('Post processing files')
    os.system("ffmpeg -i {} -i {} -codec copy -shortest {}".format(video_file, audio_file, merged_file))


downloadyoutube('https://www.youtube.com/watch?v=88iypMO9H7g', '/home/vikki/Downloads/blog/')
