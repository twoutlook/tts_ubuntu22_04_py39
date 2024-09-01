from TTS.api import TTS

# Initialize TTS with the Chinese model
tts = TTS(model_name="tts_models/zh-CN/baker/tacotron2-DDC-GST")

# Generate speech from Chinese text
tts.tts_to_file(text="是一家專注於開發尖端開源語音技術的公司。他們的使命是讓高品質的語音工具對所有人都可及，從而使開發者、研究人員和企業能夠輕鬆構建具備語音功能的應用程式", file_path="output_chinese.wav")
