from tkinter import *

import maps, ship, laser

window = Tk()
window.title("spacerds")
my_maps = maps.Map(window)

starry_night_image = PhotoImage(file = "giphy.gif")
my_maps.canvas.create_image(0, 0, anchor=NW, image = starry_night_image, tags="bg_img")

my_maps.canvas.lower("bg_img")

x_velocity = 0
y_velocity = -10
first_serve = True
direction = "right"

my_laser = laser.Laser(maps=my_maps, x_speed=x_velocity, y_speed=y_velocity,
                     height=20, width=10, color="red")

ship_R = ship.Ship(maps=my_maps, width=50, height=50, x_posn=550, y_posn=140, color="white")
ship_L = ship.Ship(maps=my_maps, width=50, height=50, x_posn=10, y_posn=140, color="blue")
#may not work
#ship_R.detect_collision(my_laser, sides_sweet_spot=False, topnbottom_sweet_spot= True)
#ship_L.detect_collision(my_laser, sides_sweet_spot=False, topnbottom_sweet_spot= True)
#work in progress
#def game_flow():
 

window.bind("w", ship_L.move_up)
window.bind("s", ship_L.move_down)
window.bind("a", ship_L.move_left)
window.bind("d", ship_L.move_right)
window.bind("<Up>",ship_R.move_up)
window.bind("<Down>",ship_R.move_down)
window.bind("<Right>",ship_R.move_right)
window.bind("<Left>",ship_R.move_left)




window.mainloop()


