from TTS.api import TTS

# Initialize TTS with the model
tts = TTS(model_name="tts_models/zh-CN/baker/tacotron2-DDC-GST")

# Generate speech with adjusted pitch (lower for male-like voice)
tts.tts_to_file(text="你好，這是一個測試。", file_path="output_male.wav", pitch_shift=-4)
