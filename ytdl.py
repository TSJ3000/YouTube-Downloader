from pytube import YouTube


url = input("Enter video URL: ")
my_video = YouTube(url)

print("Video Title")
print("my_video.title")

print("Video Thumbnail")
print("my_video.thumbnail_url")

print("Downloading video please wait...")
my_video = my_video.streams.get_highest_resolution()

#or  my_video.streams.first()

my_video.download()
print("Download Complete!")