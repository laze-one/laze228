from pygame import *

back = (200,255,255) #цвет фона (background)

win_width = 600
win_height = 500

window = display.set_mode((win_width, win_height))
display.set_caption("PING-PONG")
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

ball = GameSprite('pingball.png', 200, 200, 4, 70, 70)
kvadrat = GameSprite("kvadrat.png", 30, 200, 5, 20, 120)
kvadrat2 = GameSprite("kvadrat.png", 550, 180, 5, 20, 120)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    ball.update()
    ball.reset()
    kvadrat.update()
    kvadrat.reset()
    kvadrat2.update()
    kvadrat2.reset()
    display.update()
    clock.tick(FPS)