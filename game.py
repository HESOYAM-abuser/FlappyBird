import pygame
import random
from time import sleep

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("FLAPPY BIRD")
FPS = 60
BIRD_IMAGE = pygame.image.load('data\\bird_image.png')
BIRD = pygame.transform.scale(BIRD_IMAGE, (50, 50))

def genrate_pipe():
    h = 360
    a = random.randint(10, h - 10)
    b = h - a
    upper_pipe = pygame.Rect(950, 0, 80, a)
    lower_pipe = pygame.Rect(950, 500 - b, 80, b)
    color0 = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    return [upper_pipe, lower_pipe, color0]

def move_pipe(pipes_list):
    if pipes_list != []:
        for pipe in pipes_list:
            pipe[0].x += -1
            pipe[1].x += -1

def draw_pipes(pipes_list):
    for pipe0 in pipes_list:
        pygame.draw.rect(WIN, pipe0[2], pipe0[0])
        pygame.draw.rect(WIN, pipe0[2], pipe0[1])

def draw_backgrounnd(red, pipes_list):
    WIN.fill((255, 255, 255))
    WIN.blit(BIRD, (red.x, red.y))
    if pipes_list != []:
        draw_pipes(pipes_list)
    pygame.display.update()

def delete_pipe(pipes_list):
    for pipe in pipes_list:
        if pipe[0].x <= -80:
            pipes_list.remove(pipe)
    return pipes_list

def border(the_bird):
    if the_bird.y >= 450:
        the_bird.y = 450
    elif the_bird.y <= 0:
        the_bird.y = 0
    else:
        pass

def colide(red, pipes_list):
    for pipe in pipes_list:
        if red.colliderect(pipe[0]):
            return True
        elif red.colliderect(pipe[1]):
            return True
        else:
            pass
    return False

def main():
    time = 0
    red = pygame.Rect(200, 200, 50, 50)
    run = True
    clock = pygame.time.Clock()
    pipes = []
    times = 0
    while run:
        clock.tick(FPS)
        times += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    red.y += -63
        # key_pressed = pygame.key.get_pressed()
        # if key_pressed[pygame.K_SPACE]:
        #     red.y += -30
        red.y += 2
        border(red)
        if times/FPS >= 5.5:
            pipes.append(genrate_pipe())
            pipes = delete_pipe(pipes)
            times = 0
        move_pipe(pipes)
        draw_backgrounnd(red, pipes)
        if colide(red, pipes):
            run = False 
    sleep(5)
    pygame.quit()

if __name__ == "__main__":
    main()