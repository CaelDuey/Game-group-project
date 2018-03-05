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
       
        tk.Frame.__init__(self, master)
        self.pack()
        self.canvas = tk.Canvas(self,bg="black", width=SCREEN[0], height=SCREEN[1])
        self.canvas.pack()
        font=("comic sans", 68)
        self.scoreboard=self.canvas.create_text(300,65,font=font,fill="white")


        self.bullets = [] 
        self.tick_loop() 
        self.ship = self.create_ship(30, 175, "blue")
        self.ship2 = self.create_ship2(570, 175, "white")
          
        master.bind("<Left>", self.go_left)
        master.bind("<Right>", self.go_right)
        master.bind("<Up>", self.go_up)
        master.bind("<Down>", self.go_down)
        master.bind("<space>", self.space_key)
        master.bind("f", self.go_f)
        master.bind("a", self.go_a)
        master.bind("d", self.go_d)
        master.bind("w", self.go_w)
        master.bind("s", self.go_s)
# detect collision is a work in progress
#    def detect_collision(self, bullets):
 #       canvas.move(self, 0,-10)
#        canvas.update()
#        window.after(50, detect_collision, "Hit")

#        global star
#        ran = len(opponent)
#        if star == 0:
#            for x in range(0,ran):
 #               collision = canvas.coords(self)
#                space = canvas,coords(opponent[x])
#        if hit[0] == space[0] and hit[0] <= space[0] + 50:
 #           if hit[1] <= space[1] + 50:
 #               canvas.delete(opponent[x])
#                opponent.remove(opponent[x])
 #               canvas.delete(self)
 #               star = 1
 #                       break


 
         
    def create_ship(self, x, y, tk_fill):
        return self.canvas.create_polygon(x, y, x - 25, y + 35, x + 25, y + 35, fill=tk_fill)

    def create_ship2(self, x, y, tk_fill):
        return self.canvas.create_polygon(x, y, x - 25, y + 35, x + 25, y + 35, fill=tk_fill)

    
    def draw_score(self, left, right):
        scores = str(right) + " " + str(left)
        self.canvas.itemconfigure(self.scoreboard, text=scores)

    def tick_loop(self):
        remove_list = []
        for enum, bullet in enumerate(self.bullets):
            coords = self.canvas.coords(bullet.bullet)
            if coords[1] < 0 or coords[0] < 0 or coords[2] > SCREEN[0]:
                remove_list.append(enum)
                self.canvas.delete(bullet.bullet)
            else:
                bullet.move(self.canvas)
         
 
        for enum, index in enumerate(remove_list):
            self.bullets.pop(index - enum)
     
       
        self.after(int(1000/30), self.tick_loop) 
         
         
    def go_left(self, event):
        self.canvas.move(self.ship2, -20, 0)
        self.canvas.update()
         
    def go_right(self, event):
        self.canvas.move(self.ship2, 20, 0)
        self.canvas.update()
         
    def go_up(self, event):
        self.canvas.move(self.ship2, 0, -20)
        self.canvas.update()
         
    def go_down(self, event):
        self.canvas.move(self.ship2, 0, 20)
        self.canvas.update()
                
    def go_a(self, event):
        self.canvas.move(self.ship, -20, 0)
        self.canvas.update()
         
    def go_d(self, event):
        self.canvas.move(self.ship, 20, 0)
        self.canvas.update()
         
    def go_w(self, event):
        self.canvas.move(self.ship, 0, -20)
        self.canvas.update()
         
    def go_s(self, event):
        self.canvas.move(self.ship, 0, 20)
        self.canvas.update()
         
    def space_key(self, event=0):
        x, y = self.canvas.coords(self.ship2)[:2]
        self.bullets.append(Bullet(self.canvas, x, y, "green", (-10, 0)))

    def go_f(self, event=0):
        x, y = self.canvas.coords(self.ship)[:2]
        self.bullets.append(Bullet(self.canvas, x, y, "red", (10, 0)))


#    def game_flow():
#        global score_solo

 #       if bullet.detect_collision(ship) == True:
#            score_solo = score_solo + 1
#            my_App.remove_item(ship)
#           my_App.draw_score(score_solo)
#          if(score_solo >=2) :
 #               score_solo = "winner"
 #               my_App.draw_score(score_solo)
                
 #       if bullet.detect_collision(ship2) == True:
#            score_solo = score_solo + 1
 #           my_App.remove_item(ship)
 ##           my_App.draw_score(score_solo)
 #           if(score_solo >=2) :
 #               score_solo = "winner"
 #               my_App.draw_score(score_solo)

                

    
                
     
def main():
    root = tk.Tk()
    app = App(root)
    app.mainloop()
     
if __name__ == '__main__':
    main()        




         
        

    

        

       


         
