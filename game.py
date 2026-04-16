import pygame
import random
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Game")


player_img = pygame.image.load("player.png")
player_img = pygame.transform.scale(player_img, (70, 70))
background_img = pygame.image.load("background.png")
background_img = pygame.transform.scale(background_img, (800, 600))
point_img = pygame.image.load("point.png")
point_img = pygame.transform.scale(point_img, (70, 70))

player_x = 270
player_y = 270
player_speed = 6

lasers = []
for i in range(5):
    laser_x = random.randint(800, 1200)
    laser_y = random.randint(0, 550)
    lasers.append([laser_x, laser_y])


player_speed = 6
laser_width = 200
laser_height = 15
laser_speed = 5

points = []
for i in range(3):
    x = random.randint(800, 1200)
    y = random.randint(0, 550)
    points.append([x, y])



score = 0
font = pygame.font.SysFont(None, 40)

game_over = False

run = True
clock = pygame.time.Clock()

while run:
    clock.tick(60)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and game_over:
                player_x = 100
                player_y = 250
                score = 0
                lasers = []
                for i in range(5):
                    laser_x = random.randint(800, 1200)
                    laser_y = random.randint(0, 550)
                    lasers.append([laser_x, laser_y])
                points = []
                for i in range(3):
                    x = random.randint(800, 1200)
                    y = random.randint(0, 550)
                    points.append([x, y])
                game_over = False

    if game_over:
        laser_width = False
        laser_height = False

    
    if not game_over:

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player_x -= player_speed
        if keys[pygame.K_d]:
            player_x += player_speed
        if keys[pygame.K_s]:
            player_y += player_speed
        if keys[pygame.K_w]:
            player_y -= player_speed

        player_rect = pygame.Rect(player_x, player_y, 80, 80)

        for laser in lasers:
            laser_rect = pygame.Rect(laser[0], laser[1], laser_width, laser_height)
            if player_rect.colliderect(laser_rect):
                game_over = True

        for point in points:
            point[0] -= 5

        if player_x < 0:
            player_x = 0
        if player_x > 800 - 80:
            player_x = 800 - 80
        if player_y < 0:
            player_y = 0
        if player_y > 600 - 80:
            player_y = 600 - 80


    laser_speed = 5 + score // 500

    for laser in lasers:
        laser[0] -= laser_speed

    for point in points:
        if point[0] < -40:
            point[0] = random.randint(800, 1200)
            point[1] = random.randint(0, 550)

    for laser in lasers:
        if laser[0] < -80:
            laser[0] = random.randint(800, 1200)
            laser[1] = random.randint(0, 550)
    

    for point in points:
        point_rect = pygame.Rect(point[0], point[1], 40, 40)
        if player_rect.colliderect(point_rect):
            score += 1
            point[0] = random.randint(800, 1200)
            point[1] = random.randint(0, 550)

    screen.blit(background_img, (0, 0))
    screen.blit(player_img, (player_x, player_y))

    for point in points:
        
        if game_over:
            points.remove(point)
            
        screen.blit(point_img, (point[0], point[1]))

    for laser in lasers:
        
        if game_over:
            lasers.remove(laser)
            
        pygame.draw.rect(screen, (255, 0, 0), (laser[0], laser[1], laser_width, laser_height))

    score_text = font.render("Score: " + str(score), True, (255, 250, 250))
    screen.blit(score_text, (10, 10))

    if game_over:
        game_over_text = font.render("Game Over!", True, (255, 0, 0))
        score_text = font.render("Final Score: " + str(score), True, (255, 255, 255))
        restart_text = font.render("Press R to Restart", True, (255, 255, 255))
        screen.blit(game_over_text, (280, 230))
        screen.blit(score_text, (280, 270))
        screen.blit(restart_text, (280, 310))

    
    pygame.display.update()

pygame.quit()
