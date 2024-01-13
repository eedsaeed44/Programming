from pytube import YouTube
from pytube import Playlist


SAVE_PATH = "E:\Hunting\Download"  # to_do

pad = 0
# link of the video to be downloaded
links = str(input('Enter Playlist URL: ')).strip()

playlist = Playlist(links)

PlayListLinks = playlist.video_urls
N = len(PlayListLinks)
# print('Number of videos in playlist: %s' % len(PlayListLinks))

print(f"There are {N} videos in this playlist.\nLets Download all {N} videos")
# print(f"\n Lets Download all {N} videos")

for i, link in enumerate(PlayListLinks):
    try:
        yt = YouTube(link)
        d_video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        d_video.download(SAVE_PATH)
        print(i+1, ' Video>>{ '+ yt.title +' } is Downloaded.')
    except:
        print(i+1, ' Video>>{ ' + yt.title + ' } >>>>>>>>>>>>>>>Error<<<<<<<<<<<<<<.')
        pad +=1
print(f"There are {pad} Pad Videos in this url.")