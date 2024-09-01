from TTS.api import TTS

# Initialize the TTS model
tts = TTS(model_name="tts_models/en/vctk/vits", progress_bar=False)

# List available speakers
speakers = tts.speakers
print("Available speakers:", speakers)

# Loop through all available speakers and generate speech
for speaker in speakers:
    # Text to synthesize, starting with the speaker's name
    text = f"My name is {speaker}. Hello, this is a test using a specific speaker from the VCTK dataset."

    # Define output file name based on the speaker ID
    output_file = f"output_{speaker}.wav"
    
    # Generate speech with the current speaker
    tts.tts_to_file(text=text, speaker=speaker, file_path=output_file)
    
    print(f"Generated speech with speaker {speaker}, saved to {output_file}")
