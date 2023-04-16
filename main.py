import pygame

gap = 40
rect_size = 100
width = 1920
height = 1080
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pexeso")
clock = pygame.time.Clock()
running = True
Grid = [[[] for _ in range((width-gap)//(rect_size+gap))] for _ in range((height-gap)//(rect_size+gap))]
for i in range(len(Grid)):
    for j in range(len(Grid[i])):
        Grid[i][j] = [pygame.Rect(gap + j * (rect_size+gap), gap + i * (rect_size+gap), rect_size, rect_size), "blue"]

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    pos = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos 

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    for x in Grid:
        for y in x:
            if pos and y[0].collidepoint(pos):
                y[1] = "red"
            pygame.draw.rect(screen, y[1], y[0])

    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()