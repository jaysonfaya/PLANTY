import pygame
import sys
from moviepy.editor import ImageSequenceClip
import os

# Initialisierung von Pygame
pygame.init()

# Bildschirmgröße
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wasser-Animation")

# Farben
BACKGROUND_COLOR = (135, 206, 235)  # Himmelblau
WATER_COLOR = (0, 191, 255)        # Wasserblau

# Tropfen Eigenschaften
class Drop:
    def __init__(self, x, y, radius, speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed

    def move(self):
        self.y += self.speed

    def draw(self, surface):
        pygame.draw.circle(surface, WATER_COLOR, (int(self.x), int(self.y)), self.radius)

# Animationseinstellungen
fps = 30
clock = pygame.time.Clock()
total_seconds = 3
total_frames = fps * total_seconds
frames = []

# Tropfenliste
drops = []
import random

for _ in range(20):
    x = random.randint(100, WIDTH - 100)
    y = random.randint(-HEIGHT, 0)
    radius = random.randint(5, 10)
    speed = random.uniform(2, 5)
    drops.append(Drop(x, y, radius, speed))

for frame in range(total_frames):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Hintergrundfarbe setzen
    screen.fill(BACKGROUND_COLOR)

    # Tropfen bewegen und zeichnen
    for drop in drops:
        drop.move()
        drop.draw(screen)
        # Reset Tropfen, wenn sie den Boden erreichen
        if drop.y > HEIGHT + drop.radius:
            drop.y = random.randint(-50, 0)
            drop.x = random.randint(100, WIDTH - 100)

    pygame.display.flip()

    # Screenshot des Frames speichern
    frame_surface = pygame.display.get_surface()
    frame_data = pygame.surfarray.array3d(frame_surface)
    frame_data = frame_data.transpose([1, 0, 2])
    frames.append(frame_data.copy())

    clock.tick(fps)

# Video mit MoviePy erstellen
clip = ImageSequenceClip(frames, fps=fps)
if not os.path.exists('videos'):
    os.makedirs('videos')
clip.write_videofile("videos/water.mp4", codec='libx264')

pygame.quit()
