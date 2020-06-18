# -*- coding=utf-8 -*-

from graphics import *


GRID_WIDTH = 40
COLUMN = 15
ROW = 15
ai_list = []
me_list = []
aime_list = []
all_list = []
next_point = [0, 0]
ratio = 1
DEPTH = 3
cut_count = 0
search_count = 0

# 画棋盘
def GobangWin():
	gw = GraphWin('AI Gobang', GRID_WIDTH*COLUMN, GRID_WIDTH*ROW)
	gw.setBackground('gray')
	for j in range(0, GRID_WIDTH*COLUMN+1, GRID_WIDTH):
		l = Line(Point(j, 0), Point(j, GRID_WIDTH*COLUMN))
		l.draw(gw)
	for i in range(0, GRID_WIDTH*ROW+1, GRID_WIDTH):
		l = Line(Point(0, i), Point(GRID_WIDTH*ROW, i))
		l.draw(gw)
	return gw

# 主程序


def run():
	# 初始化
    gw = GobangWin()
    for j in range(COLUMN+1):
        for i in range(ROW+1):
            all_list.append((i, j))
    # 游戏结束后的处理
    message = Text(Point(300, 300), 'Click anywhere to quit.')
    message.draw(gw)
    gw.getMouse()
    gw.close()



if __name__ == '__main__':
	run()
