from tkinter import *

class Map:

    def __init__(self, window, bg="black", width=600, height=400):
        self.width = width
        self.height = height
        self.bg = bg
        
        self.canvas = Canvas(window, bg=self.bg, height=self.height, width=self.width)
        self.canvas.pack()

        font=("comic sans", 68)
        self.scoreboard=self.canvas.create_text(300,65,font=font,fill="white")


    def draw_triangle(self, triangle):
        x1 = triangle.x_posn
        x2 = triangle.x_posn + triangle.width
        y1 = triangle.y_posn
        y2 = triangle.y_posn + triangle.height
        c = triangle.color
        return self.canvas.create_rectangle(x1, y1, x2, y2, fill=c)

    def move_item(self, item, x1, y1, x2, y2):
        self.canvas.coords(item, x1, y1, x2, y2)

    def draw_oval(self, oval):
        x1 = oval.x_posn
        x2 = oval.x_posn + oval.width
        y1 = oval.y_posn
        y2 = oval.y_posn + oval.height
        c = oval.color
        return self.canvas.create_oval(x1, y1, x2, y2, fill=c)

    def draw_score(self, left, right):
        scores = str(right) + " " + str(left)
        self.canvas.itemconfigure(self.scoreboard, text=scores)

 
