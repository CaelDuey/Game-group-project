import Map

class Ship:
    def create(self, Map, width=10, height=75, x_pos=50,
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
        self.table = table
        self.triangle = self.Map.draw_triangle(self)


    def move_up(self, master):
        self.y_pos = self.y_pos - self.y_speed
        if(self.y_pos <= 0):
            self.y_pos = 0
        x1 = self.x_pos
        x2 = self.x_pos+self.width
        y1 = self.y_pos
        y2 = self.y_pos+self.height
        self.table.move_item(self.rectangle, x1, y1, x2, y2)

    def move_down(self, master):
        self.y_pos = self.y_pos + self.y_speed
        far_bottom = self.table.height - self.height
        if(self.y_pos >= far_bottom):
            self.y_pos = far_bottom
        x1 = self.x_pos
        x2 = self.x_pos+self.width
        y1 = self.y_pos
        y2 = self.y_pos+self.height
        self.table.move_item(self.triangle, x1, y1, x2, y2)
        
