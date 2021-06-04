import pygame
import pymunk
import random
pygame.init()

display = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
space = pymunk.Space()
FPS = 50

def convert_coordinates(point):
    return int(point[0]), 600-int(point[1])

class Ball():

    def __init__(self,x,y,vx,vy):
        self.body = pymunk.Body()
        self.body.position = x,y
        self.body.velocity =vx,vy#100*random.uniform(-1,1),100*random.uniform(-1,1)# random.uniform(-400,400),random.uniform(-400,400)
        self.shape = pymunk.Circle(self.body,10)
        self.shape.elasticity = 1
        self.shape.density = 1
        #self.shape.collision_type = 4
        space.add(self.body,self.shape)
        #print(str(self.body.position[0])+"  "+ str(self.body.position[1]))
    def draw(self):
        pygame.draw.circle(display, (255,0,0),convert_coordinates(self.body.position),10)

    def _add_static_scenery(self) -> None:
        """
        Create the static bodies.
        :return: None
        """
        static_body = space.static_body
        static_lines = [
            pymunk.Segment(static_body, (100, 100), (100, 500), 0.0),
            pymunk.Segment(static_body, (100, 500), (500, 500), 0.0),
            pymunk.Segment(static_body, (500, 500), (500, 100), 0.0),
            pymunk.Segment(static_body, (500, 100), (100, 100), 0.0),
        ]
        for line in static_lines:
            line.elasticity = 0.95
            line.friction = 0.9
        space.add(*static_lines)
def collide(arbiter,space,data):
    print("hello")


def game():
    vx, vy = 100 * random.uniform(-1, 1), 100 * random.uniform(-1, 1)
    balls = [Ball(random.randint(0,600),random.randint(0,600),vx,vy) for i in range(10)]
    #balls = [Ball(10,10, vx, vy) for i in range(1)]
    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return
        display.fill((255,255,0))
        [ball.draw() for ball in balls]
        #print(str(balls[0].body.position[0])+"  "+ str(balls[0].body.position[1]))
        for ball in balls:
            print(str(ball.body.position[0]) + " Y " + str(ball.body.position[1]))


            if ball.body.position[0] < 0 :
                ball = Ball(ball.body.position[0],ball.body.position[1],ball.body.velocity[0]*(-1),ball.body.velocity[1])
                ball.draw()
                #ball.body.velocity *= -1
            elif ball.body.position[0] > 600:
                ball = Ball(ball.body.position[0], ball.body.position[1], ball.body.velocity[0] * (-1),ball.body.velocity[1])
                ball.draw()
            elif ball.body.position[1] < 0:
                ball = Ball(ball.body.position[0], ball.body.position[1], ball.body.velocity[0],ball.body.velocity[1] * -1)
                ball.draw()
                #ball.body.velocity.y *= -1
            elif ball.body.position[1] > 600:
                ball = Ball(ball.body.position[0], ball.body.position[1], ball.body.velocity[0],ball.body.velocity[1] * -1)
                ball.draw()
        pygame.display.update()
        clock.tick(FPS)
        space.step(1/FPS)

game()
pygame.quit()