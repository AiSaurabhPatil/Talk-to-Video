from whisper_jax import FlaxWhisperPipline
from tqdm import tqdm
# instantiate pipeline
pipeline = FlaxWhisperPipline("openai/whisper-base")

# JIT compile the forward call - slow, but we only do once
text = pipeline("../video_to_mp3/audio_1.mp3")
print(type(text))
print(text)