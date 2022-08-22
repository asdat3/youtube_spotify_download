import random, os
from pytube import YouTube
import youtube_dl

#------------------------------
# Youtube-Spotify-Downloader
#------------------------------

def download_mp3_videos(url: str, outpath: str = "./"):

    yt = YouTube(url)
    get_audio = yt.streams.filter(only_audio=True).get_audio_only().itag
    # pytube.YouTube("url here").streams.filter(only_audio=True).all()
    # yt.streams.filter(file_extension="mp4").get_by_resolution().download(outpath)
    yt.streams.get_by_itag(get_audio).download(outpath)


if __name__ == "__main__":

    download_mp3_videos(
        "https://www.youtube.com/watch?v=SEgu0XZ-JoQ&list=RDIJbBOANg8CQ&index=4",
        "./songs",
    )

