import pygame
# Initialize the pygame module
pygame.init()
# Create a window to display the music player
screen = pygame.display.set_mode((400, 400))
# Create a list of songs
songs = ["song1.mp3", "song2.mp3", "song3.mp3"]
# Create a variable to store the current song
current_song = 0
# Create a function to play the current song
def play_song():
    # Load the current song
    song = pygame.mixer.music.load(songs[current_song])
    # Play the song
    pygame.mixer.music.play()
# Create a function to stop the current song
def stop_song():
    # Stop the current song
    pygame.mixer.music.stop()
# Create a function to pause the current song
def pause_song():
    # Pause the current song
    pygame.mixer.music.pause()
# Create a function to resume the current song
def resume_song():
    # Resume the current song
    pygame.mixer.music.unpause()
# Create a function to change the current song
def change_song(new_song):
    # Stop the current song
    stop_song()
    # Set the current song to the new song
    current_song = new_song
    # Play the new song
    play_song()
# Create a loop to run the music player
while True:
    # Check for events
    for event in pygame.event.get():
        # If the user presses the play button, play the current song
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            play_song()
        # If the user presses the stop button, stop the current song
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            stop_song()
        # If the user # If the user presses the pause button, pause the current song
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pause_song()
        # If the user presses the next button, change to the next song
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            change_song((current_song + 1) % len(songs))
        # If the user presses the previous button, change to the previous song
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            change_song((current_song - 1) % len(songs))
    # Update the screen
    pygame.display.update()