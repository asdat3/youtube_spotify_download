import random, os, re
from pytube import YouTube
import youtube_dl
from pytube import Playlist
import moviepy.editor as mp 
from typer import Typer


#------------------------------
# Youtube-Spotify-Downloader
#------------------------------

# def download_mp3_videos(url: str, outpath: str = "./"):

#     yt = YouTube(url)
#     get_audio = yt.streams.filter(only_audio=True).get_audio_only().itag
#     # pytube.YouTube("url here").streams.filter(only_audio=True).all()
#     # yt.streams.filter(file_extension="mp4").get_by_resolution().download(outpath)
#     yt.streams.get_by_itag(get_audio).download(outpath)


# if __name__ == "__main__":

#     download_mp3_videos(
#         "https://www.youtube.com/watch?v=CkU9zS1gLgo&list=RDIJbBOANg8CQ&index=6",
#         "./songs",
#     )

# folder = "./test"

# for file in os.listdir(folder):
#   if re.search('mp4', file):
#     mp4_path = os.path.join(folder,file)
#     mp3_path = os.path.join(folder,os.path.splitext(file)[0]+'.mp3')
#     new_file = mp.AudioFileClip(mp4_path)
#     new_file.write_audiofile(mp3_path)
#     os.remove(mp4_path)


def download(url: str, outpath: str = "./"):
    playlist = Playlist(url)

    #prints each video url, which is the same as iterating through playlist.video_urls
    for url in playlist:
        print(url)
    #prints address of each YouTube object in the playlist
    for vid in playlist.videos:
        print(vid)
    for url in playlist:
        YouTube(url).streams.filter(only_audio=True).first().download(outpath)
    # for url in playlist:
    #     YouTube(url).streams.first().download("./test")

    folder = "./test"

    for file in os.listdir(folder):
        if re.search('mp4', file):
            mp4_path = os.path.join(folder,file)
            mp3_path = os.path.join(folder,os.path.splitext(file)[0]+'.mp3')
            new_file = mp.AudioFileClip(mp4_path)
            new_file.write_audiofile(mp3_path)
            os.remove(mp4_path)

download(
    "https://www.youtube.com/playlist?list=PL9z83dt87nBVgjafaXf6WtqazRvPzcAID",
    "./test"
)