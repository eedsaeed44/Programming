from pytube import YouTube

URL = str(input("Input URL: "))
PATH = 'E:\Hunting\Download'
yt = YouTube(URL)
print("Video Title: " + yt.title)
stream = yt.streams.get_highest_resolution()

try:
	# downloading the video
	# d_video.download(SAVE_PATH)

    stream.download(PATH)
except:
	print("Some Error!")
print('Task Completed!')
