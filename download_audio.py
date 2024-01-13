# importing packages
from pytube import YouTube
import os

# url input from user
link = 'https://www.youtube.com/watch?v=9FYaN5JyfOk&list=RDMM&start_radio=1&rv=C7r5qDduxxU'
# str(input("Enter URL>> "))
yt = YouTube(link)

# extract only audio
audio = yt.streams.get_audio_only()
# stream = yt.streams.get_highest_resolution()
#  stream.download(PATH)
# check for destination to save file
path = 'E:\Hunting\Download'

# download the file
audio.download(path)

# save the file
# base, ext = os.path.splitext(path)
# new_file = base + '.mp3'
# os.rename(path, new_file)

# result of success
print(yt.title + " has been successfully downloaded.")
