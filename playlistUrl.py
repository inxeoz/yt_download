from yt_dlp import YoutubeDL
from urllib.parse import parse_qs, urlparse
import  DownloadSingleAud

def get_playlist_urls(playlist_url):
    """
    Extract all video URLs from a YouTube playlist

    Args:
        playlist_url (str): URL of the YouTube playlist

    Returns:
        list: List of video URLs in the playlist
    """
    try:
        # Configure yt-dlp options
        ydl_opts = {
            'quiet': True,  # Suppress output
            'extract_flat': True,  # Don't download videos, just get info
            'no_warnings': True  # Don't show warnings
        }

        # Initialize empty list for URLs
        video_urls = []

        print(f"Extracting URLs from playlist: {playlist_url}")

        with YoutubeDL(ydl_opts) as ydl:
            # Extract playlist info
            result = ydl.extract_info(playlist_url, download=False)

            if 'entries' in result:
                # Process each video in the playlist
                for entry in result['entries']:
                    if entry:
                        video_id = entry['id']
                        video_url = f'https://www.youtube.com/watch?v={video_id}'
                        video_title = entry.get('title', 'Untitled')
                        video_urls.append({
                            'url': video_url,
                            'title': video_title
                        })

                print(f"\nSuccessfully extracted {len(video_urls)} video URLs")

                # Print first few videos as example
                print("\nFirst few videos in playlist:")
                for i, video in enumerate(video_urls[:3], 1):
                    print(f"{i}. {video['title']}")

                if len(video_urls) > 3:
                    print(f"...and {len(video_urls) - 3} more videos")

                for i, video in enumerate(video_urls, 1):
                    DownloadSingleAud.singleAUDIO(video['url'])

                return video_urls
            else:
                print("No videos found in playlist")
                return []

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print("\nPossible issues:")
        print("1. Invalid playlist URL")
        print("2. Private or unavailable playlist")
        print("3. Network connection error")
        return []


def is_playlist_url(url):
    """Check if URL is a playlist URL"""
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    return 'list' in query_params


def main():
    # Example usage
    url = input("Enter YouTube playlist URL: ")

    if not is_playlist_url(url):
        print("Warning: This doesn't appear to be a playlist URL.")
        print("Make sure the URL contains 'list=' parameter.")
        proceed = input("Do you want to proceed anyway? (y/n): ")
        if proceed.lower() != 'y':
            return

    # Get the video URLs
    videos = get_playlist_urls(url)

    # Save URLs to a file (optional)
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