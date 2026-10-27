from pytubefix import YouTube   
from faster_whisper import WhisperModel


video = input("Enter the YouTube video URL: ")
yt = YouTube(video.strip())
print(f"Title: {yt.title}")

streams = yt.streams.filter(only_audio=True).order_by('abr').desc()
Selected_stream = streams.first()
file_path = Selected_stream.download(output_path="audio",filename=f"audio_transcricao.{Selected_stream.subtype}")

print(f"Downloaded audio file: {file_path}")
