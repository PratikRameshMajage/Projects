import os
import tkinter as tk
import tkinter.filedialog as filedialog
import pygame

class MusicPlayer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Music Player")
        self.root.geometry("300x100")

        self.current_directory = os.getcwd()
        self.playlist = []

        self.play_button = tk.Button(self.root, text="Play", command=self.play_music)
        self.play_button.pack(side="left", padx=10, pady=10)

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_music)
        self.stop_button.pack(side="left", padx=10, pady=10)

        self.add_button = tk.Button(self.root, text="Add", command=self.add_music)
        self.add_button.pack(side="left", padx=10, pady=10)

        self.remove_button = tk.Button(self.root, text="Remove", command=self.remove_music)
        self.remove_button.pack(side="left", padx=10, pady=10)

    def play_music(self):
        if self.playlist:
            pygame.mixer.music.load(self.playlist[0])
            pygame.mixer.music.play()

    def stop_music(self):
        pygame.mixer.music.stop()

    def add_music(self):
        filetypes = (("Audio Files", "*.mp3"), ("All Files", "*.*"))
        filename = filedialog.askopenfilename(initialdir=self.current_directory, title="Select File", filetypes=filetypes)
        if filename:
            self.playlist.append(filename)

    def remove_music(self):
        if self.playlist:
            self.playlist.pop(0)

    def run(self):
        pygame.mixer.init()
        self.root.mainloop()

if __name__ == "__main__":
    app = MusicPlayer()
    app.run()
