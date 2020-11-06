from tkinter import *
import tkinter as tk
import random


# ----- Creates beginning elements -----#
root = Tk()
root.title('Rectangle Organizer')
W, H = 500, 600
root.geometry(("{}x{}").format(W, H))
root.resizable(0, 0)
rect_position = {}

# ----- Inputs # of rectangles from user -----#
Label(root, text="Number of Rectangles: ").grid(
    row=0, column=0, sticky='W')
Num_rect = Entry(root, width=5)
Num_rect.grid(row=0, column=1, sticky='W')


# ----- Creating rectangles -----#
def draw_rect():
    canvas.delete("MyR")
    NR = int(Num_rect.get())
    width_rectangles = (canvas_width-10)/NR
    rect_startPos = 5
    for RHassign in range(NR):
        canvas.create_rectangle(
            rect_startPos, rect_position[RHassign], rect_startPos+width_rectangles, canvas_height, tags='MyR')
        rect_startPos += width_rectangles


def create_rectsN():
    NR = int(Num_rect.get())
    for RHassign in range(NR):
        rect_position[RHassign] = random.randint(11, canvas_height-10)
    draw_rect()


# ----- Sorting rectangles -----#
def quickSort():
    NR = int(Num_rect.get())
    for  in range(NR):


    # ----- Button for activating rectangles -----#
Button(root, text='Draw New Rectangles', command=create_rectsN).grid(
    row=1, column=0, sticky='W')
Button(root, text='Quick Sort', command=quickSort).grid(
    row=1, column=1, sticky='W')


# ----- Canvas for creating rectangles -----#
canvas_width = W
canvas_height = H/3
canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.grid(row=2, column=0, columnspan=3, pady=20)
# Top and Bottom lines
canvas.create_line(5, 10, canvas_width-5, 10, fill="#476042")
canvas.create_line(5, canvas_height, canvas_width-5,
                   canvas_height, fill="#476042")
# Side lines
canvas.create_line(5, 10, 5, canvas_height, fill="#476042")
canvas.create_line(canvas_width-5, 10, canvas_width -
                   5, canvas_height, fill="#476042")


root.mainloop()
