import Map
from tkinter import *

class Ship:
    def create(self, Map, width=60, height=60, x_pos=50,
               y_posn=50, color="blue", x_speed=35, y_speed=35):
        self.width = width
        self.height = height
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.color = color
        self.x_start = x_pos
        self.y_start = y_pos
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.Map = Map
        self.triangle = self.Map.draw_triangle(self)


    def move_up(self, master):
        self.y_pos = self.y_pos - self.y_speed
        if(self.y_pos <= 0):
            self.y_pos = 0
        x1 = self.x_pos
        x2 = self.x_pos+self.width
        y1 = self.y_pos
        y2 = self.y_pos+self.height
        self.Map.move_item(self.triangle, x1, y1, x2, y2)

    def move_down(self, master):
        self.y_pos = self.y_pos + self.y_speed
        far_bottom = self.Map.height - self.height
        if(self.y_pos >= far_bottom):
            self.y_pos = far_bottom
        x1 = self.x_pos
        x2 = self.x_pos+self.width
        y1 = self.y_pos
        y2 = self.y_pos+self.height
        self.Map.move_item(self.triangle, x1, y1, x2, y2)

    def move_right(self, master):
        self.x_pos = self.x_pos + self.x_speed
        far_right = self.Map.width - self.width
        if(self.x_pos >= far_right):
            self.x_pos = far_right
        x1 = self.x_pos
        x2 = self.x_pos+self.width
        y1 = self.y_pos
        y2 = self.y_pos+self.height
        self.Map.move_item(self.triangle, x1, y1, x2, y2)

    def move_left(self, master):
        self.x_pos = self.x_pos - self.x_speed
        far_left = self.Map.width - self.width
        if(self.x_pos <= far_left):
            self.x_pos = far_left
        x1 = self.x_pos
        x2 = self.x_pos+self.width
        y1 = self.y_pos
        y2 = self.y_pos+self.height
        self.Map.move_item(self.triangle, x1, y1, x2, y2)

    def start_pos(self):
        self.x_pos = self.x_start
        self.y_pos = self.y_start

    def detect_collision(self, lasers):
        canvas.move(self, 0,-10)
        canvas.update()
        window.after(50, detect_collision, "Hit")

        global star

        ran = len(opponent)

        if star == 0:
            for x in range(0,ran):

                collision = canvas.coords(self)
                space = canvas,coords(opponent[x])


                if hit[0] == space[0] and hit[0] <= space[0] + 50:
                    if hit[1] <= space[1] + 50:
                        canvas.delete(opponent[x])
                        opponent.remove(opponent[x])
                        canvas.delete(self)
                        star = 1 
                        break
                        
                        

        
        

    

        
