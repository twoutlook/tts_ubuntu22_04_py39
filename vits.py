from TTS.api import TTS

# Initialize the TTS model
tts = TTS(model_name="tts_models/en/vctk/vits", progress_bar=False)

# List available speakers
speakers = tts.speakers
print("Available speakers:", speakers)

# Select a specific speaker by their ID
selected_speaker = "p225"  # Replace with the speaker ID you want to use

# Text to synthesize
text = "Hello, this is a test using a specific speaker from the VCTK dataset."

# Generate speech with the selected speaker
tts.tts_to_file(text=text, speaker=selected_speaker, file_path="output.wav")

print(f"Generated speech with speaker {selected_speaker}")
