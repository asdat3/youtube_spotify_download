"""
YouTube Playlist Audio Downloader
Downloads audio from YouTube playlists and adds metadata including thumbnails.
"""

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import eyed3
import requests
from pytube import Playlist, YouTube
import moviepy.editor as mp
from randimage import get_random_image
import matplotlib.pyplot as plt

@dataclass
class AudioMetadata:
    """Stores metadata for audio files"""
    title: str
    artist: str = "NQ"
    album: str = "NQ"
    thumbnail_path: Optional[Path] = None

class PlaylistDownloader:
    """Handles downloading and processing of YouTube playlist audio"""
    
    def __init__(self, output_dir: str):
        self.output_dir = Path(output_dir)
        self.temp_dir = Path("temp/temp")
        self.pics_dir = Path("temp/pics")
        self._setup_directories()

    def _setup_directories(self) -> None:
        """Creates necessary directories if they don't exist"""
        for directory in [self.output_dir, self.temp_dir, self.pics_dir]:
            directory.mkdir(parents=True, exist_ok=True)

    def _clean_temp_directory(self) -> None:
        """Removes all files from temporary directory"""
        for file in self.temp_dir.glob("*"):
            file.unlink()

    def download_playlist(self, playlist_url: str) -> None:
        """Downloads all audio from a YouTube playlist"""
        playlist = Playlist(playlist_url)
        print(f'Found {len(playlist)} songs in playlist')

        self._clean_temp_directory()

        for video_url in playlist:
            try:
                self._process_video(video_url)
            except Exception as e:
                print(f"Error processing {video_url}: {str(e)}")

    def _process_video(self, video_url: str) -> None:
        """Processes a single video: downloads, converts, and adds metadata"""
        # Download audio
        yt = YouTube(video_url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        temp_file = audio_stream.download(output_path=self.temp_dir)
        
        # Convert to MP3
        mp3_path = self._convert_to_mp3(temp_file)
        
        # Add metadata
        metadata = AudioMetadata(
            title=Path(temp_file).stem,
            thumbnail_path=self._download_thumbnail(yt)
        )
        self._add_metadata(mp3_path, metadata)
        
        # Move to final destination
        final_path = self.output_dir / f"{metadata.title}.mp3"
        Path(mp3_path).rename(final_path)

    def _convert_to_mp3(self, input_file: str) -> str:
        """Converts audio file to MP3 format"""
        mp3_path = str(Path(input_file).with_suffix('.mp3'))
        audio = mp.AudioFileClip(input_file)
        audio.write_audiofile(mp3_path)
        audio.close()
        Path(input_file).unlink()  # Remove original file
        return mp3_path

    def _download_thumbnail(self, yt: YouTube) -> Path:
        """Downloads or generates thumbnail for the audio"""
        thumbnail_path = self.pics_dir / "temp_thumbnail.png"
        
        try:
            response = requests.get(yt.thumbnail_url, stream=True)
            if response.status_code == 200:
                with open(thumbnail_path, 'wb') as f:
                    f.write(response.content)
                return thumbnail_path
        except Exception as e:
            print(f"Failed to download thumbnail: {str(e)}")

        # Generate random thumbnail as fallback
        self._generate_random_thumbnail(thumbnail_path)
        return thumbnail_path

    def _generate_random_thumbnail(self, path: Path) -> None:
        """Generates a random thumbnail image"""
        img = get_random_image((480, 480))
        plt.imsave(path, img)

    def _add_metadata(self, file_path: str, metadata: AudioMetadata) -> None:
        """Adds metadata to the audio file"""
        audiofile = eyed3.load(file_path)
        
        if audiofile.tag is None:
            audiofile.initTag()

        audiofile.tag.title = metadata.title
        audiofile.tag.album = metadata.album
        audiofile.tag.artist = metadata.artist

        if metadata.thumbnail_path and metadata.thumbnail_path.exists():
            with open(metadata.thumbnail_path, 'rb') as f:
                audiofile.tag.images.set(3, f.read(), 'image/png')

        audiofile.tag.save(version=eyed3.id3.ID3_V2_3)

def main():
    """Main entry point of the script"""
    PLAYLIST_URL = 'https://www.youtube.com/playlist?list=PLh392u5h6rd23Yjzgpksz6bAZKiA5vA1R'
    OUTPUT_DIR = 'test2'

    try:
        downloader = PlaylistDownloader(OUTPUT_DIR)
        downloader.download_playlist(PLAYLIST_URL)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()