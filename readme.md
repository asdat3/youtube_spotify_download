# YouTube Playlist to MP3 Converter

This project allows you to download videos from a YouTube playlist, convert them to MP3, attach the correct thumbnail from the video as the song's icon, and set metadata such as author, album, and other details.
I just had to push something, 2y ago me was embarrassing :/

## Features

- **Playlist Download**: Download all videos from a given YouTube playlist URL.
- **MP3 Conversion**: Convert downloaded videos into high-quality MP3 files.
- **Thumbnail Embedding**: Automatically extract and embed video thumbnails as icons for the MP3 files.
- **Metadata Tagging**: Set metadata like title, artist, album, and genre for each MP3 file based on video details.

---

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/asdat3/youtube_spotify_download.git
   cd your-repo-name
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure FFmpeg is installed and accessible from the command line.
   - On Windows: [Download FFmpeg](https://ffmpeg.org/download.html) and add it to your PATH.
   - On Linux: Install via Homebrew or package manager:
     ```bash
     brew install ffmpeg
     ```
   - On Mac: you should just buy youtube premium

---

## Usage

### Command Line

1. Run the script with a YouTube playlist URL:
   ```bash
   python main.py --playlist-url "<PLAYLIST_URL>" --output-dir "<OUTPUT_DIRECTORY>"
   ```

2. Options:
   - `--playlist-url`: URL of the YouTube playlist.
   - `--output-dir`: Directory where MP3 files will be saved (default: `./output`).

### Example
```bash
python main.py --playlist-url "https://www.youtube.com/playlist?list=PL12345ABC" --output-dir "./music"
```

---

## How It Works

1. **Download Videos**: Videos from the playlist are downloaded using `yt-dlp`.
2. **Convert to MP3**: FFmpeg converts the downloaded videos into MP3 files.
3. **Extract and Embed Thumbnail**: Thumbnails are extracted from the video and embedded into the MP3 as album art.
4. **Set Metadata**: The script sets metadata such as:
   - **Title**: Based on video title.
   - **Artist**: Based on the YouTube channel name.
   - **Album**: User-defined or based on the playlist name.

---

## Future Enhancements (will never happen)

- Add support for individual video URLs.
- Include error handling for unavailable videos.
- Allow users to customize metadata fields interactively.
- Add a GUI for non-technical users.

---

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request.

---

## Acknowledgments

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) for robust video downloading.
- [FFmpeg](https://ffmpeg.org/) for video/audio processing.

---

## Disclaimer

This tool is intended for educational purposes only. Please ensure that you comply with YouTube's Terms of Service and copyright laws when using this project.
