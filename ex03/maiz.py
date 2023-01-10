import tkinter as tk
import maze_maker as mm
import pygame
from pygame.locals import *


def key_down(event):
    global key
    key = event.keysym


def key_up(event):
    global key
    key = ""


def main_proc():
    global cx, cy, mx, my
    if key == "Up": my -= 1
    if key == "Down": my += 1
    if key == "Left": mx -= 1
    if key == "Right": mx += 1
    if maze_lst[mx][my] == 1: # 移動先が壁だったらa
        if key == "Up": my += 1
        if key == "Down": my -= 1
        if key == "Left": mx += 1
        if key == "Right": mx -= 1   

    cx, cy = mx*40+20, my*40+20
    canvas.coords("kokaton", cx, cy)
    root.after(150, main_proc)

class Score():
    #初期化メソッド
    def __init__(self):
        self.font  = pygame.font.SysFont("hgep006", 50)
        self.point = 0
 
    #スコア計算
    def cal_score(self, point):
        self.point += point * 100
 
    #スコア描画
    #def draw(self, surface):
    #    text = self.font.render("{:04d}".format(self.point), True, (63,255,63))
    #    surface.blit(text, [10, 5])


def bgm():
    pygame.mixer.init(frequency = 44100)  
    pygame.mixer.music.load("menuettm.mp3")    
    pygame.mixer.music.play(10) 

def alarm():
    pygame.mixer.init(frequency = 44100)  
    pygame.mixer.music.load("carstop.wav")    
    pygame.mixer.music.play(1)       



if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root, width=1200, height=1000, bg="black")
    canvas.pack()
    bgm()

    maze_lst = mm.make_maze(30, 18)
    # print(maze_lst)
    mm.show_maze(canvas, maze_lst)

    mx, my = 1, 16
    cx, cy = mx*30+30, my*30+30
    tori = tk.PhotoImage(file="fig/1.png")
    canvas.create_image(cx, cy, image=tori, tag="kokaton")
    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    main_proc()
    root.mainloop()
    

