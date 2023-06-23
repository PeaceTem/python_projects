from pytube import YouTube

myVideo = YouTube('https://m.youtube.com/watch?v=ieeH3ck6mP4')

myVideo.streams.filter(file_extension = 'mp4').get_by_itag(18).first().download()
print("The video has been auccessfully downloaded")