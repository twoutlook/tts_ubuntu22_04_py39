from pydub import AudioSegment

# Load the generated audio file
sound = AudioSegment.from_wav("output_male.wav")

# Lower the pitch by reducing the playback speed
octaves = -0.5  # A negative value lowers the pitch (0.5 represents one octave)

new_sample_rate = int(sound.frame_rate * (2.0 ** octaves))

# Change the frame rate to achieve pitch shift
low_pitch_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})

# Save the modified audio
low_pitch_sound = low_pitch_sound.set_frame_rate(22050)
low_pitch_sound.export("output_male_low_pitch.wav", format="wav")
