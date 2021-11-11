import pygame
import random

screen_size = (360, 500)
screen = pygame.display.set_mode(screen_size)

background = pygame.image.load('background.png')
Heart = pygame.image.load('Chicken.png')
user = pygame.image.load('user.png')

pygame.font.init()

clock = pygame.time.Clock()
keep_alive = True


def random_num():
    return -1 * random.randint(100, 1500)


y_positions = [random_num(), random_num(), 0]
move = 150
global score
score = 0


def display_score(score):
    font = pygame.font.SysFont('Comic Sans MS', 25)
    img_always = font.render('if score>-120, we loose :(', True, (0, 0, 255))
    if score < -120:
        img = font.render('Not Bad :-)', True, (255, 0, 0))
        print('NOT BAD, YOU PLAYED WELL !!')
        exit()
    else:
        score_txt = 'score : ' + str(score)
        if score > 0:
            img = font.render(score_txt, True, (0, 255, 0))
        else:
            img = font.render(score_txt, True, (255, 0, 0))
    return screen.blit(img, [10, 10]), screen.blit(img_always, [135, 10])


def increment(ind):
    global score
    if y_positions[ind] > 500:
        y_positions[ind] = random_num()
        score = score + 5
        print(score)
    else:
        y_positions[ind] = y_positions[ind] + 5


def crushed(ind):
    global score
    score = score - 20
    print('Crushed with chicken :-', ind)
    print(score)
    y_positions[ind] = random_num()


while keep_alive:
    pygame.event.get()

    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT] and move < 279:
        move = move + 10
    elif key[pygame.K_LEFT] and move > 5:
        move = move - 10

    increment(0)
    increment(1)
    increment(2)

    screen.blit(background, [0, 0])
    screen.blit(Heart, [30, y_positions[0]])
    screen.blit(Heart, [140, y_positions[1]])
    screen.blit(Heart, [270, y_positions[2]])
    screen.blit(user, [move, 423])

    if y_positions[0] > 430 and move < 70:
        crushed(0)

    if y_positions[1] > 430 and move < 210 and move > 70:
        crushed(1)

    if y_positions[2] > 430 and move > 200:
        crushed(2)
    display_score(score)
    pygame.display.update()
    clock.tick(60)
