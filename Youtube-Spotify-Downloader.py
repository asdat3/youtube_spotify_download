from fileinput import filename
from importlib.metadata import files
import random, os, re, requests
from timeit import repeat
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

#thumbnail
import pafy

#------------------------------
# Youtube-Audio(Playlist)
#------------------------------

def download(playlist_url,folder_input):
    folder_bla = folder_input

    playlist = Playlist(playlist_url)

    #prints each video url, which is the same as iterating through playlist.video_urls AND prints address of each YouTube object in the playlist
    for vid_url in playlist:
        print(vid_url)
    vid_names_list = []
    for vid_name in playlist.videos:
        print(vid_name)
        vid_names_list.append(str(vid_name))

    cunt_counte_tvmp = 0
    for vid_url in playlist:
        YouTube(vid_url).streams.filter(only_audio=True).first().download(folder_bla)

        mp4_path = os.path.join(folder_bla,vid_names_list[cunt_counte_tvmp]+'.mp4')
        mp3_path = os.path.join(folder_bla,vid_names_list[cunt_counte_tvmp]+'.mp3')
        new_file = mp.AudioFileClip(mp4_path)
        new_file.write_audiofile(mp3_path)
        os.remove(mp4_path)

        rename(folder_bla,vid_names_list[cunt_counte_tvmp]+'.mp3',vid_url)

        cunt_counte_tvmp = cunt_counte_tvmp + 1

def rename(folder_bla,song_file_parsed,url_parsed):
    file = folder_bla + "/" + song_file_parsed
    audiofile = eyed3.load(file)
                
    if (audiofile.tag == None):
        audiofile.initTag()

    audiofile.tag.title = u"fuck"
    audiofile.tag.album = u'fucking'
    audiofile.tag.artist = u'NQ'

    thumb_file_res = requests.get(get_thumbnail(url_parsed),allow_redirects=True)
    open('temp/pics/temp_thumbnail.jpg', 'wb').write(thumb_file_res.content)
    
    audiofile.tag.images.set(3, open(f'temp/pics/temp_thumbnail.jpg', 'rb').read(), 'image/jpeg')
    audiofile.tag.save(version=eyed3.id3.ID3_V2_3)

def get_thumbnail(url_parsed):
    video_thumb = pafy.new(url_parsed).getbestthumb()
    return(str(video_thumb))

playlist_url = 'https://www.youtube.com/playlist?list=PL9z83dt87nBVgjafaXf6WtqazRvPzcAID'
download(playlist_url,'test2')