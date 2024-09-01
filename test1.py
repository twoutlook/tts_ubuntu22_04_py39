from TTS.api import TTS

# Initialize TTS with your model path
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC_ph")

# Generate speech
tts.tts_to_file(text="Do you know what gets really scared in the fridge? ")
