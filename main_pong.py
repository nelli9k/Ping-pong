from pygame import*
from time import time as timer

background = "background.png"
ball = "ball.png"
tennis_r = "tennis_r.png"
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, sizex, sizey, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (sizex, sizey))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

ball = GameSprite(ball, 200, 200, 50, 50, 0)
tenis_rocket = GameSprite(tennis_r, 50, 200, 75, 200, 0)
tenis_rocket2 = GameSprite(tennis_r, 550, 200, 75, 200, 0)
window = display.set_mode((700,500))
display.set_caption("Shooter")
background = transform.scale(image.load(background), (700,500))

finish = False
run = True

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        window.blit(background, (0,0))

        ball.reset()
        tenis_rocket.reset()
        tenis_rocket2.reset()

        display.update()
    time.delay(50)