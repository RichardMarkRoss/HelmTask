# Define a class to represent a song
class Song:
    def __init__(self, name):
        self.name = name
        self.next = None  # Initialize the next song as None

    # Method to set the next song in the playlist
    def next_song(self, song):
        self.next = song

    # Method to check if the playlist is repeating
    def is_repeating_playlist(self):
        # Initialize two pointers, slow and fast, both starting from the first song
        slow = self
        fast = self.next  # Assuming there's at least one song in the playlist

        # Traverse the playlist
        while fast is not None and fast.next is not None:
            # If the slow and fast pointers meet, there's a repeating cycle
            if slow == fast:
                return True

            # Move the slow pointer by one song
            slow = slow.next
            # Move the fast pointer by two songs
            fast = fast.next.next

        # If the fast pointer reaches the end, there's no repeating cycle
        return False

# Test the code
first = Song("Hello")
second = Song("Eye of the tiger")

# Link the songs together to form a playlist
first.next_song(second)
second.next_song(first)

# Check if the playlist is repeating and print the result
print(first.is_repeating_playlist())  # Output: True