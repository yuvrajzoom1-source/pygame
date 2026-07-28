import pygame

pygame.init()
win = pygame.display.set_mode((500, 300))
clock = pygame.time.Clock()

player = pygame.Rect(50, 50, 40, 40)
box = pygame.Rect(200, 150, 40, 40)

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.y -= 4
    if keys[pygame.K_DOWN]:
        player.y += 4
    if keys[pygame.K_LEFT]:
        player.x -= 4
    if keys[pygame.K_RIGHT]:
        player.x += 4

    win.fill((30, 30, 30))
    pygame.draw.rect(win, (255, 0, 0), player)
    pygame.draw.rect(win, (0, 255, 0), box)
    pygame.display.update()
    clock.tick(30)

pygame.quit()
