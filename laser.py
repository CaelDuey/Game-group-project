from tkinter import *
import ship

class laser:

        def __init__(self, Map, width=10, height=10, color="red",
                     x_speed=8, y_speed=3, x_start=0, y_start=0):
            self.width= width
            self.height = height
            self.x_posn = x_start
            self.y_posn = y_start
            self.color = color

            self.x_start = x_start
            self.y_start = y_start
            self.x_speed = x_speed
            self.y_speed = y_speed
            self.maps = maps
            self.circle = self.maps.draw_oval(self)

        def start_position(self):
            self.x_posn = self.x_start
            self.y_posn = self.y_start

        def move_next(self):
            self.x_posn = self.x_posn + self.x_speed
            self.y_posn = self.y_posn + self.y_speed

        def stop_laser(self):
            self.x_speed = 0
            self.y_speed = 0
