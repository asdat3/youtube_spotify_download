from fileinput import filename
import random, os, re, glob
from unicodedata import name
from pytube import YouTube
import youtube_dl
from pytube import Playlist
import moviepy.editor as mp 
from typer import Typer

#song information
import eyed3.id3
from eyed3.id3 import Tag
from eyed3.id3.frames import ImageFrame
from PIL import Image



#------------------------------
# Youtube-Spotify-Downloader
#------------------------------


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
   
    global folder 
    folder = outpath
   
    for file in os.listdir(folder):
        if re.search('mp4', file):
            mp4_path = os.path.join(folder,file)
            mp3_path = os.path.join(folder,os.path.splitext(file)[0]+'.mp3')
            new_file = mp.AudioFileClip(mp4_path)
            new_file.write_audiofile(mp3_path)
            os.remove(mp4_path)

        # if re.search('mp3', file):
        #     os.rename()

download(
    "https://www.youtube.com/playlist?list=PL9z83dt87nBUz5T9_ZtH71eVhID6JYSqD",
    "./test"
)

# for file in os.listdir("test"):
#     # if glob.glob("./*.mp3"):
# global audiofile
# audiofile = eyed3.load("test/te.mp3")

# for file in os.listdir(folder):
# os.chdir(folder)
for file in os.listdir(folder):
    audiofile = eyed3.load("test/Mansionz ft Spark Master Tape - STFU (Massive Vibes Remix).mp3")
                
    if (audiofile.tag == None):
        audiofile.initTag()

    audiofile.tag.title = u'fuck'
    audiofile.tag.album = u'fucking'
    audiofile.tag.images.set(3, open("pics/song.jpg", 'rb').read(), 'image/jpeg')
    audiofile.tag.save(version=eyed3.id3.ID3_V2_3)



