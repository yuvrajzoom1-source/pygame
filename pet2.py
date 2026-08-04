import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
pet = pygame.Rect(200, 150, 40, 40)
food = pygame.Rect(100, 100, 20, 20)
font = pygame.font.SysFont("Arial", 36)

running = True
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if not game_over:
        if keys[pygame.K_LEFT]: pet.x -= 5
        if keys[pygame.K_RIGHT]: pet.x += 5
        if keys[pygame.K_UP]: pet.y -= 5
        if keys[pygame.K_DOWN]: pet.y += 5

        if pet.colliderect(food):
            game_over = True

    screen.fill((200, 220, 255))
    if not game_over:
        pygame.draw.rect(screen, (255, 100, 100), pet)
        pygame.draw.rect(screen, (100, 255, 100), food)
    else:
        text = font.render("Food Collected!", True, (0, 0, 0))
        rect = text.get_rect(center=(200, 150))
        screen.blit(text, rect)

    pygame.display