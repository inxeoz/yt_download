from yt_dlp import YoutubeDL
import os
from pathlib import Path

def singleAUDIO(
    url="https://youtu.be/bzW9fmwcmG4?si=GETlG5Bc1ukGZ78b",
    output_path=str(Path.home() / "Downloads" / "my_Audio")
):
    # Create the output directory if it doesn't exist
    os.makedirs(output_path, exist_ok=True)

    ydl_opts = {
        'format': 'bestaudio/best',  # Selects the best available audio format
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',  # Force highest MP3 quality
            },
            {
                'key': 'FFmpegMetadata'  # Retains metadata (artist, title, etc.)
            },
            {
                'key': 'EmbedThumbnail'  # Embeds the thumbnail into the MP3 file
            }
        ],
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),  # Custom output filename
        'writethumbnail': True,  # Download thumbnail for embedding
        'embedthumbnail': True,  # Ensure thumbnails are embedded in MP3
        'addmetadata': True,  # Add metadata to the file
        'prefer_ffmpeg': True,  # Ensures FFmpeg is used for processing
        'verbose': False,  # Set to True for debugging
    }

    # Options for yt-dlp
    # ydl_opts = {
    #     'format': 'bestaudio/best',
    #      'postprocessors': [{
    #             'key': 'FFmpegExtractAudio',
    #             'preferredcodec': 'mp3',
    #             'preferredquality': '320',  # Highest MP3 quality
    #         }],
    #     'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),  # Specify the output template to include the path
    #     'verbose': False  # Set to True if you want to see detailed progress
    # }

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
        return []

# # Example usage
# if __name__ == "__main__":
#     singleAUDIO()
