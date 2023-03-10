import pygame
from constants import WIDTH, HEIGHT, ENEMY_SUM, ENEMY_ROW
from game_objects import Enemy
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullets = pygame.sprite.Group()


def music_background():
    pygame.mixer.music.load('game_sounds/background_music.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(loops=-1)


def show_game_over():
    font = pygame.font.Font(None, 150)
    text = font.render("ИГРА ОКОНЧЕНА", True, (255, 0, 0))
    text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.mixer.music.load('game_sounds/gameover.mp3')
    pygame.mixer.music.play()
    pygame.time.delay(3000)
    music_background()


def show_game_win():
    font = pygame.font.Font(None, 200)
    text = font.render("ПОБЕДА!", True, (255, 255, 255))
    text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.mixer.music.load('game_sounds/win.mp3')
    pygame.mixer.music.play()
    pygame.time.delay(4000)
    music_background()


def reset_game_state(enemies, enemy_img):
    enemies.empty()
    for j in range(ENEMY_ROW):
        for i in range(ENEMY_SUM):
            enemy = Enemy(i * 100 + 30 + 50, j * 100 + 30, enemy_img)
            enemies.add(enemy)

    enemy_group = pygame.sprite.Group()
    for enemy in enemies:
        enemy_group.add(enemy)

    bullets.empty()
    bullet_counter = 0
    player_life = 100

    return enemy_group, bullets, bullet_counter, player_life
