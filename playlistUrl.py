from yt_dlp import YoutubeDL
from urllib.parse import parse_qs, urlparse
import DownloadSingleAud
import folder

from pathlib import Path

output_path = Path.home() / "Downloads" / "my_Audio"


def get_playlist_urls(playlist_url):
    """
    Extract all video URLs from a YouTube playlist

    Args:
        playlist_url (str): URL of the YouTube playlist

    Returns:
        list: List of video URLs in the playlist
    """
    try:
        ydl_opts = {
            'quiet': True,
            'extract_flat': True,
            'no_warnings': True
        }

        video_urls = []

        print(f"Extracting URLs from playlist: {playlist_url}")

        with YoutubeDL(ydl_opts) as ydl:
            result = ydl.extract_info(playlist_url, download=False)

            if 'entries' in result:
                count  = 1
                new_count =0
                for entry in result['entries']:
                    if entry:
                        video_id = entry['id']
                        video_url = f'https://www.youtube.com/watch?v={video_id}'
                        video_title = entry.get('title', 'Untitled')

                        if folder.contains_song(output_path, video_title):
                            print(f"\nSkipping {video_title}, audio already exists. --> ${count}")
                            count +=1
                            continue

                        video_urls.append({'url': video_url, 'title': video_title})
                        new_count +=1

                print(f"\nSuccessfully extracted {len(video_urls)} video URLs with new {new_count}")

                for i, video in enumerate(video_urls, 1):
                    try:
                        DownloadSingleAud.singleAUDIO(video['url'])
                        print("download_count ", i, "\n")
                    except Exception as e:
                        print(f"Error converting {video['title']}: {e}, skipping...")

                return video_urls
            else:
                print("No videos found in playlist")
                return []
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return []


def is_playlist_url(url):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    return 'list' in query_params


def main():
    url = input("Enter YouTube playlist URL: ")

    if not is_playlist_url(url):
        print("Warning: This doesn't appear to be a playlist URL.")
        proceed = input("Do you want to proceed anyway? (y/n): ")
        if proceed.lower() != 'y':
            return

    videos = get_playlist_urls(url)

    if videos:
        save = input("\nWould you like to save the URLs to a file? (y/n): ")
        if save.lower() == 'y':
            filename = "playlist_urls.txt"
            with open(filename, 'w', encoding='utf-8') as f:
                for video in videos:
                    f.write(f"{video['title']}\n{video['url']}\n\n")
            print(f"\nURLs saved to {filename}")


if __name__ == "__main__":
    main()
