import os
from whisper_jax import FlaxWhisperPipline
from tqdm import tqdm  # Import tqdm for the progress bar

# Instantiate the Whisper pipeline
pipeline = FlaxWhisperPipline("openai/whisper-base")

# Input directory containing audio files
input_directory = "../video_to_mp3"

# Output directory for the transcriptions
output_directory = "../transcriptions"

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# List audio files in the input directory
audio_files = [os.path.join(input_directory, file) for file in os.listdir(input_directory) if file.endswith(".mp3")]

# Initialize tqdm to display the progress bar for transcribing audio files
progress_bar_audio = tqdm(total=len(audio_files), desc="Transcribing Audio")

# Loop through each audio file and transcribe
for index, audio_file in enumerate(audio_files, start=1):
    try:
        # Perform ASR (Automatic Speech Recognition)
        transcriptions = pipeline(audio_file, task="transcribe")

        # Extract the transcription text as a string
        transcription_text = transcriptions["text"]

        # Save the transcription to a text file
        transcription_file = os.path.join(output_directory, f"transcription_{index}.txt")

        with open(transcription_file, "w", encoding="utf-8") as text_file:
            text_file.write(transcription_text)

        # Update the progress bar for audio file processing
        progress_bar_audio.update(1)
        progress_bar_audio.set_postfix({"File": audio_file})

    except Exception as e:
        print(f"Audio {index}: An error occurred while processing {audio_file}: {str(e)}")

# Close the progress bar for audio file processing
progress_bar_audio.close()

# Now, you can create a progress bar for the overall transcription process
progress_bar_transcription = tqdm(total=len(audio_files), desc="Transcribing Progress")

# Loop through each audio file again to update the overall progress bar
for _ in audio_files:
    # Update the progress bar for the overall transcription process
    progress_bar_transcription.update(1)

# Close the progress bar for the overall transcription process
progress_bar_transcription.close()
