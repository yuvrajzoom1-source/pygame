import pygame

pygame.init()
win = pygame.display.set_mode((500, 300))
clock = pygame.time.Clock()

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    win.fill((50, 100, 150))
    pygame.display.update()
    clock.tick(30)

pygame.quit()
