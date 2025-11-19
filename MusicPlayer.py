import customtkinter
import pygame
from mutagen.mp3 import MP3
import os

pygame.mixer.init()

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
root = customtkinter.CTk()
root.title("MusicPlayer")
root.geometry("600x600")
root.attributes("-alpha", 0.9)
root.resizable(False, False)
songs = [f for f in os.listdir('.') if f.endswith('.mp3')]

# this is the sidepart which shows what songs are playing 

song_label = customtkinter.CTkLabel(root, text="", height=600, width=300,fg_color="grey", font=("Arial", 24),corner_radius=0, anchor="center", justify="center",text_color="black"
)
song_label.place(x=300, y=0)
is_playing = False
current_song = songs[0] if songs else None
song_length = 1
is_paused = False
current_pos = 0
fast_forward_amount = 10
backward_amount = 10

def set_volume(val):
    volume = float(val)
    pygame.mixer.music.set_volume(volume)

def pause_song():
    global is_paused, is_playing
    if is_playing and not is_paused:
        pygame.mixer.music.pause()
        is_paused = True
    elif is_playing and is_paused:
        pygame.mixer.music.unpause()
        is_paused = False


pause_button = customtkinter.CTkButton(root, text="Pause", command=pause_song, corner_radius=0)
pause_button.place(x=380, y=500)

progress = customtkinter.CTkProgressBar(root, width=280, height=20, corner_radius=0)
progress.place(x=310, y=550)
progress.set(0)


def play_song(song_name):
    global is_playing, is_paused, current_song, song_length, current_pos
    current_song = song_name
    display_name = current_song
    if len(current_song) > 25:
        display_name = current_song[:25] + "..."
    song_label.configure(text=display_name)
    audio = MP3(current_song)
    song_length = audio.info.length
    current_pos = 0
    song_label.configure(text=display_name)
    pygame.mixer.music.load(current_song)
    pygame.mixer.music.play()
    is_playing = True


# buttons
scroll_frame = customtkinter.CTkScrollableFrame(root, width=250, height=580)
scroll_frame.place(x=10, y=10)

for s in songs:
    display_name = s if len(s) <= 25 else s[:25] + "..."
    btn = customtkinter.CTkButton(
        scroll_frame,
        text=display_name,
        border_color="gray",
        hover_color="gray",
        command=lambda s=s: play_song(s)
    )
    btn.pack(pady=2)
volume_slider = customtkinter.CTkSlider(root, from_=0, to=1, number_of_steps=100, command=set_volume, width=250)
volume_slider.place(x=325, y=580)
volume_slider.set(0.5)
def update_progress():
    global current_pos
    if is_playing and current_song:
        pos = current_pos + pygame.mixer.music.get_pos() / 1000
        progress.set(min(pos / song_length, 1))
    root.after(100, update_progress)


def fast_forward():
    global current_pos, song_length, is_playing

    if not is_playing or not current_song:
        return
    current_pos += fast_forward_amount
    if current_pos >= song_length:
        current_pos = song_length - 0.1
    pygame.mixer.music.set_pos(current_pos)


def rewind():
    global current_pos, current_song, is_playing

    if not is_playing or not current_song:
        return

    current_pos -= backward_amount
    if current_pos < 0:
        current_pos = 0
    pygame.mixer.music.set_pos(current_pos)


rewind_button = customtkinter.CTkButton(root, text="<-", border_color="gray", corner_radius=0, command=rewind,height=27, width=30)
rewind_button.place(x=320, y=500)
fast_forward_button = customtkinter.CTkButton(root, text="->", border_color="gray", corner_radius=0,command=fast_forward, height=27, width=30)
fast_forward_button.place(x=550, y=500)

update_progress()
root.mainloop()