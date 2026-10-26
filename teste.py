from pytubefix import YouTube
yt = input("Enter the YouTube video URL: ")
yt = YouTube(yt)
print(yt.title)
