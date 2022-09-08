from fileinput import filename
from importlib.metadata import files
import random, os, re, requests, matplotlib
from timeit import repeat
from unicodedata import name
from pytube import YouTube
from pytube import Playlist
import moviepy.editor as mp
from moviepy.editor import AudioFileClip, ImageClip
from typer import Typer

#song information
import eyed3.id3
from eyed3.id3 import Tag
from eyed3.id3.frames import ImageFrame

#thumbnail
import pafy
from randimage import get_random_image, show_array


#------------------------------
# Youtube-Audio(Playlist)
#------------------------------

def download(playlist_url,folder_input):
    folder_bla = folder_input

    playlist = Playlist(playlist_url)

    #prints each video url, which is the same as iterating through playlist.video_urls AND prints address of each YouTube object in the playlist
    print('songs found: ' + str(len(playlist)))

    for old_temp_file_now in os.listdir('temp/temp'):
        os.remove('temp/temp/' + str(old_temp_file_now))

    for vid_url in playlist:
        YouTube(vid_url).streams.filter(only_audio=True).first().download('temp/temp')

        filename_temp = os.listdir('temp/temp')[0].replace('.mp4','').replace('.mp3','')
        mp4_path = 'temp/temp/' + os.listdir('temp/temp')[0]
        mp3_path = 'temp/temp/' + os.listdir('temp/temp')[0].replace('mp4','mp3')
        new_file = mp.AudioFileClip(mp4_path)
        new_file.write_audiofile(mp3_path)
        os.remove(mp4_path)
        
        rename('temp/temp',filename_temp+'.mp3',vid_url,filename_temp)

        os.replace(mp3_path,f'{folder_input}/{filename_temp}.mp3')

def rename(folder_bla,song_file_parsed,url_parsed,filename_temp):
    file = folder_bla + "/" + song_file_parsed
    audiofile = eyed3.load(file)
                
    if (audiofile.tag == None):
        audiofile.initTag()

    audiofile.tag.title = str(filename_temp)
    audiofile.tag.album = u"NQ"
    audiofile.tag.artist = u'NQ'

    img_size = (480,480)
    img = get_random_image(img_size)
    matplotlib.image.imsave("temp/pics/temp_thumbnail.png", img)
    
    audiofile.tag.images.set(3, open("temp/pics/temp_thumbnail.png", 'rb').read(), 'image/png')
    audiofile.tag.save(version=eyed3.id3.ID3_V2_3)
    

def get_thumbnail(url_parsed):
    video_thumb = pafy.new(url_parsed).getbestthumb()
    return(str(video_thumb))

playlist_url = 'https://www.youtube.com/playlist?list=PL9z83dt87nBUHM51eDF42TFJjjP9zshpJ'
download(playlist_url,'test2')