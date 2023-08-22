from whisper_jax import FlaxWhisperPipline
import os 

# Instantiate the pipeline
pipeline = FlaxWhisperPipline("openai/whisper-base")

# List of audio files to transcribe
input_directory = "../video_to_mp3"
audio_files = [os.path.join(input_directory, file) for file in os.listdir(input_directory) if file.endswith(".mp3")]

# Output directory for the transcriptions
output_directory = "../transcriptions"

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Loop through each audio file and transcribe
for index, audio_file in enumerate(audio_files, start=1):
    try:
        # Perform ASR (Automatic Speech Recognition)
        transcription = pipeline(audio_file, task="transcribe")
        transcription_text = transcription["text"]

        # Save the transcription to a text file
        transcription_file = os.path.join(output_directory, f"transcription_{index}.txt")

        with open(transcription_file, "w", encoding="utf-8") as text_file:
            text_file.write(transcription_text)

        print(f"Audio {index}: Transcription saved to {transcription_file}")

    except Exception as e:
        print(f"Audio {index}: An error occurred while processing {audio_file}: {str(e)}")
