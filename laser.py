import maps

class Laser:

    def __init__(self, maps, width=10, height=10, color="red",
                 x_speed=15, y_speed=20, x_start=0, y_start=0):
        self.width = width
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

    def start_ball(self, x_speed, y_speed):
        self.x_speed = -x_speed
        self.y_speed = -y_speed
        self.start_position

    def move_next(self):
        self.x_posn = self.x_posn + self.x_speed
        self.y_posn = self.y_posn + self.y_speed

        if(self.x_posn <= 3):
            self.x_posn = 3
            self.x_speed = -self.x_speed

        if(self.x_posn >= (self.maps.width - (self.width - 3))):
            self.x_posn = (self.maps.width - (self.width - 3))
            self.x_speed = -self.x_speed

        if(self.y_posn <= 3):
            self.y_posn = 3
            self.y_speed = -self.y_speed

        if(self.y_posn >= (self.maps.height - (self.height - 3))):
            self.y_posn = (self.maps.height - (self.height - 3))
            self.y_speed = -self.y_speed

        x1 = self.x_posn
        x2 = self.x_posn+self.width
        y1 = self.y_posn
        y2 = self.y_posn+self.height
        self.maps.move_item(self.circle, x1, y1, x2, y2)

    def stop_ball(self):
        self.x_speed = 0
        self.y_speed = 0
