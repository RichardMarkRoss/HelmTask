class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song

    def is_repeating_playlist(self):
        seen_songs = set()
        current_song = self
        while current_song is not None:
            if current_song in seen_songs:
                return True
            seen_songs.add(current_song)
            current_song = current_song.next
        return False

first = Song("Hello")
second = Song("Eye of the tiger")
first.next_song(second)
second.next_song(first)
print(first.is_repeating_playlist())