from tkinter import *
import tkinter as tk
import random
import time


# ----- Creates beginning elements -----#
root = Tk()
W, H = 500, 600
rect_position = {}
SortType = StringVar()
SorterOPTS = ['Quick Sort', 'Selection Sort', 'Bubble Sort']
root.title('Rectangle Organizer')
root.geometry(("{}x{}").format(W, H//2))
root.resizable(0, 0)
SortType.set(SorterOPTS[2])
runAmount = 0
runCycle_EndIND = 0


# ----- Inputs # of rectangles from user -----#
Label(root, text="Number of Rectangles: ").grid(
    row=0, column=0, sticky='W')
Num_rect = Entry(root, width=10)
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
    for i in range(NR):
        rect_position[i] = SSsorting[i]
    root.after(20, draw_rect, True, num)
    for numchecker in range(num+1, NR):
        if SSsorting[numchecker] > SSsorting[num]:
            num = numchecker
    root.after(10, draw_rect, True, num)
    SSsorting[runAmount], SSsorting[num] = SSsorting[num], SSsorting[runAmount]
    runAmount += 1
    if runAmount == NR:
        runAmount = 0
        root.after(20, draw_rect, False, -100)
        return
    root.after(25, selectionSort)


def bubbleSort():
    global runAmount
    global runCycle_EndIND
    for i in range(NR):
        rect_position[i] = SSsorting[i]
    root.after(5, draw_rect, True, runAmount+1)
    if SSsorting[runAmount] < SSsorting[runAmount+1]:
        SSsorting[runAmount], SSsorting[runAmount +
                                        1] = SSsorting[runAmount+1], SSsorting[runAmount]
        runCycle_EndIND += 1
    for i in range(NR):
        rect_position[i] = SSsorting[i]
    root.after(0, draw_rect, True, runAmount+1)
    if runCycle_EndIND == 0 and runAmount == NR-2:
        for i in range(NR):
            rect_position[i] = SSsorting[i]
        runAmount = 0
        runCycle_EndIND = 0
        root.after(5, draw_rect, False, -100)
        return
    runAmount += 1
    if runAmount == NR-1:
        runAmount = 0
        runCycle_EndIND = 0
    root.after(5, bubbleSort)


def sort():
    global NR
    NR = int(Num_rect.get())
    sortingList()
    errorLabel.configure(text=' ')
    if SortType.get() == 'Quick Sort':
        SSsorting.sort(reverse=True)
        for i in range(NR):
            rect_position[i] = SSsorting[i]
        draw_rect(False, -100)
    elif SortType.get() == 'Selection Sort':
        selectionSort()
    elif SortType.get() == 'Bubble Sort':
        if int(Num_rect.get()) > 30:
            errorLabel.configure(text='Error:TooMany!')
        elif int(Num_rect.get()) == 1:
            errorLabel.configure(text='Error:NotEnough!')
        else:
            bubbleSort()


# ----- Menu Items -----#
Button(root, text='Draw New Rectangles', command=create_rectsN).grid(
    row=1, column=0, sticky='W')
OptionMenu(root, SortType, *SorterOPTS).grid(row=0, column=2)
Button(root, text="Sort", command=sort).grid(row=1, column=2)
errorLabel = Label(root)
errorLabel.grid(row=1, column=1)


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

