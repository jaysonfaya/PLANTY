import pygame
import sys
from moviepy.editor import ImageSequenceClip
import random

# Initialisierung von Pygame
pygame.init()

# Bildschirmgröße
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Nacht-Animation")

# Farben
NIGHT_COLOR = (25, 25, 112)  # Mitternachtsblau
MOON_COLOR = (220, 220, 220) # Mondgrau
STAR_COLOR = (255, 255, 255)

# Mond Eigenschaften
moon_pos = [ -100, 100 ]  # Start außerhalb des Bildschirms

# Sterne generieren
stars = [(random.randint(0, WIDTH), random.randint(0, HEIGHT//2)) for _ in range(100)]

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
    screen.fill(NIGHT_COLOR)

    # Sterne zeichnen
    for star in stars:
        pygame.draw.circle(screen, STAR_COLOR, star, 2)

    # Mond bewegen
    moon_pos[0] += WIDTH / (total_frames / 2)  # Mond bewegt sich in 5 Sekunden bis vollständig sichtbar

    if moon_pos[0] < WIDTH + 100:
        pygame.draw.circle(screen, MOON_COLOR, (int(moon_pos[0]), int(moon_pos[1])), 40)
        # Optional: Monddetails (z.B. Krater)
        pygame.draw.circle(screen, (255, 255, 255), (int(moon_pos[0] - 10), int(moon_pos[1] - 10)), 10)

    pygame.display.flip()

    # Screenshot des Frames speichern
    frame_surface = pygame.display.get_surface()
    frame_data = pygame.surfarray.array3d(frame_surface)
    frame_data = frame_data.transpose([1, 0, 2])
    frames.append(frame_data)

    clock.tick(fps)

# Video mit MoviePy erstellen
clip = ImageSequenceClip(frames, fps=fps)
clip.write_videofile("night.mp4", codec='libx264')

pygame.quit()
