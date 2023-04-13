import pygame
pygame.init()
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("RED CIRCLE")
done = True
color=(255,0,0)
x=250
y=250
speed=20
clock=pygame.time.Clock()
while done:
    screen.fill((251,251,251))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=False
    pressed=pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y>speed+20:
        y-=speed
    if pressed[pygame.K_DOWN]and y<500-speed-20:
        y+=speed
    if pressed[pygame.K_RIGHT] and x<500-speed-25:
        x+=speed
    if pressed[pygame.K_LEFT] and x>speed+25:
        x-=speed
    pygame.draw.circle(screen,color,(x,y),25)
    pygame.display.flip()
    clock.tick(30)