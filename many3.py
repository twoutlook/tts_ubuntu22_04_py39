from pydub import AudioSegment
from pydub.playback import play
from TTS.api import TTS

# Initialize the TTS model
tts = TTS(model_name="tts_models/en/vctk/vits", progress_bar=False)

# List available speakers
speakers = tts.speakers
print("Available speakers:", speakers)

# Loop through all available speakers and generate speech
for speaker in speakers[:7]:
    # Text to synthesize, starting with the speaker's name
    text = f"My name is {speaker}. 試試講中文"

    # Define output file name based on the speaker ID
    output_file = f"output2_{speaker}.wav"

    # Generate speech with the current speaker
    tts.tts_to_file(text=text, speaker=speaker, file_path=output_file)

    print(f"Generated speech with speaker {speaker}, saved to {output_file}")

    # Play the sound using pydub
    sound = AudioSegment.from_wav(output_file)
    play(sound)
