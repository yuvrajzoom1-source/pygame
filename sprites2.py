import pygame

pygame.init()
win = pygame.display.set_mode((500, 300))
clock = pygame.time.Clock()

player = pygame.Rect(50, 50, 40, 40)

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

    if player.left < 0:
        player.left = 0
        color = (255, 0, 0)
    elif player.right > 500:
        player.right = 500
        color = (0, 255, 0)
    elif player.top < 0:
        player.top = 0
        color = (0, 0, 255)
    elif player.bottom > 300:
        player.bottom = 300
        color = (255, 255, 0)
    else:
        color = (255, 255, 255)

    win.fill((30, 30, 30))
    pygame.draw.rect(win, color, player)          # solid
    pygame.draw.rect(win, (200, 200, 200), player, 2)  # outline
    pygame.display.update()
    clock.tick(30)

pygame.quit()
