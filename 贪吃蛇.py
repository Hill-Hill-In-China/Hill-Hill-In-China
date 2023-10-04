#王一山作。
from tkinter import *
import random
import time
tk = Tk()
cv = Canvas(tk, height=300, width=300)
cv.pack()

class Bug:
    def __init__(self, cv, color, line):
        self.cv = cv
        self.bug_id = cv.create_rectangle(144, 144, 156, 156, fill=color, outline=line)   #画贪吃蛇的第一节。
        self.bug2_id = cv.create_rectangle(132, 144, 144, 156, fill=color, outline=line)
        self.turn = False
        self.x = 1
        self.y = 0
        self.bug_co = cv.coords(self.bug_id)
        self.bug2_co = cv.coords(self.bug2_id)
        self.bug_x1 = self.bug_co[0]
        self.bug_y1 = self.bug_co[1]
        self.bug_x2 = self.bug_co[2]
        self.bug_y2 = self.bug_co[3]
        self.cv.bind_all('<KeyPress-Left>', self.turn_left)
        self.cv.bind_all('<KeyPress-Right>', self.turn_right)
        self.cv.bind_all('<KeyPress-Up>', self.turn_top)
        self.cv.bind_all('<KeyPress-Down>', self.turn_bottom)
       
    def move(self):
        self.cv.move(self.bug_id, self.x, self.y)
        self.bug_x1 = self.bug_co[0]
        self.bug_y1 = self.bug_co[1]
        self.bug_x2 = self.bug_co[2]
        self.bug_y2 = self.bug_co[3]
        if self.turn == False:
            self.cv.move(self.bug2_id, 0.5, self.y)
        else:
            self.cv.move(self.bug2_id, self.x, 0)
            if self.bug2_co[0] == self.bug_co[0]:
                self.cv.move(self.bug2_id, self.x, self.y)

    def bug2_move(self):
        pass

    def turn_left(self, evt):
        self.x = -1
        self.y = 0
        self.turn = True

    def turn_right(self, evt):
        self.x = 1
        self.y = 0
        self.turn = True

    def turn_top(self, evt):
        self.y = -1
        self.x = 0
        self.turn = True

    def turn_bottom(self, evt):
        self.y = 1
        self.x = 0
        self.turn = True
        
class Apple:
    def __init__(self, cv, color, line):
        self.hit = False
        self.cv = cv
        self.color = color
        self.line = line
        self.appcoord = random.choice(list(range(0, 312, 12)))
        self.apple_x1 = self.appcoord
        self.apple_x2 = self.apple_x1 + 12
        self.apple_y1 = self.appcoord
        self.apple_y2 = self.apple_y1 + 12
        self.apple_id = cv.create_rectangle(self.apple_x1, self.apple_y1, self.apple_x2, self.apple_y2, fill=color, outline=line)

    def apple_move(self):
        if self.hit == True:
            self.cv.itemconfig(self.apple_id, state='hidden')
            print('ferferferfervr', end=',')
            time.sleep(5)
            self.__init__(self, cv, color, line)
          
    def hitbug(self):
        self.apple_move()

bug1 = Bug(cv, 'green', 'green')
apple = Apple(cv, 'red', 'red')

while True:   #主循环
    bug1.move()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
