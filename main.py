from tkinter import *
from floor import *
from character import Character
from resource import Resource

image_size = 72
board_size = 10

root = Tk()
canvas = Canvas(root, width=image_size * board_size, height=image_size * board_size)
resource = Resource()

hero = Character(0, 0, canvas, resource)
canvas.bind("<KeyPress>", hero.movement)
canvas.pack()
canvas.focus_set()
root.mainloop()