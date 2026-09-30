import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("DODGE // CYBER RUN")

clock = pygame.time.Clock()

font = pygame.font.Font(None, 70)
small_font = pygame.font.Font(None, 35)

high_score = 0


def game():

    global high_score

    player = pygame.Rect(375, 520, 40, 40)
    enemy = pygame.Rect(random.randint(0, 760), -50, 40, 40)

    score = 0
    enemy_speed = 5
    running = True

    stars = []

    for i in range(60):
        stars.append([
            random.randint(0, 800),
            random.randint(0, 600),
            random.randint(1, 3)
        ])

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            player.x -= 7

        if keys[pygame.K_RIGHT]:
            player.x += 7

        if player.x < 0:
            player.x = 0

        if player.x > 760:
            player.x = 760

        enemy.y += enemy_speed

        if enemy.y > 600:

            enemy.y = -50
            enemy.x = random.randint(0, 760)

            score += 1
            enemy_speed += 0.25

        if player.colliderect(enemy):
            running = False

        screen.fill((5, 5, 20))

        # Moving stars
        for star in stars:

            star[1] += star[2]

            if star[1] > 600:
                star[0] = random.randint(0, 800)
                star[1] = 0

            pygame.draw.circle(
                screen,
                (100, 100, 150),
                (star[0], star[1]),
                1
            )

        # Player
        pygame.draw.rect(
            screen,
            (0, 220, 255),
            player
        )

        pygame.draw.rect(
            screen,
            (255, 255, 255),
            player,
            2
        )

        # Enemy
        pygame.draw.rect(
            screen,
            (255, 40, 80),
            enemy
        )

        pygame.draw.rect(
            screen,
            (255, 200, 200),
            enemy,
            2
        )

        # Score
        text = small_font.render(
            "SCORE  " + str(score),
            True,
            (255, 255, 255)
        )

        screen.blit(text, (20, 20))

        pygame.display.update()

        clock.tick(60)

    if score > high_score:
        high_score = score

    return score


# START SCREEN

while True:

    screen.fill((5, 5, 20))

    title = font.render(
        "DODGE // CYBER RUN",
        True,
        (0, 220, 255)
    )

    instruction = small_font.render(
        "PRESS SPACE TO START",
        True,
        (255, 255, 255)
    )

    screen.blit(title, (175, 220))
    screen.blit(instruction, (275, 310))

    pygame.display.update()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                game_started = True

                score = game()

                while True:

                    screen.fill((5, 5, 20))

                    over = font.render(
                        "GAME OVER",
                        True,
                        (255, 40, 80)
                    )

                    score_text = small_font.render(
                        "SCORE: " + str(score),
                        True,
                        (255, 255, 255)
                    )

                    best_text = small_font.render(
                        "BEST: " + str(high_score),
                        True,
                        (0, 220, 255)
                    )

                    restart = small_font.render(
                        "PRESS R TO RESTART",
                        True,
                        (255, 255, 255)
                    )

                    screen.blit(over, (265, 190))
                    screen.blit(score_text, (330, 280))
                    screen.blit(best_text, (330, 320))
                    screen.blit(restart, (270, 390))

                    pygame.display.update()

                    for e in pygame.event.get():

                        if e.type == pygame.QUIT:
                            pygame.quit()
                            quit()

                        if e.type == pygame.KEYDOWN:

                            if e.key == pygame.K_r:
                                break

                            if e.key == pygame.K_ESCAPE:
                                pygame.quit()
                                quit()

                    else:
                        continue

                    break