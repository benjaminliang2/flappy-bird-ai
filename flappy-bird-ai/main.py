import os
import pygame
import neat
import time
pygame.font.init()

from bird import Bird
from base import Base
from pipe import Pipe 

WIN_WIDTH = 500
WIN_HEIGHT = 800

BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("flappy-bird-ai", "imgs", "bg.png")))

STAT_FONT = pygame.font.SysFont("comicsans", 50)

def draw_window(win, bird, pipes, base, score):
    win.blit(BG_IMG, (0,0))
    text= STAT_FONT.render("Score:" + str(score) , 1, (255,255,255))
    win.blit(text, (WIN_WIDTH - 10 -text.get_width(), 10))
    for pipe in pipes: 
        pipe.draw(win)
    base.draw(win)
    bird.draw(win)
    pygame.display.update()


def main():
    bird = Bird(230,350)
    base = Base(730)
    pipes = [Pipe(700)]
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()
    run = True
    score = 0
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # bird.move()
        base.move()
        add_pipe = False
        rem = []
        for pipe in pipes:
            if pipe.collide(bird):
                pass
            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                rem.append(pipe)
            if not pipe.passed and pipe.x < bird.x: 
                pipe.passed = True
                add_pipe = True
            pipe.move()
        if add_pipe: 
            score += 1
            pipes.append(Pipe(700))
        for pipe in rem:
            pipes.remove(pipe)

        if bird.y + bird.img.get_height() >= 730:
            pass
        draw_window(win, bird, pipes, base, score)

    pygame.quit()
    quit()

main()