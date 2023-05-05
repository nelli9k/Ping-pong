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

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y = self.rect.y - self.speed
        if keys[K_s] and self.rect.y < 300:
            self.rect.y = self.rect.y + self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y = self.rect.y - self.speed
        if keys[K_DOWN] and self.rect.y < 300:
            self.rect.y = self.rect.y + self.speed

ball = GameSprite(ball, 200, 200, 50, 50, 15)
tenis_rocket = Player(tennis_r, 50, 200, 75, 200, 15)
tenis_rocket2 = Player(tennis_r, 550, 200, 75, 200, 15)
window = display.set_mode((700,500))
display.set_caption("Shooter")
background = transform.scale(image.load(background), (700,500))

speed_ball_x = 15
speed_ball_y = 15
caught = 0
caught2 = 0

finish = False
run = True

font.init()
font1 = font.SysFont("Arial", 25)
font = font.SysFont("Arial", 70)
lost1 = font.render("PLAYER 1 LOST", True, (0,0,128))
lost2 = font.render("PLAYER 2 LOST", True, (0,0,128))

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:

        ball.rect.x = ball.rect.x + speed_ball_x
        ball.rect.y = ball.rect.y + speed_ball_y

        if ball.rect.y >= 500-50 or ball.rect.y <= 0:
            speed_ball_y = speed_ball_y * -1
            

        if sprite.collide_rect(tenis_rocket, ball):
            speed_ball_x = speed_ball_x * -1
            caught = caught + 1
            
        if sprite.collide_rect(tenis_rocket2, ball):
            speed_ball_x = speed_ball_x * -1
            caught2 = caught2 + 1
        
        window.blit(background, (0,0))
        counter1 = font1.render("Bounced by 1player: " + str(caught), True, (0,0,128))
        window.blit(counter1, (10, 20))

        counter1 = font1.render("Bounced by 2player : " + str(caught2), True, (0,0,128))
        window.blit(counter1, (450, 20))
        
        if caught == 15 and caught2 < 15:
            win1 = font.render("PLAYER 1 WON", True, (0,0,128))
            window.blit(win1, (125, 200))
            finish = True

        if caught2 == 15 and caught < 15:
            win2 = font.render("PLAYER 2 WON", True, (0,0,128))
            window.blit(win2, (125, 200))
            finish = True
       
        if ball.rect.x <= 0:
            window.blit(lost1, (125, 200))
            finish = True
        
        if ball.rect.x == 650:
            window.blit(lost2, (125, 200))
            finish = True

        ball.reset()
        tenis_rocket.update()
        tenis_rocket.reset()
        tenis_rocket2.update_r()
        tenis_rocket2.reset()

        display.update()
    time.delay(50)