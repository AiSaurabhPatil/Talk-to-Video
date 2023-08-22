import pytube
import os
import datetime

def youtube_to_mp3(youtube_url, output_path,index):
    try:
        # Create a YouTube object
        yt = pytube.YouTube(youtube_url)

        # Choose the best audio stream
        audio_stream = yt.streams.filter(only_audio=True).first()

        # Download the audio stream
        audio_stream.download(output_path)
        
        # Rename the downloaded file to have a .mp3 extension
        downloaded_file = os.path.join(output_path, audio_stream.default_filename)
        mp3_file = os.path.join(output_path, f"audio_{index}.mp3")
        os.rename(downloaded_file, mp3_file)

        print(f"The YouTube video has been successfully converted to MP3: {mp3_file}")

    except pytube.exceptions.RegexMatchError:
        print(f"Invalid YouTube URL: {youtube_url}. Skipping...")
    except Exception as e:
        print(f"An error occurred while processing {youtube_url}: {str(e)}")

if __name__ == "__main__":
    # List of YouTube video URLs to convert
    youtube_links = [
        "https://youtu.be/msWTTk4nghU",
        "https://youtu.be/nHaspOiZqbA",
        "https://youtu.be/9sfK9lA5E4M",
        "https://youtu.be/pBlEXeBK3rY",
        "https://youtu.be/aVWis_F4n7c",
        "https://youtu.be/Syh_Au3Vogo",
        "https://youtu.be/BamWDV8XMEM",
        "https://youtu.be/GUnCHUOghWQ",
        "https://youtu.be/BRQQ3Tu6HKg",
        "https://youtu.be/Mc-AwQPFEhM",
        "https://youtu.be/9aS9R6xOqYg",
        "https://youtu.be/PYAkJ92Pu3Q"
    ]

    # Output directory for the converted MP3 files
    output_directory = "../video_to_mp3"

    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Convert each YouTube video to an MP3 file
    for index, link in enumerate(youtube_links, start=1):
        youtube_to_mp3(link, output_directory, index)