from yt_dlp import YoutubeDL
import os
from pathlib import Path

# Create downloads directory in user's home directory
output_path = str(Path.home() / "Downloads" / "YouTube Audio")
os.makedirs(output_path, exist_ok=True)

# Configure yt-dlp options
ydl_opts = {
    'format': 'bestaudio/best',
    'paths': {'home': output_path},
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': '%(title)s.%(ext)s',
    'verbose': False  # Set to True if you want to see detailed progress
}

# The URL you provided
url = "https://youtu.be/bzW9fmwcmG4?si=GETlG5Bc1ukGZ78b"

try:
    print(f"Starting download from: {url}")
    print(f"Files will be saved to: {output_path}")

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print("\nDownload completed successfully!")
    print(f"Check your Downloads folder in a subfolder called 'YouTube Audio'")

except Exception as e:
    print(f"\nAn error occurred: {str(e)}")
    print("\nTroubleshooting steps:")
    print("1. Make sure you have installed yt-dlp: pip install yt-dlp")
    print("2. Make sure you have installed ffmpeg")
    print("3. Check your internet connection")
    print("4. Verify you have write permissions in your Downloads folder")