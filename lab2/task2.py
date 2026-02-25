import pygame
from pygame.draw import *

pygame.init()

screen = pygame.display.set_mode((630, 480))
#ЦВЕТА
DARK_GREEN  = (61,  70,  20)   # стена
BROWN_FLOOR = (101, 81,  30)   # пол
CAT_BROWN   = (180, 90,  40)   # тело кота
CAT_DARK    = (150, 70,  25)   # тёмные детали кота
EAR_PINK    = (210, 140, 110)  # внутри уха
GREEN_EYE   = (80,  180, 40)   # зелёный глаз
BLACK       = (0,   0,   0)
WHITE       = (255, 255, 255)
LIGHT_BLUE  = (180, 225, 235)  # стекло окна
WINDOW_WHITE= (220, 230, 230)  # рамка окна
GRAY        = (140, 140, 145)  # клубок
GRAY_DARK   = (100, 100, 105)  # линии на клубке
NOSE_PINK   = (220, 130, 110)  # нос

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # 1. ФОН
    # Тёмно-зелёная стена
    rect(screen, DARK_GREEN, (0, 0, 630, 260))

    # Коричневый пол
    rect(screen, BROWN_FLOOR, (0, 260, 630, 220))
    # 2. ОКНО

    # Внешняя рамка окна
    rect(screen, WINDOW_WHITE, (370, 30, 220, 190))

    # Четыре стекла
    rect(screen, LIGHT_BLUE, (378, 38,  98, 83))   # верхнее левое
    rect(screen, LIGHT_BLUE, (484, 38,  98, 83))   # верхнее правое
    rect(screen, LIGHT_BLUE, (378, 129, 98, 83))   # нижнее левое
    rect(screen, LIGHT_BLUE, (484, 129, 98, 83))   # нижнее правое

    # Крестовина окна
    rect(screen, WINDOW_WHITE, (472, 38, 12, 174))  # вертикальная
    rect(screen, WINDOW_WHITE, (378, 117, 204, 12)) # горизонтальная

    # 3. КОТ

    #ТЕЛО
    ellipse(screen, CAT_BROWN, (100, 270, 420, 160))

    # ЗАДНЯЯ ЛАПА
    ellipse(screen, CAT_BROWN, (460, 370, 90, 40))

    # ПЕРЕДНИЕ ЛАПЫ
    ellipse(screen, CAT_BROWN, (100, 390, 100, 35))  # левая лапа
    ellipse(screen, CAT_BROWN, (175, 390, 100, 35))  # правая лапа

    #ХВОСТ
    arc(screen, CAT_BROWN,
        (480, 260, 100, 120),  # прямоугольник дуги
        0, 3.14, 25)

    #ГОЛОВА
    circle(screen, CAT_BROWN, (155, 310), 75)

    #УШИ
    # Левое ухо
    polygon(screen, CAT_BROWN,
            [(108, 265), (125, 225), (152, 258)])
    # Розовая часть левого уха
    polygon(screen, EAR_PINK,
            [(113, 262), (126, 232), (149, 257)])

    # Правое ухо
    polygon(screen, CAT_BROWN,
            [(155, 255), (175, 220), (198, 250)])
    # Розовая часть правого уха
    polygon(screen, EAR_PINK,
            [(159, 253), (175, 227), (193, 249)])

    # ГЛАЗА
    # Белки глаз
    ellipse(screen, WHITE,      (118, 295, 42, 32))  # левый
    ellipse(screen, WHITE,      (168, 295, 42, 32))  # правый

    # Зелёная радужка
    circle(screen, GREEN_EYE,   (139, 311), 14)
    circle(screen, GREEN_EYE,   (189, 311), 14)

    # Чёрный зрачок
    ellipse(screen, BLACK,      (134, 300, 10, 22))  # левый зрачок
    ellipse(screen, BLACK,      (184, 300, 10, 22))  # правый зрачок

    # Обводка глаз
    ellipse(screen, BLACK,      (118, 295, 42, 32), 2)
    ellipse(screen, BLACK,      (168, 295, 42, 32), 2)

    #НОС
    polygon(screen, NOSE_PINK,
            [(152, 330), (162, 330), (157, 340)])

    #РОТ
    line(screen, BLACK, (157, 340), (148, 348), 2)
    line(screen, BLACK, (157, 340), (166, 348), 2)

    # 4. КЛУБОК НИТОК

    # Основной серый овал
    ellipse(screen, GRAY, (240, 400, 90, 55))

    # Линии на клубке
    arc(screen, GRAY_DARK, (245, 403, 80, 45), 0.3, 2.8,  2)
    arc(screen, GRAY_DARK, (248, 408, 70, 35), 0.5, 2.5,  2)
    arc(screen, GRAY_DARK, (252, 413, 60, 25), 0.7, 2.3,  2)

    # Нитка от клубка к коту
    line(screen, GRAY_DARK, (240, 425), (160, 415), 1)

    pygame.display.flip()

pygame.quit()