from pygame import *
window = display.set_mode((700, 500))
display.set_caption('Догонялки')
background = transform.scale(image.load('background.png'), (700, 500))

sprite1 = transform.scale(
    image.load('background1.jpg'),
    (100, 100)
)
sprite2 = transform.scale(
    image.load('sprite2.png'),
    (100, 100)
)
sprite3 = transform.scale(
    image.load('ауцув.png'),
    (100, 100)
)
sprite4 = transform.scale(
    image.load('а.pngp'),
    (100, 100)
)
clock = time.Clock()
FPS = 60

x1 = 150
y1 = 250

x2 = 450
y2 = 400

x3 = 600
y3 = 100

x4 = 300
y4 = 120

game = True
while game:
    keys_pressed = key.get_pressed()
    if keys_pressed[K_UP] and y1 > 0:
        y1 -= 10

    if keys_pressed[K_DOWN] and y1 < 395:
        y1 += 10
    
    if keys_pressed[K_LEFT] and x1 > 0:
        x1 -= 10

    if keys_pressed[K_RIGHT] and x1 < 600:
        x1 += 10

    if keys_pressed[K_w] and y2 > 0:
        y2 -= 10

    if keys_pressed[K_s] and y2 < 395:
        y2 += 10
    
    if keys_pressed[K_a] and x2 > 0:
        x2 -= 10

    if keys_pressed[K_d] and x2 < 600:
        x2 += 10

    if keys_pressed[K_1] and y3 > 0:
        y3 -= 10

    if keys_pressed[K_2] and y3 < 395:
        y3 += 10
    
    if keys_pressed[K_3] and x3 > 0:
        x3 -= 10

    if keys_pressed[K_4] and x3 < 600:
        x3 += 10

    if keys_pressed[K_5] and y4 > 0:
        y4 -= 10

    if keys_pressed[K_6] and y4 < 395:
        y4 += 10
    
    if keys_pressed[K_7] and x4 > 0:
        x4 -= 10

    if keys_pressed[K_8] and x4 < 600:
        x4 += 10
    
    otrisovka1 = True
    otrisovka2 = True
    otrisovka3 = True
    otrisovka4 = True

    if keys_pressed[K_SPACE]:
        otrisovka1 = False

    if keys_pressed[K_SPACE]:
        otrisovka2 = False

    if keys_pressed[K_SPACE]:
        otrisovka3 = False

    if keys_pressed[K_SPACE]:
        otrisovka4 = False

    window.blit(background, (0, 0))
    if otrisovka1 == True:
        window.blit(sprite1, (x1, y1))
    if otrisovka2 == True:   
        window.blit(sprite2, (x2, y2))
    if otrisovka3 == True:
        window.blit(sprite3, (x3, y3))
    if otrisovka4 == True:
        window.blit(sprite4, (x4, y4))


    for e in event.get():
        if e.type == QUIT:
            game = False
    clock.tick(FPS)
    display.update()
