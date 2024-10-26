from yt_dlp import YoutubeDL
import os
from pathlib import Path
import re


def sanitize_filename(title):
    """Remove invalid characters from filename"""
    return re.sub(r'[<>:"/\\|?*]', '', title)


def download_playlist(url, output_path=None):
    """
    Download a YouTube playlist or single video in highest quality audio

    Args:
        url (str): YouTube playlist or video URL
        output_path (str, optional): Directory to save the audio files
    """
    try:
        # Set default output path if none provided
        if output_path is None:
            output_path = str(Path.home() / "Music" / "YouTube Music")

        # Create output directory if it doesn't exist
        os.makedirs(output_path, exist_ok=True)

        # Configure yt-dlp options for highest quality
        ydl_opts = {
            # Get the best audio quality available
            'format': 'bestaudio/best',
            'paths': {'home': output_path},

            # Post-processing options for high quality
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',  # Highest MP3 quality
            }],

            # Playlist options
            'ignoreerrors': True,  # Skip unavailable videos
            'cookiesfrombrowser': None,  # Add this if you need to download private playlists

            # Output template for organized files
            'outtmpl': '%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s',

            # Download progress hooks
            'progress_hooks': [lambda d: print_progress(d)],

            # Additional options for better downloads
            'nocheckcertificate': True,
            'playlist': True,
            'concurrent_fragments': 3  # Download faster with multiple connections
        }

        # Initialize YouTube-DL
        print(f"\nInitializing download from: {url}")
        print(f"Files will be saved to: {output_path}")
        print("\nStarting download (this might take a while for playlists)...\n")

        with YoutubeDL(ydl_opts) as ydl:
            # Get playlist/video info first
            info = ydl.extract_info(url, download=False)

            if 'entries' in info:
                # It's a playlist
                playlist_title = sanitize_filename(info.get('title', 'Playlist'))
                print(f"Playlist: {playlist_title}")
                print(f"Total videos found: {len(info['entries'])}")

                # Download playlist
                ydl.download([url])

            else:
                # It's a single video
                print("Single video detected, downloading...")
                ydl.download([url])

        print("\n✅ Download completed successfully!")
        print(f"📂 Files are saved in: {output_path}")

    except Exception as e:
        print(f"\n❌ An error occurred: {str(e)}")
        print("\n🔧 Troubleshooting guide:")
        print("1. For private playlists, make sure you're logged in")
        print("2. Check your internet connection")
        print("3. Verify the playlist/video is available in your region")
        print("4. Make sure you have enough disk space")
        print("5. Ensure you have the latest version of yt-dlp:")
        print("   pip install -U yt-dlp")
        print("6. Verify ffmpeg is installed properly")


def print_progress(d):
    """Print download progress"""
    if d['status'] == 'downloading':
        try:
            # Calculate progress percentage
            progress = float(d['downloaded_bytes'] * 100 / d['total_bytes'])
            # Get current file name
            filename = d['filename'].split('/')[-1]
            print(f"\rDownloading: {filename[:50]}... {progress:.1f}%", end='', flush=True)
        except:
            pass
    elif d['status'] == 'finished':
        print("\n✓ Finished downloading, now converting...")


def main():
    print("YouTube Playlist Downloader (Highest Quality)")
    print("-------------------------------------------")

    # Get URL from user
    url = input("Enter YouTube playlist or video URL: ")

    # Optional custom output path
    use_custom_path = input("Use custom output path? (y/n, default: n): ").lower() == 'y'
    output_path = None
    if use_custom_path:
        output_path = input("Enter custom output path: ")

    # Start download
    download_playlist(url, output_path)


if __name__ == "__main__":
    main()