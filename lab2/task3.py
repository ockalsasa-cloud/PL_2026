import pygame
from pygame.draw import *

pygame.init()

screen = pygame.display.set_mode((800, 600))

# ЦВЕТА
DARK_BROWN = (70,  55,  20)
FLOOR      = (110, 95,  35)
CAT_ORANGE = (200, 100, 40)
CAT_GRAY   = (90,  85,  80)
EAR_PINK   = (220, 150, 120)
GREEN_EYE  = (80,  180, 40)
BLUE_EYE   = (40,  180, 210)
BLACK      = (0,   0,   0)
WHITE      = (255, 255, 255)
LIGHT_BLUE = (170, 220, 230)
WINDOW_F   = (210, 225, 205)
GRAY_BALL  = (140, 140, 145)
GRAY_DARK  = (100, 100, 105)
NOSE_PINK  = (220, 130, 110)


def i(value):
    return int(value)


# ФОН
def draw_wall():
    rect(screen, DARK_BROWN, (0, 0, 800, 270))

def draw_floor():
    rect(screen, FLOOR, (0, 270, 800, 330))

def draw_background():
    draw_wall()
    draw_floor()

# ОКНО
def draw_window(x, y, w=170, h=155):
    hw = w // 2 - 6
    hh = h // 2 - 6

    rect(screen, WINDOW_F, (x, y, w, h))

    rect(screen, LIGHT_BLUE, (x + 4,        y + 4,        hw, hh))
    rect(screen, LIGHT_BLUE, (x + w//2 + 2, y + 4,        hw, hh))
    rect(screen, LIGHT_BLUE, (x + 4,        y + h//2 + 2, hw, hh))
    rect(screen, LIGHT_BLUE, (x + w//2 + 2, y + h//2 + 2, hw, hh))

    rect(screen, WINDOW_F, (x + w//2 - 3, y + 4,      6,     h - 8))
    rect(screen, WINDOW_F, (x + 4,        y + h//2-3, w - 8, 6    ))

def draw_all_windows():
    draw_window(30,  25)
    draw_window(270, 25)
    draw_window(530, 25)



# ЧАСТИ КОТА


def draw_cat_body(x, y, s, color):
    ellipse(screen, color,
            (i(x + 10*s), i(y - 15*s), i(320*s), i(110*s)))

def draw_cat_paws(x, y, s, color):
    ellipse(screen, color,
            (i(x - 50*s), i(y + 60*s), i(80*s), i(26*s)))
    ellipse(screen, color,
            (i(x + 20*s), i(y + 60*s), i(80*s), i(26*s)))
    ellipse(screen, color,
            (i(x + 280*s), i(y + 58*s), i(70*s), i(28*s)))

def draw_cat_tail(x, y, s, color):
    arc(screen, color,
        (i(x + 290*s), i(y - 20*s), i(70*s), i(90*s)),
        0, 3.14, max(3, i(18*s)))

def draw_cat_head(x, y, s, color):
    circle(screen, color, (x, y), i(55*s))

def draw_cat_ears(x, y, s, color):
    # Левое ухо
    polygon(screen, color, [
        (i(x - 32*s), i(y - 40*s)),
        (i(x - 18*s), i(y - 68*s)),
        (i(x +  4*s), i(y - 42*s))
    ])
    polygon(screen, EAR_PINK, [
        (i(x - 27*s), i(y - 42*s)),
        (i(x - 18*s), i(y - 60*s)),
        (i(x +  1*s), i(y - 44*s))
    ])
    # Правое ухо
    polygon(screen, color, [
        (i(x +  8*s), i(y - 42*s)),
        (i(x + 26*s), i(y - 68*s)),
        (i(x + 40*s), i(y - 40*s))
    ])
    polygon(screen, EAR_PINK, [
        (i(x + 11*s), i(y - 43*s)),
        (i(x + 26*s), i(y - 60*s)),
        (i(x + 36*s), i(y - 41*s))
    ])

def draw_cat_eyes(x, y, s, eye_color):
    er  = i(15*s)
    th  = max(1, i(2*s))

    for side in [-18, 18]:
        cx = i(x + side*s)
        cy = i(y + 5*s)

        circle(screen, WHITE,     (cx, cy), er)
        circle(screen, eye_color, (cx, cy), i(12*s))
        ellipse(screen, BLACK, (
            i(cx - 4*s), i(cy - 9*s),
            i(8*s),      i(19*s)))
        circle(screen, BLACK, (cx, cy), er, th)

def draw_cat_nose_mouth(x, y, s):
    polygon(screen, NOSE_PINK, [
        (i(x - 4*s), i(y + 20*s)),
        (i(x + 4*s), i(y + 20*s)),
        (x,          i(y + 27*s))
    ])
    th = max(1, i(2*s))
    line(screen, BLACK,
         (x, i(y + 27*s)), (i(x - 7*s), i(y + 33*s)), th)
    line(screen, BLACK,
         (x, i(y + 27*s)), (i(x + 7*s), i(y + 33*s)), th)



# ГЛАВНАЯ ФУНКЦИЯ КОТА


def draw_cat(x, y, scale=1.0, color=CAT_ORANGE, eye_color=GREEN_EYE):

    draw_cat_body      (x, y, scale, color)
    draw_cat_paws      (x, y, scale, color)
    draw_cat_tail      (x, y, scale, color)
    draw_cat_head      (x, y, scale, color)
    draw_cat_ears      (x, y, scale, color)
    draw_cat_eyes      (x, y, scale, eye_color)
    draw_cat_nose_mouth(x, y, scale)



# КЛУБОК


def draw_ball(cx, cy, r=30):
    """
    cx, cy — центр клубка
    r      — радиус
    """
    ellipse(screen, GRAY_BALL, (cx-r, cy-r//2, r*2, r))

    # Линии намотки
    ellipse(screen, GRAY_DARK, (cx-r+4,  cy-r//2+2, r*2-8,  r-5),  2)
    ellipse(screen, GRAY_DARK, (cx-r+9,  cy-r//2+5, r*2-18, r-10), 2)
    ellipse(screen, GRAY_DARK, (cx-r+14, cy-r//2+8, r*2-28, r-16), 2)

    # Нитка
    line(screen, GRAY_DARK, (cx-r, cy), (cx-r-20, cy-8), 1)

def draw_all_balls():
    draw_ball(190, 350, r=24)   # левый верхний
    draw_ball(370, 460, r=50)   # большой центральный
    draw_ball(410, 535, r=38)   # средний центр низ
    draw_ball(570, 445, r=27)   # правый средний
    draw_ball(650, 515, r=21)   # маленький правый
    draw_ball(90,  495, r=19)   # маленький левый низ



# ГРУППЫ КОТОВ


def draw_big_cats():
    """Два больших кота"""
    # Рыжий — правый верхний
    draw_cat(480, 315, scale=1.0,  color=CAT_ORANGE, eye_color=GREEN_EYE)
    # Серый — левый, чуть меньше чтобы не перекрывал всё
    draw_cat(195, 405, scale=0.82, color=CAT_GRAY,   eye_color=BLUE_EYE)

def draw_small_cats():
    """Маленькие коты разбросаны по полу"""
    # Рыжие маленькие
    draw_cat(88,  355, scale=0.28, color=CAT_ORANGE, eye_color=GREEN_EYE)
    draw_cat(625, 420, scale=0.28, color=CAT_ORANGE, eye_color=GREEN_EYE)
    draw_cat(505, 465, scale=0.28, color=CAT_ORANGE, eye_color=GREEN_EYE)
    draw_cat(655, 490, scale=0.28, color=CAT_ORANGE, eye_color=GREEN_EYE)
    # Серые маленькие
    draw_cat(128, 525, scale=0.25, color=CAT_GRAY, eye_color=BLUE_EYE)
    draw_cat(725, 540, scale=0.25, color=CAT_GRAY, eye_color=BLUE_EYE)




def draw_scene():
    draw_background()   # 1 Фон
    draw_all_windows()  # 2 Окна
    draw_big_cats()     # 3 Большие коты
    draw_small_cats()   # 4 Маленькие коты
    draw_all_balls()    # 5 Клубки




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_scene()
    pygame.display.flip()

pygame.quit()