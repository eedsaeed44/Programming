from pytube import YouTube
F_name = 'videos_links.txt'
F_hand = open(F_name)
i = 1
for line in F_hand:
	URL = line
	PATH = 'E:\Hunting\Download'
	yt = YouTube(URL)
	
	stream = yt.streams.get_highest_resolution()
	
	try:
		# downloading the video
		# d_video.download(SAVE_PATH)

		stream.download(PATH)
		print(f"=> {i} Video [ {  yt.title } ] is Downloaded.")
		i+=1
	except:
		print("Some Error!")
	# print('===Downloaded===')
print('All Done')
