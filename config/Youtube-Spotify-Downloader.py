import random, os, re
from pytube import YouTube
import youtube_dl
from pytube import Playlist
import moviepy.editor as mp 
from typer import Typer

#song information
import eyed3.id3
from eyed3.id3 import Tag
from eyed3.id3.frames import ImageFrame


#------------------------------
# Youtube-Spotify-Downloader
#------------------------------


# def download(url: str, outpath: str = "./"):
#     playlist = Playlist(url)

#     #prints each video url, which is the same as iterating through playlist.video_urls
#     for url in playlist:
#         print(url)
#     #prints address of each YouTube object in the playlist
#     for vid in playlist.videos:
#         print(vid)
#     for url in playlist:
#         YouTube(url).streams.filter(only_audio=True).first().download(outpath)
#     # for url in playlist:
#     #     YouTube(url).streams.first().download("./test")

#     folder = outpath

#     for file in os.listdir(folder):
#         if re.search('mp4', file):
#             mp4_path = os.path.join(folder,file)
#             mp3_path = os.path.join(folder,os.path.splitext(file)[0]+'.mp3')
#             new_file = mp.AudioFileClip(mp4_path)
#             new_file.write_audiofile(mp3_path)
#             os.remove(mp4_path)

# download(
#     "https://www.youtube.com/playlist?list=PL9z83dt87nBUz5T9_ZtH71eVhID6JYSqD",
#     "./Music"
# )



# song = eyed3.load("music/test.mp3", tag_version=None)

# if not song.tag:
#     song.initTag()

# t = Tag()

# t.artist = "Behemoth"
# t.album = "The Satanist"
# t.genre = "Black Metal"
# t.recording_date = 2014
# t.track_num = 4
# t.title = "Ora pro nobis Lucifer"

# with open("music/amadeus.jpg", "rb") as cover_art:
#     song.tag.images.set(3, cover_art.read(), "amadeus.jpg")

# eyed3.log.setLevel("ERROR")


audiofile = eyed3.load('music/test.mp3')
if (audiofile.tag == None):
    audiofile.initTag()

audiofile.tag.title = u'fuck'
audiofile.tag.album = u'fucking'
audiofile.tag.images.set(3, open("music/fuck.jpg", 'rb').read(), 'image/jpeg')
audiofile.tag.save(version=eyed3.id3.ID3_V2_3)

