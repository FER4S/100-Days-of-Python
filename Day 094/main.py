from turtle import Screen
import winsound
from random import randint

from scoreboard import Scoreboard
from player import Player
from invaders import Invaders
from bullet import Bullet


def fire_bullet():
    x, y = player.xcor(), player.ycor()
    bullet.fire(x, y + 15)
    winsound.PlaySound('sounds/fire.wav', winsound.SND_ASYNC)


screen = Screen()
screen.setup(700, 700)
screen.title('Space Invaders')
screen.bgcolor('black')
screen.tracer(0)

scoreboard = Scoreboard()

player = Player()
bullet = Bullet()
invaders = Invaders()

screen.listen()
screen.onkeypress(player.move_left, 'a')
screen.onkeypress(player.move_right, 'd')
screen.onkeypress(fire_bullet, 'space')

counter = 1
playing = True
while playing:
    screen.update()

    # moving invaders
    if counter < 200:
        invaders.move_h('R')
    elif counter >= 200:
        invaders.move_h('L')
    counter += 1
    if counter > 400:
        counter = 1
        invaders.move_v(scoreboard.level)

    # moving the bullets
    bullet.bullets_move()

    # checking if the bullet out of the screen or it hits an invader
    for bul in bullet.bullets:
        if bul.ycor() > 300:
            bullet.bullets.remove(bul)
            bul.hideturtle()
        for invader in invaders.invaders:
            if invader.distance(bul) < 20:
                invader.hideturtle()
                invaders.invaders.remove(invader)
                bullet.bullets.remove(bul)
                bul.hideturtle()
                scoreboard.score_up()
                winsound.PlaySound('sounds/destroy.wav', winsound.SND_ASYNC)

    # invaders firing
    for invader in invaders.invaders:
        if randint(0, 4000) in range(1):
            bullet.invaders_fire(invader.xcor(), invader.ycor())

    # check the bullets of the invaders
    for bul in bullet.invaders_bullets:
        if bul.ycor() < -300:
            bul.hideturtle()
            bullet.invaders_bullets.remove(bul)
        if bul.distance(player) < 20:
            winsound.PlaySound('sounds/die.wav', winsound.SND_ASYNC)
            scoreboard.life_loss()
            player.goto(0, -270)
            bullet.invaders_bullets.remove(bul)
            bul.hideturtle()

    # check if lvl up
    if not invaders.invaders:
        scoreboard.level_up()
        invaders.create_invaders()
        counter = 1
        winsound.PlaySound('sounds/lvl_up.wav', winsound.SND_ASYNC)

        for bul in bullet.bullets:
            bul.hideturtle()
            bullet.bullets.remove(bul)
        for bul in bullet.invaders_bullets:
            bul.hideturtle()
            bullet.invaders_bullets.remove(bul)

    # check if game is over
    if scoreboard.lives < 0:
        scoreboard.game_over()
        winsound.PlaySound('sounds/game_over.wav', winsound.SND_ASYNC)
        playing = False
    for invader in invaders.invaders:
        if invader.distance(player) < 30 or invader.ycor() < -280:
            scoreboard.game_over()
            winsound.PlaySound('sounds/game_over.wav', winsound.SND_ASYNC)
            playing = False

screen.exitonclick()
