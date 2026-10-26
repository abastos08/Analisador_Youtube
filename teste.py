from pytubefix import YouTube
video = input("Enter the YouTube video URL: ")
yt = YouTube(video.strip())
print(yt.title)
