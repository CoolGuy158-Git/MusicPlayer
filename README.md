# Python Music Player 

A simple, lightweight music player built using Python, CustomTkinter, and Pygame. Play your .mp3 files, control playback, and monitor progress—all with a sleek, semi-transparent GUI.

## Screenshot
![Music Player Screenshot](Photo%20(2).png)


## Features

Browse and play .mp3 files from the project folder

Play / Pause functionality

Fast Forward and Rewind controls

Progress Bar to show the current position of the song

Simple and modern CustomTkinter GUI

Semi-transparent window for a sleek look

## Requirements

- Python 3.8+

- CustomTkinter

- Pygame

- Mutagen

Install using pip install

```bash
pip install customtkinter pygame mutagen
```

## How to Use

- Place your .mp3 files in the same directory as the script.

- Run the Python script:

```bash
python MusicPlayer.py
```

- Click on a song button to play it.

- Use the Pause button to pause/resume playback.

- Use -> to fast forward and <- to rewind.

- Watch the progress bar track the song’s current position.

## Code Overview

- songs = [f for f in os.listdir('.') if f.endswith('.mp3')] → Automatically loads all MP3 files in the folder

- play_song(song_name) → Plays the selected song

- pause_song() → Toggles pause/resume

- fast_forward() → Skips forward by a set number of seconds

- rewind() → Goes backward by a set number of seconds

- update_progress() → Continuously updates the progress bar

## Notes / Limitations

- Only plays .mp3 files in the same directory as the script

- Progress bar updates may lag slightly depending on system performance

- Fast forward and rewind reset the Pygame music position, which may briefly restart playback

## Future Improvements

- Support playlists and multiple directories

- Add volume control

- Smooth, continuous progress bar update without jumpiness

- Add GUI themes or custom skins

## License

**MIT License**
