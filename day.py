import pygame
import sys
from moviepy.editor import ImageSequenceClip

# Initialisierung von Pygame
pygame.init()

# Bildschirmgröße
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tag-Animation")

# Farben
DAY_COLOR = (135, 206, 235)  # Himmelblau
SUN_COLOR = (255, 223, 0)    # Sonnengelb

# Sonne Eigenschaften
sun_pos = [ -100, 100 ]  # Start außerhalb des Bildschirms

# Animationseinstellungen
fps = 30
clock = pygame.time.Clock()
total_frames = fps * 10  # 10 Sekunden Animation
frames = []

for frame in range(total_frames):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Hintergrundfarbe setzen
    screen.fill(DAY_COLOR)

    # Sonne bewegen
    sun_pos[0] += WIDTH / (total_frames / 2)  # Sonne bewegt sich in 5 Sekunden bis vollständig sichtbar

    if sun_pos[0] < WIDTH + 100:
        pygame.draw.circle(screen, SUN_COLOR, (int(sun_pos[0]), int(sun_pos[1])), 50)

    pygame.display.flip()

    # Screenshot des Frames speichern
    frame_surface = pygame.display.get_surface()
    frame_data = pygame.surfarray.array3d(frame_surface)
    frame_data = frame_data.transpose([1, 0, 2])
    frames.append(frame_data)

    clock.tick(fps)

# Video mit MoviePy erstellen
clip = ImageSequenceClip(frames, fps=fps)
clip.write_videofile("day.mp4", codec='libx264')

pygame.quit()
