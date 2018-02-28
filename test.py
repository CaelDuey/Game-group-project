import tkinter as tk

SCREEN = 600, 400
         
class Bullet:
    def __init__(self, canvas, x, y, tk_fill, movement):
        self.bullet = canvas.create_oval(x -3 , y - 3, x + 3, y + 3, fill=tk_fill)
        self.movement = movement
         
    def move(self, canvas):
        canvas.move(self.bullet, self.movement[0], self.movement[1])
 
class App(tk.Frame):
    def __init__(self, master):
        # put canvas in frame so you can have other goodies
        tk.Frame.__init__(self, master)
        self.pack()
        self.canvas = tk.Canvas(self, width=SCREEN[0], height=SCREEN[1])
        self.canvas.pack()
        self.bullets = [] # store bullets
        self.tick_loop() # start the tick loop
        self.ship2 = self.create_ship2(25, 175, "blue")
        self.ship1 = self.create_ship1(575, 175, "red")
         
        master.bind("<Left>", ship1.go_left)
        master.bind("<Right>", ship1.go_right)
        master.bind("<Up>", ship1.go_up)
        master.bind("<Down>", ship1.go_down)
        master.bind("<space>", ship1.space_key)
        master.bind("f", ship2.go_f)
         
    def create_ship1(self, x, y, tk_fill):
        return self.canvas.create_polygon(x, y, x - 20, y + 30, x + 20, y + 30, fill=tk_fill)

    def create_ship2(self, x,y, tk_fill):
        return self.canvas.create_polygon(x, y, x - 20, y + 30, x + 20, y + 30, fill=tk_fill)

    def tick_loop(self):
        remove_list = []
        for enum, bullet in enumerate(self.bullets):
            coords = self.canvas.coords(bullet.bullet)
            if coords[1] < 0 or coords[0] < 0 or coords[2] > SCREEN[0]:
                remove_list.append(enum)
                self.canvas.delete(bullet.bullet)
            else:
                bullet.move(self.canvas)
         
        # fix poping bug        
        for enum, index in enumerate(remove_list):
            self.bullets.pop(index - enum)
     
        # framerate per seconds 1000/30 = 30 frames roughly
        self.after(int(1000/30), self.tick_loop)        
         
    def go_left(self, event):
        self.canvas.move(self.ship1, -5, 0)
        self.canvas.update()
         
    def go_right(self, event):
        self.canvas.move(self.ship1, 5, 0)
        self.canvas.update()
         
    def go_up(self, event):
        self.canvas.move(self.ship1, 0, -5)
        self.canvas.update()
         
    def go_down(self, event):
        self.canvas.move(self.ship1, 0, 5)
        self.canvas.update()
         
    def space_key(self, event=0):
        # only want the first two coords
        x, y = self.canvas.coords(self.ship1)[:2]
        # just having shoot straight up
        self.bullets.append(Bullet(self.canvas, x, y, "blue", (-10, 0)))

    def go_f(self, event=0):
        x,y = self.canvas.coords(self.ship2)[:2]

        self.bullets.append(Bullet(self.canvas, x,y, "blue", (10, 0)))
def main():
        root = tk.Tk()
        app = App(root)
        app.mainloop()
     
if __name__ == '__main__':
    main()



        




         
        

    

        

       


         
