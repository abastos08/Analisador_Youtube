from pytubefix import YouTube   

video = input("Enter the YouTube video URL: ")
yt = YouTube(video.strip())
print(f"Title: {yt.title}")

streams = yt.streams.filter(only_audio=True).order_by('abr').desc()
Selected_stream = streams.first()
file_path = Selected_stream.download(output_path="audio")
print(f"Downloaded audio file: {file_path}")
