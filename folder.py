from pathlib import Path


output_path = Path.home() / "Downloads" / "my_Audio"

def get_mp3_files(folder_path):
    """Get a list of all MP3 filenames (without extension) in the given folder."""
    folder = Path(folder_path)
    return [file.stem.replace("｜", "|") for file in folder.glob("*.mp3")]  # Normalize Unicode bar

def contains_song(folder_path, x):
    """Check if any MP3 filename in the folder contains the given string x."""
    mp3_files = get_mp3_files(folder_path)
    x = x.replace("｜", "|")  # Normalize input string
    return any(x.lower() in song.lower() for song in mp3_files)

# # Example usage
# folder_path = Path.home() / "Downloads" / "my_Audio"
# x = "Ishq Vishq Pyaar Vyaar | Shahid Kapoor | Amrita Rao | Kumar Sanu | Alka Yagnik | Hindi Love Song"
# if contains_song(folder_path, x):
#     print(f"A song containing '{x}' already exists.")
# else:
#     print(f"No song found containing '{x}'.")
