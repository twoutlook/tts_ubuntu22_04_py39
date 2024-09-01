import re
from pydub import AudioSegment
from pydub.playback import play
from TTS.api import TTS

# Initialize the TTS model
tts = TTS(model_name="tts_models/en/vctk/vits", progress_bar=False)

# List available speakers
speakers = tts.speakers
print("Available speakers:", speakers)

# Famous movie lines with their corresponding movie names and years
movie_lines = [
    {"line": "I'll be back.", "movie": "The Terminator", "year": 1984},
    {"line": "May the Force be with you.", "movie": "Star Wars", "year": 1977},
    {"line": "Here's looking at you, kid.", "movie": "Casablanca", "year": 1942},
    {"line": "You can't handle the truth!", "movie": "A Few Good Men", "year": 1992},
    {"line": "To infinity and beyond!", "movie": "Toy Story", "year": 1995},
    {"line": "I'm the king of the world!", "movie": "Titanic", "year": 1997},
    {"line": "Why so serious?", "movie": "The Dark Knight", "year": 2008},
    {"line": "Houston, we have a problem.", "movie": "Apollo 13", "year": 1995},
    {"line": "E.T. phone home.", "movie": "E.T. the Extra-Terrestrial", "year": 1982},
    {"line": "There's no place like home.", "movie": "The Wizard of Oz", "year": 1939},
    {"line": "I see dead people.", "movie": "The Sixth Sense", "year": 1999},
    {"line": "Bond. James Bond.", "movie": "Dr. No", "year": 1962},
]

# Loop through the first 12 speakers and assign each a movie line
for speaker, movie_info in zip(speakers[:12], movie_lines):
    # Attempt to extract the numeric part of the speaker ID
    match = re.search(r'\d+', speaker)
    if match:
        speaker_id = match.group()
    else:
        # If no numeric part is found, skip this speaker
        print(f"Skipping speaker {speaker} as it does not contain a numeric ID.")
        continue

    # Text to synthesize, including the speaker's ID, movie line, movie name, and year, with a pause after the line
    text = (
        f"My ID number is {speaker_id}. "
        f"'{movie_info['line']}', "  # Comma for a pause after the movie line
        f"from the movie '{movie_info['movie']}' released in {movie_info['year']}."
    )

    # Define output file name based on the speaker ID
    output_file = f"output_{speaker_id}.wav"

    # Generate speech with the current speaker
    tts.tts_to_file(text=text, speaker=speaker, file_path=output_file)

    print(f"Generated speech with speaker ID {speaker_id}, saved to {output_file}")

    # Play the sound using pydub
    sound = AudioSegment.from_wav(output_file)
    play(sound)
