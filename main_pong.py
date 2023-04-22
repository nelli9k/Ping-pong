from pygame import*
from time import time as timer

background = "background.png"
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
        display.update()
    time.delay(50)