from pytube import YouTube
from pytube import Playlist
import os


SAVE_PATH = "E:\Hunting\Download\daudio"  # to_do


# link of the video to be downloaded
links = str(input('Enter Playlist URL: ')).strip()

playlist = Playlist(links)

PlayListLinks = playlist.video_urls
N = len(PlayListLinks)
# print('Number of videos in playlist: %s' % len(PlayListLinks))

print(f"There are {N} videos in this playlist.\nLets Download all {N} videos")
# print(f"\n Lets Download all {N} videos")

for i, link in enumerate(PlayListLinks):

    yt = YouTube(link)
    video = yt.streams.filter(only_audio=True).first()
    downloaded_file = video.download(SAVE_PATH)
    base, ext = os.path.splitext(downloaded_file)
    new_file = base + '.mp3'
    os.rename(downloaded_file, new_file)
    print(i+1, ' Audio >>{ ' + yt.title + ' } is Downloaded.')

# filter(progressive=True, file_extension='mp3', only_audio=True).order_by('resolution').desc().first()
# SAVE_PATH



print("Done")
