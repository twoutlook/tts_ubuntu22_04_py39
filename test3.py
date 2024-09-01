from TTS.api import TTS

# Initialize TTS with the model
tts = TTS(model_name="tts_models/zh-CN/baker/tacotron2-DDC-GST")

# List available speakers (if the model supports it)
tts.list_speaker_ids()

# Generate speech using a specific male speaker ID
tts.tts_to_file(text="你好，這是一個測試。", file_path="output_male.wav", speaker_id=0)  # Replace 0 with the ID of the male speaker
