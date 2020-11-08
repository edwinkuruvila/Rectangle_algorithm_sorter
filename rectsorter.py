from tkinter import *
import tkinter as tk
import random
import time


# ----- Creates beginning elements -----#
root = Tk()
W, H = 500, 600
rect_position = {}
SortType = StringVar()
SorterOPTS = ['Quick Sort', 'Selection Sort']
root.title('Rectangle Organizer')
root.geometry(("{}x300").format(W))
root.resizable(0, 0)
SortType.set(SorterOPTS[1])
global runAmount
runAmount = 0

# ----- Inputs # of rectangles from user -----#
Label(root, text="Number of Rectangles: ").grid(
    row=0, column=0, sticky='W')
Num_rect = Entry(root, width=5)
Num_rect.grid(row=0, column=1, sticky='W')

# ----- Creating rectangles -----#


def draw_rect(Tsorter, WHICHrect=-1):
    canvas.delete("MyR")
    NR = int(Num_rect.get())
    width_rectangles = (canvas_width-10)/NR
    rect_startPos = 5
    if Tsorter == False and WHICHrect != -100:
        for RHassign in range(NR):
            canvas.create_rectangle(
                rect_startPos, rect_position[RHassign], rect_startPos+width_rectangles, canvas_height, tags='MyR')
            rect_startPos += width_rectangles
    if Tsorter and WHICHrect != -100:
        WHICHrect = WHICHrect-1
        for RHassign in range(NR):
            if RHassign == WHICHrect:
                canvas.create_rectangle(
                    rect_startPos, rect_position[RHassign], rect_startPos+width_rectangles, canvas_height, tags='MyR', fill='#FF0000')
            else:
                canvas.create_rectangle(
                    rect_startPos, rect_position[RHassign], rect_startPos+width_rectangles, canvas_height, tags='MyR')
            rect_startPos += width_rectangles
    if Tsorter == False and WHICHrect == -100:
        for RHassign in range(NR):
            canvas.create_rectangle(
                rect_startPos, rect_position[RHassign], rect_startPos+width_rectangles, canvas_height, tags='MyR', fill='#008000')
            rect_startPos += width_rectangles


def create_rectsN():
    NR = int(Num_rect.get())
    for RHassign in range(NR):
        rect_position[RHassign] = random.randint(11, canvas_height-10)
    draw_rect(False)

# ----- Sorting rectangles -----#


def sortingList():
    global SSsorting
    SSsorting = []
    for i in range(NR):
        SSsorting.append(rect_position[i])


def selectionSort():
    global runAmount
    num = runAmount
    visual = num
    for i in range(NR):
        rect_position[i] = SSsorting[i]
    root.after(20, draw_rect, True, num)
    for numchecker in range(num+1, NR):
        if SSsorting[numchecker] > SSsorting[num]:
            num = numchecker
    root.after(10, draw_rect, True, num)
    for i in range(NR):
        rect_position[i] = SSsorting[i]
    root.after(0, draw_rect, True, visual)
    SSsorting[runAmount], SSsorting[num] = SSsorting[num], SSsorting[runAmount]
    runAmount += 1
    if runAmount == NR:
        runAmount = 0
        root.after(100, draw_rect, False, -100)
        return
    root.after(25, selectionSort)


def sort():
    global NR
    NR = int(Num_rect.get())
    sortingList()
    if SortType.get() == 'Quick Sort':
        SSsorting.sort(reverse=True)
        for i in range(NR):
            rect_position[i] = SSsorting[i]
        draw_rect(False, -100)
    elif SortType.get() == 'Selection Sort':
        selectionSort()


# ----- Menu Items -----#
Button(root, text='Draw New Rectangles', command=create_rectsN).grid(
    row=1, column=0, sticky='W')
OptionMenu(root, SortType, *SorterOPTS).grid(row=0, column=2)
Button(root, text="Sort", command=sort).grid(row=1, column=2)

# ----- Canvas for creating rectangles -----#
canvas_width = W
canvas_height = H/3
canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.grid(row=2, column=0, columnspan=3)
# Top and Bottom lines
canvas.create_line(5, 10, canvas_width-5, 10, fill="#476042")
canvas.create_line(5, canvas_height, canvas_width-5,
                   canvas_height, fill="#476042")
# Side lines
canvas.create_line(5, 10, 5, canvas_height, fill="#476042")
canvas.create_line(canvas_width-5, 10, canvas_width -
                   5, canvas_height, fill="#476042")

root.mainloop()

