import random
import pygame
import pymunk
import pymunk.pygame_util
from tkinter import *
import tkinter as tk

class Ball():
    def __init__(self):
        self.space = pymunk.Space()
        self.space.gravity = (0.0, 0.0)
        self.licznik = 0
        self.ile = 40 # mozna zmienic zeby uzytkownik podawal
        self.timeForNewBall = 50 # podawane w frame per second czyli dla 120 to 2s mozna zmienic zeby uzytkownik podawal
        self.timeForNewBallZmienny = self.timeForNewBall
        self.FPS = 1.0 / 60.0
        self.speed = 150 # mozna zmienic zeby uzytkownik podawal
        self.screen = pygame.display.set_mode((600, 600))
        self.clock = pygame.time.Clock()
        self.draw_options = pymunk.pygame_util.DrawOptions(self.screen)
        self.board()
        self.balls = []
        self.runn = True
        pygame.init()

    def run(self):
        while self.runn:
            self.space.step(self.FPS)
            self.wylacz()
            self.newBall()
            self.refresh()
            pygame.display.flip()
            self.clock.tick(60)
            pygame.display.set_caption("fps: " + str(self.clock.get_fps()))

    def board(self):
        static_body = self.space.static_body
        static_lines = [
            pymunk.Segment(static_body, (0,0), (0,500), 0.0),
            pymunk.Segment(static_body, (0, 500), (600, 500), 0.0),
            pymunk.Segment(static_body, (600, 500 ), (600,0), 0.0),
            pymunk.Segment(static_body, (600,0), (0,0), 0.0),
        ]
        for line in static_lines:
            line.elasticity = 1
            line.friction = 1
        self.space.add(*static_lines)

    def wylacz(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.runn = False

    def newBall(self):
        self.timeForNewBallZmienny -= 1
        for ball in self.balls:
            ball.body.velocity = ball.body.velocity[0]*abs(self.speed/ball.body.velocity[0]),ball.body.velocity[1]*abs(self.speed/ball.body.velocity[1])
        if self.timeForNewBallZmienny <= 0 and self.licznik <self.ile:
            self.createBall()
            self.licznik+=1
            self.timeForNewBallZmienny = self.timeForNewBall

    def createBall(self):
        mass = 1
        radius = 10
        inertia = pymunk.moment_for_circle(mass, 0, radius, (0, 0))
        body = pymunk.Body(mass, inertia)
        x = random.randint(20,580)
        body.position = x, 300
        body.velocity = self.speed,self.speed
        shape = pymunk.Circle(body, radius, (0, 0))
        shape.elasticity = 1
        shape.friction = 1
        self.space.add(body, shape)
        self.balls.append(shape)


    def refresh(self):
        self.screen.fill(pygame.Color("white"))
        self.space.debug_draw(self.draw_options)





if __name__ == "__main__":
    game = Ball()
    game.run()