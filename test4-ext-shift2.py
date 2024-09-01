import librosa
import soundfile as sf

# Load the generated audio file
y, sr = librosa.load("output_male.wav", sr=22050)

# Shift the pitch (now using sr as a keyword argument)
y_shifted = librosa.effects.pitch_shift(y, sr=sr, n_steps=-2)

# Save the modified audio
sf.write("output_male_low_pitch.wav", y_shifted, sr)
