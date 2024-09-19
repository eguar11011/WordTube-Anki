import yt_dlp
import whisper
import json
import torch
import os

def get_youtube_config():
    """
    Returns the YouTube video URL and yt-dlp options for downloading audio.
    
    Returns:
        tuple: A tuple containing the list of URLs and the yt-dlp options dictionary.
    """
    urls = ['https://www.youtube.com/watch?v=MES3ZG9wxSU&t=343s']
    ydl_opts = {
        'format': 'm4a/bestaudio/best',
        'postprocessors': [{  # Extract audio using ffmpeg
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
        }],
        'outtmpl': '%(title)s.%(ext)s',  # Name the downloaded file using the video title
    }
    return urls, ydl_opts

def download_audio(urls, options):
    """Download audio from YouTube using yt-dlp."""
    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download(urls)

def get_audio_filename():
    """Get the filename of the downloaded audio file."""
    for file in os.listdir():
        if file.endswith(".m4a"):
            return file
    raise FileNotFoundError("Audio file not found. Please ensure the file was downloaded correctly.")

def transcribe_audio(audio_file):
    """Transcribe the audio file using Whisper model."""
    device = torch.device("cuda:1" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")

    model = whisper.load_model("base")
    model.to(device)
    
    result = model.transcribe(audio_file)
    return result

def save_transcription(result, filename):
    """Save the transcription result to a JSON file."""
    with open(filename, "w") as json_file:
        json.dump(result, json_file, indent=4)
    print(f"Transcription result saved to {filename}")

if __name__ == "__main__":
    try:
        # Get configuration
        urls, ydl_opts = get_youtube_config()
        
        # Process the audio
        download_audio(urls, ydl_opts)
        audio_file = get_audio_filename()
        transcription_result = transcribe_audio(audio_file)
        save_transcription(transcription_result, "layer_bronze.json")
    except Exception as e:
        print(f"An error occurred: {e}")
