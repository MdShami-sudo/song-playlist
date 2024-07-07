import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import pygame
import os
pygame.init()
pygame.mixer.init()

class PlaylistManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Playlist Manager")

        # Initialize playlist
        self.playlist = []

        # Create GUI components
        self.create_widgets()

    def create_widgets(self):
        # Frame for playlist display
        playlist_frame = ttk.Frame(self.root)
        playlist_frame.pack(pady=10)

        # Playlist label
        self.playlist_label = ttk.Label(playlist_frame, text="Playlist:")
        self.playlist_label.pack()

        # Playlist listbox
        self.playlist_listbox = tk.Listbox(playlist_frame, height=10, width=50)
        self.playlist_listbox.pack(pady=10)

        # Frame for buttons
        buttons_frame = ttk.Frame(self.root)
        buttons_frame.pack()

        # Buttons
        add_button = ttk.Button(buttons_frame, text="Add Song", command=self.add_song)
        add_button.grid(row=0, column=0, padx=5)

        remove_button = ttk.Button(buttons_frame, text="Remove Song", command=self.remove_song)
        remove_button.grid(row=0, column=1, padx=5)

        play_button = ttk.Button(buttons_frame, text="Play", command=self.play_song)
        play_button.grid(row=0, column=2, padx=5)

        stop_button = ttk.Button(buttons_frame, text="Stop", command=self.stop_song)
        stop_button.grid(row=0, column=3, padx=5)

    def add_song(self):
        file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
        if file_path:
            song = os.path.basename(file_path)
            self.playlist.append(file_path)
            self.playlist_listbox.insert(tk.END, song)

    def remove_song(self):
        selected_song_index = self.playlist_listbox.curselection()
        if selected_song_index:
            self.playlist_listbox.delete(selected_song_index)
            del self.playlist[selected_song_index[0]]

    def play_song(self):
        selected_song_index = self.playlist_listbox.curselection()
        if selected_song_index:
            song_path = self.playlist[selected_song_index[0]]
            pygame.mixer.music.load(song_path)
            pygame.mixer.music.play()

    def stop_song(self):
        pygame.mixer.music.stop()


# Main function
def main():
    root = tk.Tk()
    app = PlaylistManagerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
