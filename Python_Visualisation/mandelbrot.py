import pygame
import sys
import numpy as np

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mandelbrot Set Visualisation")

# Set constants
maxIteration = 16
scalers = {
    'x': (-2.00, 0.47),
    'y': (-1.12, 1.12)
}

# Function to scale a value between new constraints
def scale(value, old_min, old_max, new_min, new_max):
    return ((value - old_min) / (old_max - old_min)) * (new_max - new_min) + new_min

# Function to map iteration count to a color
def get_color(iteration, max_iteration):
    if iteration == max_iteration:
        return (0, 0, 0)  # Black for points inside the Mandelbrot set
    else:
        color_value = int(255 * iteration / max_iteration)
        return (color_value, 255 - color_value, max_iteration - iteration) 



# Create a numpy array for the screen
pixels = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
def updateScreen():
    for i in range(WIDTH):
        for j in range(HEIGHT):
            x0 = scale(i, 0, WIDTH, scalers['x'][0], scalers['x'][1])
            y0 = scale(j, 0, HEIGHT, scalers['y'][0], scalers['y'][1])
            x = 0.0
            y = 0.0
            iteration = 0
            while (x**2 + y**2 <= 4 and iteration < maxIteration):
                xtemp = x**2 - y**2 + x0
                y = 2 * x * y + y0
                x = xtemp
                iteration += 1
            color = get_color(iteration, maxIteration)
            pixels[j, i] = color  # Update the numpy array

updateScreen()
pygame.surfarray.blit_array(screen, np.transpose(pixels, (1, 0, 2)))
pygame.display.flip()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()
sys.exit()
