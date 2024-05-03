import pygame as pg
from character import Character
from Level import Level, Block
from screen import SCREEN_WIDTH, SCREEN_HEIGHT
from Group import Group_of_sprite

def text_win(number_of_levels, screen):
    win_font = pg.font.Font(None, 60)  # шрифт
    win_text = win_font.render('Вы прошли ' + str(number_of_levels) + ' уровень!', True, (255, 255, 255))  # текст
    screen.blit(win_text, (200, 300))
    pg.display.update()
def frozen_display(screen):
    end_key = True
    while end_key:  # закрытие программы после нажатия любой кнопки
        for i in pg.event.get():
            if i.type == pg.QUIT or i.type == pg.KEYDOWN:
                end_key = False
def final_win(screen,):
    screen.blit(pg.image.load("win_bg.png"), (0,0))
    win_font = pg.font.Font(None, 70)  # шрифт
    win_text = win_font.render('Поздравляем! Вы прошли игру', True, (255, 255, 255))  # текст
    screen.blit(win_text, (20, 300))
    pg.display.update()
    frozen_display(screen)
def check_final_win(tuple_levels,number_of_levels):
    return number_of_levels > len(tuple_levels)
def create_tuple_levels():
    l1 = open("level1.txt").readlines()
    l2 = open("level2.txt").readlines()
    level1 = Level(l1)
    level2 = Level(l2)
    return (level1, level2)
def stopwatch(screen, begin_of_time_count, number_of_levels):
    text_font1 = pg.font.Font(None, 25)  # шрифт
    str1=f'Время прохождения уровня {number_of_levels}:'
    text1 = text_font1.render(str1, True, (255, 255, 255))  # текст
    screen.blit(text1, (16, 16))
    text_font2 = pg.font.Font(None, 40)  # шрифт
    cur_time = pg.time.get_ticks() - begin_of_time_count
    str2 = (str(cur_time / 1000))[:4]
    text2 = text_font2.render(str2, True, (255, 255, 255))  # текст
    screen.blit(text2, (16, 48))
    pg.display.update()
def main():
    save=[]
    pg.init()
    size = (SCREEN_WIDTH, SCREEN_HEIGHT)
    screen = pg.display.set_mode(size)
    pg.display.set_caption("Огонь и вода")
    clock = pg.time.Clock() # Скорость обновления экрана
    # Создаем игроков
    player1 = Character('ogon/fire.png',
                        ['ogon/fire_left_1.png', 'ogon/fire_left_2.png',
                         'ogon/fire_left_3.png', 'ogon/fire_left_4.png'],
                        ['ogon/fire_right_1.png', 'ogon/fire_right_2.png',
                         'ogon/fire_right_3.png', 'ogon/fire_right_4.png'],"ogon")
    player2 = Character('voda/water.png',
                        ['voda/water_left_1.png', 'voda/water_left_2.png',
                         'voda/water_left_3.png', 'voda/water_left_4.png'],
                        ['voda/water_right_1.png', 'voda/water_right_2.png',
                         'voda/water_right_3.png', 'voda/water_right_4.png'],"voda")
    Group=Group_of_sprite(player1, player2)
    # Устанавливаем текущий уровень
    tuple_of_levels = create_tuple_levels()
    number_of_levels = 1
    Group.go_to_initial_position()
    # Цикл будет до тех пор, пока пользователь не нажмет кнопку закрытия
    done = False
    begin_of_time_count = 0
    # Основной цикл программы
    while not done:
        current_level = tuple_of_levels[number_of_levels-1]
        Group.set_level(current_level)
        # Отслеживание действий
        for event in pg.event.get():
            if event.type == pg.QUIT: # Если закрыл программу, то останавливаем цикл
                done = True
                break
            # Если нажали на стрелки клавиатуры, то двигаем объект
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:#1 игрок
                    player1.go_left()
                if event.key == pg.K_RIGHT:
                    player1.go_right()
                if event.key == pg.K_UP:
                    player1.jump()
                if event.key == pg.K_a:#2 игрок
                    player2.go_left()
                if event.key == pg.K_d:
                    player2.go_right()
                if event.key == pg.K_w:
                    player2.jump()
            #Отпустили клавиши
            if event.type == pg.KEYUP:
                if event.key == pg.K_LEFT and player1.movespeed_x < 0:
                    player1.stop()
                if event.key == pg.K_RIGHT and player1.movespeed_x > 0:
                    player1.stop()
                if event.key == pg.K_a and player2.movespeed_x < 0:
                    player2.stop()
                if event.key == pg.K_d and player2.movespeed_x > 0:
                    player2.stop()

        current_level.draw(screen)
        Group.update()
        Group.draw(screen)
        stopwatch(screen, begin_of_time_count, number_of_levels)
        clock.tick(30)  # Устанавливаем количество фреймов
        pg.display.flip()   # Обновляем экран после рисования объектов
        if Group.check_lose_condition():
            Group.go_to_initial_position()
            begin_of_time_count = pg.time.get_ticks()
        if Group.check_win_condition():
            save.append(pg.time.get_ticks()-begin_of_time_count)
            begin_of_time_count = pg.time.get_ticks()
            Group.go_to_initial_position()
            text_win(number_of_levels,screen)
            frozen_display(screen)
            number_of_levels+=1
            if check_final_win(tuple_of_levels, number_of_levels):
                final_win(screen)
                print(save)
                done = True
    # Корректное закрытие программы
    pg.quit()

if __name__ == '__main__':
    main()
