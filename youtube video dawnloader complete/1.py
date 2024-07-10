# ..........for single video dawnload...............
# from pytube import YouTube
# link = "https://youtu.be/kmI8KgWP274"
# A = YouTube(link)
# # print(A.title)
# # print(A.thumbnail_url)
# B = A.streams.filter(only_audio=True)
# # B = A.streams.all()
# vid = list(enumerate(B))
# for i in vid:
#     print(i)
# strm = int(input("Enter No: "))
# B[strm].download()
# print("Successfully") 


# ..........for playlist video dawnload...............
# from pytube import Playlist
# py = Playlist("https://youtube.com/playlist?list=PLGE6DezqSJKLhSp5RkZGZJkUpZE_6YHcO")

# print(f"Downloading : {py.title}")
# for video in py.videos:
#     video.streams.first().download()