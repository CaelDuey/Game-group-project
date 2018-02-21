from tkinter import *
import Map, spaceship

window = Tk()
window.title("spacerds")
my_Map = Map.Map(window)

space = PhotoImage(file = "gifphy.mp4")
my_Map.canvas.create_image(0, 0, anchor=NW, image = space, tags="bg_img")

my_Map.canvas.lower("bg_img")

spaceship_R = spaceship.Ship(Map=my_Map, width=15, height=100, x_pos=575, y_pos=150, color="white")
spaceship_L = spaceship.Ship(Map=my_Map, width=15, height=100, x_pos=20, y_pos=150, color="blue")


def game_flow():

    my_lazer.move_next()
    window.after(50, game_flow)

window.bind("w", spaceship_L.move_up)
window.bind("s", spaceship_L.move_down)
window.bind("a", spaceship_L.move_left)
window.bind("d", spaceship_L.move_right)
window.bind("<Up>",spaceship_R.move_up)
window.bind("<Down>",spaceship_R.move_down)
window.bind("<Right>",spaceship_R.move_right)
window.bind("<Left>",spaceship_R.move_left)




window.mainloop()


