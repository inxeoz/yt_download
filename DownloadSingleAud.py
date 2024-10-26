from yt_dlp import YoutubeDL
import os
from pathlib import Path

def singleAUDIO(
    url="https://youtu.be/bzW9fmwcmG4?si=GETlG5Bc1ukGZ78b",
    output_path=str(Path.home() / "Downloads" / "test Audio")
):
    # Create the output directory if it doesn't exist
    os.makedirs(output_path, exist_ok=True)

    # Options for yt-dlp
    ydl_opts = {
        'format': 'bestaudio/best',
         'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',  # Highest MP3 quality
            }],
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),  # Specify the output template to include the path
        'verbose': False  # Set to True if you want to see detailed progress
    }

    try:
        print(f"Starting download from: {url}")
        print(f"Files will be saved to: {output_path}")

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print("\nDownload completed successfully!")
        print(f"Check your folder: {output_path}")

    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
        print("\nTroubleshooting steps:")
        print("1. Make sure you have installed yt-dlp: pip install yt-dlp")
        print("2. Make sure you have installed ffmpeg")
        print("3. Check your internet connection")
        print("4. Verify you have write permissions in your Downloads folder")

# # Example usage
# if __name__ == "__main__":
#     singleAUDIO()
