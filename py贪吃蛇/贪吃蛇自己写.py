import pygame
from turtle import *
from pygame.locals import *
from sys import exit
import time
from random import *
# from freegames import square,vector
"""
做一个贪吃蛇游戏
属性：画出food和snack
接着：控制snack上下左右的移动
然后：计算snack和food的碰撞，然后snack变长
最后：当snack喷到四周的墙壁或者蛇头碰到自己的身体，则游戏结束
"""

pygame.init()
WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption("贪吃蛇")

pygame.key.set_repeat(1, 200)  # 表示每隔1毫秒发送一个

pygame.time.Clock()
fhsClock = pygame.time.Clock()  # 时钟

snake = "images/snake.png"  # 创建蛇头图片
snake = pygame.image.load(snake).convert()  # 加载蛇头图片
beij = "images/yemeinv.jpg"  # 创建背景图
beij = pygame.image.load(beij)  # 加载背景图

# 背景音乐，可自定义
# pygame.mixer.music.load("music/半城烟沙.mp3")  # 加载音乐文件
# pygame.mixer.music.play()  # 开始播放


font = pygame.font.SysFont("microsoftyaheimicrosoftyaheiui",30) # 设置字体格式和大小
name_font = font.render("Game Over",True,(122,0,0)) # 创建游戏结束提示Game Over
restart_font = font.render("Restart",True,(0,0,122))
tis_font = font.render("Press r to restart",True,(122,0,0)) # 创建游戏结束提示 Press r to restart
font = pygame.font.SysFont("microsoftyaheimicrosoftyaheiui",20)
tis1_font = font.render("Press r to restart",True,(122,0,0)) # 创建右上加提示 Press r to restart

snake_colour = (255,122,122) # 蛇的颜色
food_colour = (255,122,0) # 食物的颜色
x,y = 60,40 # 蛇的起始位置
a = 20 # 控制一下移动的距离
b = 0 # 控制游戏重新开始
c = 0 # 控制移动方向
d = 5 # 控制速度
rp = (x,y) # 蛇的起始位置
rs = (20,20) # 蛇的方块大小

fk_list = [[60,40],[40,40],[20,40]] # 定义一个方块蛇列表
rps = (randint(0,(WIDTH-20)/20)*20,randint(0,(HEIGHT-20)/20)*20) # 显示食物方块随机的位置
rss = (20,20) # 食物方块的大小


def move():
    global rps,rp,d
    rp = (x, y)  # 蛇的起始位置
    if 0 <= x < WIDTH and 0 <= y < HEIGHT:
        screen.fill((0, 122, 0))  # 刷新背景
        screen.blit(beij, (-200, -200)) # 背景图
        fk_list.insert(0, list(rp))  # 在开头插入新的位置
        pygame.draw.rect(screen, food_colour, Rect(rps, rs))  # 显示食物方块的位置
        for i in range(len(fk_list)):  # 显示蛇的长度
            pygame.draw.rect(screen, snake_colour, Rect(fk_list[i], rss))  # 显示蛇长
        if rp == rps:  # 如果蛇头和果实位置重合就吃到食物，在蛇的列表后面追加当前的位置
            fk_list.append(list(rps))  # 表示在列表最后面追加位置
            d += 1
            rps = (randint(0, (screen.get_width() - 20) / 20) * 20,randint(0, (screen.get_height() - 20) / 20) * 20)  # 重新生成食物方块的随机位置
        else:
            fk_list.pop()  # 如果没有吃到食物就删除最后一个位置
    else:
        screen.fill((122,122,0)) # 游戏结束之后的背景颜色
        screen.blit(name_font,(screen.get_width()/2-name_font.get_width()/2,screen.get_height()/2-name_font.get_height()/2)) # 游戏结束之后提示Game over
        screen.blit(tis_font, (screen.get_width() / 2 - tis_font.get_width() / 2, screen.get_height()*0.8 - tis_font.get_height() / 2)) # 游戏之后提示Press r to restart,按r重新开始游戏


def restart():
    global x,y,rp,b,c,d,rps,fk_list
    if b == 1: # 如果b恒等于1 就重新开始游戏
        x = 60 # x重新设置初始位置
        y = 40 # y重新设置初始位置
        rp = (x, y) # 重新设置蛇的初始位置
        b = 0 # 重新开始游戏
        c = 0 # 控制蛇的移动方向
        d = 5 # 恢复开始的游戏速度
        rps = (randint(0, (screen.get_width() - 20) / 20) * 20, randint(0, (screen.get_height() - 20) / 20) * 20)  # 重新生成食物方块的随机位置
        fk_list = [[60,40],[40,40],[20,40]]


def directionkeymove():
    global x,y,b,c
    move_x, move_y = 0, 0
    if event.type == KEYDOWN:
        if event.key == K_UP or event.key == ord("w"):
            move_y = -a
            c = 1
        elif event.key == K_DOWN or event.key == ord("s"):
            move_y = a
            c = 2
        elif event.key == K_LEFT or event.key == ord("a"):
            move_x = -a
            c = 3
        elif event.key == K_RIGHT or event.key == ord("d"):
            move_x = a
            c = 4
        elif event.key == ord("r"):  # 按r重新开始游戏
            b = 1
    # elif event.type == KEYUP:
    #     move_x = a
    #     move_y = 0
    if c == 1: # y向上走
        y -= a
    elif c == 2: # y向下走
        y += a
    elif c == 3: # x向左走
        x -= a
    elif c == 4: # x向右走
        x += a


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    directionkeymove()  # 方向键控制方向
    move()  # 蛇移动
    restart()  # 重新开始
    screen.blit(snake, rp)  # 显示蛇头图片
    screen.blit(snake, rps)  # 显示食物图片
    screen.blit(tis1_font, (screen.get_width() - tis1_font.get_width(), 0)) # 右上角提示按r重新开始
    fhsClock.tick(d)  # 时钟频率控制游戏快慢
    pygame.display.update()  # 刷新
