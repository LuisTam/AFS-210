import random

class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def __str__(self):
        return f"{self.title} by {self.artist}"

    def __eq__(self, other):
        return ((self.title, self.artist) == (other.title, other.artist))

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))

    def __gt__(self, other):
        return ((self.title, self.artist) > (other.title, other.artist))


class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"{song} removed from the playlist.")
        else:
            print(f"{song} not found in the playlist.")

    def play(self):
        if self.songs:
            print("Playing:", self.songs[0])
        else:
            print("Playlist is empty.")

    def skip(self):
        if len(self.songs) > 1:
            self.songs.pop(0)
            print("Skipping to the next song.")
            print("Now playing:", self.songs[0])
        else:
            print("Playlist only has one song. Cannot skip.")

    def go_back(self):
        if len(self.songs) > 1:
            self.songs.pop(0)
            self.songs.insert(0, self.songs[-1])
            print("Going back to the previous song.")
            print("Now playing:", self.songs[0])
        else:
            print("Playlist only has one song. Cannot go back.")

    def shuffle(self):
        random.shuffle(self.songs)
        print("Playlist shuffled.")
        print("Now playing:", self.songs[0])

    def show_currently_playing(self):
        if self.songs:
            print("Currently playing:", self.songs[0])
        else:
            print("No song is currently playing.")

    def show_current_playlist_order(self):
        if self.songs:
            print("\nSong list:")
            for song in self.songs:
                print(song)
        else:
            print("Playlist is empty.")


def menu():
    print(20 * "-", "MENU", 20 * "-")
    print("1. Add Song to Playlist")
    print("2. Remove Song from Playlist")
    print("3. Play")
    print("4. Skip")
    print("5. Go Back")
    print("6. Shuffle")
    print("7. Show Currently Playing Song")
    print("8. Show Current Playlist Order")
    print("0. Exit")
    print(47 * "-")


playlist = Playlist()
playlist.add_song("Smooth Operator")
playlist.add_song("Blue to Blue")
playlist.add_song("Miss Primetime")
playlist.add_song("Solar System")
playlist.add_song("About that life")
playlist.add_song("All I Wanna do")

while True:
    menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        title = input("Enter song title: ")
        artist = input("Enter artist name: ")
        new_song = Song(title, artist)
        playlist.add_song(new_song)
        print(f"{new_song} added to the playlist.")
    elif choice == 2:
        title = input("Enter song title to remove: ")
        artist = input("Enter artist name: ")
        song_to_remove = Song(title, artist)
        playlist.remove_song(song_to_remove)
    elif choice == 3:
        playlist.play()
    elif choice == 4:
        playlist.skip()
    elif choice == 5:
        playlist.go_back()
    elif choice == 6:
        playlist.shuffle()
    elif choice == 7:
        playlist.show_currently_playing()
    elif choice == 8:
        playlist.show_current_playlist_order()
    elif choice == 0:
        print("Goodbye.")
        break
    else:
        print("Invalid choice. Please enter a number between 0 and 8.")

