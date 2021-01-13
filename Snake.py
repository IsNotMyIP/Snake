import pygame
from random import randrange
import neat
#######
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
scores =0
width, height = 1200, 700
title = "Python.io"
# background is set to black by default, pygame interprets color in RGB (red, green, blue) values
background = (0, 0, 0)
clock = pygame.time.Clock()


# initializing main pygame window
win = pygame.display.set_mode((width, height))
pygame.display.set_caption(title)

##############
#  CODIGO NAT ##
##############


















# #############

class Game:
    def __init__(self):
        pygame.init()
        #Sprites
        self.snake = Snake(width/2, height/2, "white")
        self.food = Food()
        self.score = Score()
        self.left_bound = Boundary(25, 75, 5, 600)
        self.right_bound = Boundary(1175, 75, 5, 605)
        self.top_bound = Boundary(25, 75, 1150, 5)
        self.down_bound = Boundary(25, 675, 1150, 5)

        self.running = True
        self.sprite_list = pygame.sprite.Group()
        self.boundaries_list = pygame.sprite.Group()
        self.sprite_list.add(self.snake)
        self.sprite_list.add(self.food)
        self.sprite_list.add(self.score)

        self.boundaries_list.add(self.left_bound)
        self.boundaries_list.add(self.right_bound)
        self.boundaries_list.add(self.down_bound)
        self.boundaries_list.add(self.top_bound)

    def play(self):
        scores = 0
        while self.running:
            # Look at every event in the queue
            for event in pygame.event.get():
                # Did the user hit a key?
                if event.type == KEYDOWN:
                    # Was it the Escape key? If so, stop the loop.
                    if event.key == K_ESCAPE:
                        self.running = False
                        # Did the user click the window close button? If so, stop the loop.
                elif event.type == QUIT:
                    self.running = False
            # Checking cols
            if pygame.sprite.collide_rect(self.snake, self.food):
                self.food.kill()
                self.rand_Food()
                self.score.getPoint()

            if pygame.sprite.spritecollideany(self.snake, self.boundaries_list):
                pygame.quit()



            win.fill(background)

            self.sprite_list.update()
            self.boundaries_list.update()
            self.sprite_list.draw(win)
            self.boundaries_list.draw(win)
            pressed_keys = pygame.key.get_pressed()

            self.control(pressed_keys)
            win.blit(self.score.surface,( 1000, 25))
            pygame.display.flip()
            pygame.display.update(self.score)
            clock.tick(15)

    def control(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.snake.set_acc(0, -10)
        elif pressed_keys[K_DOWN]:
            self.snake.set_acc(0, +10)
        elif pressed_keys[K_LEFT]:
            self.snake.set_acc(-10, 0)
        elif pressed_keys[K_RIGHT]:
            self.snake.set_acc(10, 0)

    def rand_Food(self):

        self.food = Food()
        self.sprite_list.add(self.food)


    def score(self):
        font = pygame.font.Font("roboto", 12)
        text_surface = font.render("Score: ", True, "green")
        text_rect = text_surface.get_rect()
        text_rect.midtop =(500,400)

    def render(self):
        pygame.display.update()
        pygame.display.update()

class Snake(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.color = color
        #Definimos las coordenadas del objeto
        self.x = x
        self.y = y
        #Lo utilizemos en el movimiento del objeto, teniendo así su dirección y actualizándolo cada frame si es necesario
        self.acc_x = 0
        self.acc_y = 0
        self.last_key = "r"
        #Necesarios
        self.image = pygame.Surface((10, 10))
        self.image.fill(self.color)
        self.rect = pygame.Rect(x,y, 10,10)

    def draw(self):
        pass

    def drawTail(self, surface):
        for i in range(0,self.length):
            surface.blit(self.image,(self.x[i],self.y[i]))

def set_acc(self,x,y):
        self.acc_y = y
        self.acc_x = x

    def move(self, x, y, r):
        self.acc_x += x
        self.acc_y += y
        self.last_key = r

    def update(self):
        self.rect.move_ip(self.acc_x, self.acc_y)
    """
        if (self.acc_x != 0) or (self.acc_y != 0):
            self.x += self.acc_x
            self.y += self.acc_y
            self.rect.move_ip(self.acc_x, self.acc_y)
            self.acc_x = 0
            self.acc_y = 0
        else:
            if self.last_key == "u":
                self.acc_y = -10
            elif self.last_key == "d":
                self.acc_y = 10
            elif self.last_key == "r":
                self.acc_x = 10
            elif self.last_key == "l":
                self.acc_x = -10
    """
    def draw(self, win):
        win.blit(self.image, self.rect)

    def render(self):
        head = pygame.Rect(30, 30, 60, 60)
        print("Printando")


class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        print("Normal")

        # Definimos las coordenadas del objeto
        self.x = randrange(51, 1148)
        self.y = randrange(76, 674)

        # Necesarios
        self.image = pygame.Surface((10, 10))
        self.image.fill("green")
        self.rect = pygame.Rect(self.x, self.y, 10, 10)


class Score(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.pts = 0
        self.font = pygame.font.Font(pygame.font.match_font("roboto"), 20)
        self.surface = self.font.render("Score: {}".format(scores), True, "green")
        self.image = pygame.Surface((1000, 75))
        self.rect = self.surface.get_rect()
        self.rect.midtop =(1000, 75)

    def update(self):
        self.image.fill("black")
        self.surface = self.font.render("Score: {}".format(self.pts), True, "green")
        self.image = pygame.Surface((1000, 75))
        self.rect = self.surface.get_rect()
        self.rect.midtop =(1000, 75)

    def getPoint(self):
        self.pts += 1


class Boundary(pygame.sprite.Sprite):
    def __init__(self, x, y, width, length):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, length)
        self.image = pygame.Surface((width, length))
        self.image.fill("white")


class IASnake(pygame.sprite.Sprite):
    def __init__(self, g, config):
        self.nets = neat.nn.FeedForwardNetWork(g, config)




def main():
    game = Game()
    game.play()

main()