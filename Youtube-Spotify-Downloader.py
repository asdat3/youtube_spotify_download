from fileinput import filename
from importlib.metadata import files
import os
from pytube import YouTube
from pytube import Playlist
import moviepy.editor as mp
from moviepy.editor import AudioFileClip, ImageClip
from progress.bar import Bar


#------------------------------
# Youtube-Audio(Playlist)
#------------------------------

def download(playlist_url,folder_input):
    playlist = Playlist(playlist_url)

    #prints each video url, which is the same as iterating through playlist.video_urls AND prints address of each YouTube object in the playlist
    print('vids found: ' + str(len(playlist)))

    for old_temp_file_now in os.listdir('temp/temp'):
        os.remove('temp/temp/' + str(old_temp_file_now))

    bar = Bar('Total', max=len(playlist))
    for vid_url in playlist:
        bar.next()
        YouTube(vid_url).streams.get_highest_resolution().download('temp/temp')

        filename_temp = os.listdir('temp/temp')[0].replace('.mp4','').replace('.mp3','')
        mp4_path = 'temp/temp/' + os.listdir('temp/temp')[0]
        os.replace(mp4_path,f'{folder_input}/{filename_temp}.mp4')
    bar.finish()

download('https://www.youtube.com/playlist?list=PLh392u5h6rd1s1d-nPgNn_aersQWbAfR5','vids')