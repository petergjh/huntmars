# -*-coding:UTF-8-*-
import pygame

pygame.init()

# 创建游戏的窗口 480*700
screen = pygame.display.set_mode((1024, 768))

# 绘制背景图像
# 1> load 加载图像数据
bg = pygame.image.load("./images/background.png")
# 2> blit 绘制图像
screen.blit(bg, (0, 0))
# 3> update 更新屏幕显示
# pygame.display.update()

# 绘制英雄的飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (150, 500))

# 可以在所有图片加载绘制完后，统一调用update方法实现所有图片的更新
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 1. 定义一个pygame.Rect的变量来记录飞机的初始位置
hero_rect = pygame.Rect(150, 300, 200, 123)

# 游戏循环开始，游戏正式开始
while True:

    # 指定循环体内部的代码执行的频率
    clock.tick(60)

    # 捕获事件
    #    event_list = pygame.event.get()  # 获得用户当前时刻所做动作的事件列表
    #    if len(event_list) > 0:  # 只捕获并显示用户具体的操作动作，不打印空行
    #        print(event_list)
    # 监听事件
    for event in pygame.event.get():  # 调用pygame的 event.get方法监听所有用户事件列表，并用for循环遍历列表查看每个用户事件

        # 监听判断用户是否点击了关闭按钮
        if event.type == pygame.QUIT:
            print("游戏退出...")

            # 调用pygame的quit方法来卸载所有的模块,退出最近的for循环
            pygame.quit()

            # 调用python的exit()函数,退出while游戏循环
            exit()

    # 2. 修改飞机的位置,在游戏循环中每次让英雄向右移动1步即 x + 1
    hero_rect.x += 1

    # if hero_rect.y <= 0:  # 如果英雄的顶部移出屏幕，则将英雄的顶部移动到屏幕底部
    # hero_rect.y = 700

    if hero_rect.x >= 1024:  # 如果英雄的尾部移出屏幕，则将英雄的位置重置到屏幕底部
        hero_rect.x = -200

    # 3. 调用blit方法绘制图像
    screen.blit(bg, (0, 0))  # 刷新重置背景,把原来的图像做一个遮挡
    screen.blit(hero, hero_rect)  # 刷新重置英雄位置

    # 4. 调用update方法更新显示
    pygame.display.update()

pygame.quit()

