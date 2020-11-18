from tkinter import *
import tkinter as tk
import random
import time


# ----- Creates beginning elements -----#
root = Tk()
W, H = 800, 1000
rect_position = {}
SortType = StringVar()
SorterOPTS = ['Quick Sort', 'Selection Sort', 'Bubble Sort', 'Radix Sort']
root.title('Rectangle Organizer')
root.geometry(("{}x{}").format(W, int(H//2.5)))
root.resizable(0, 0)
SortType.set(SorterOPTS[3])
runAmount = 0
runCycle_EndIND = 0


# ----- Inputs # of rectangles from user -----#
Label(root, text="Number of Rectangles: ").grid(
    row=0, column=0, sticky='W')
Num_rect = Entry(root, width=10)
Num_rect.grid(row=0, column=1, sticky='W')


# ----- Creating rectangles -----#
def draw_rect(Tsorter, WHICHrect=-1, fill='#008000'):
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
                rect_startPos, rect_position[RHassign], rect_startPos+width_rectangles, canvas_height, tags='MyR', fill=fill)
            rect_startPos += width_rectangles

# Randomizes the rectangles <resets>


def create_rectsN():
    NR = int(Num_rect.get())
    for RHassign in range(NR):
        rect_position[RHassign] = random.randint(11, int(canvas_height-10))
    draw_rect(False)


# ----- Sorting rectangles -----#
def selectionSort():
    global runAmount
    num = runAmount
    for i in range(NR):
        rect_position[i] = SSsorting[i]
    root.after(20, draw_rect, True, num)
    for heightChecker in range(num+1, NR):
        if SSsorting[heightChecker] > SSsorting[num]:
            num = heightChecker
    root.after(10, draw_rect, True, num)
    SSsorting[runAmount], SSsorting[num] = SSsorting[num], SSsorting[runAmount]
    runAmount += 1
    if runAmount == NR:
        runAmount = 0
        root.after(20, draw_rect, False, -100)
        return
    root.after(25, selectionSort)


def bubbleSort():
    runAmount = 0
    for heightChecker in range(NR-1):
        if SSsorting[heightChecker] < SSsorting[heightChecker+1]:
            SSsorting[heightChecker], SSsorting[heightChecker +
                                                1] = SSsorting[heightChecker+1], SSsorting[heightChecker]
            runAmount += 1
    if runAmount == 0:
        for i in range(NR):
            rect_position[i] = SSsorting[i]
        draw_rect(False, -100)
        return
    for i in range(NR):
        rect_position[i] = SSsorting[i]
    draw_rect(False, -100, '#FF0000')
    root.after(25, bubbleSort)


def radixSort():
    global runAmount
    runAmount -= 1
    for _ in range(NR):
        for heightChecker in range(NR-1):
            if len(str(SSsorting[heightChecker])) < len(str((SSsorting[heightChecker+1]))):
                SSsorting[heightChecker], SSsorting[heightChecker +
                                                    1] = SSsorting[heightChecker+1], SSsorting[heightChecker]
            elif len(str(SSsorting[heightChecker])) >= -runAmount and len(str(SSsorting[heightChecker+1])) >= -runAmount:
                if int(str(SSsorting[heightChecker])[runAmount]) < int(str(SSsorting[heightChecker+1])[runAmount]):
                    SSsorting[heightChecker], SSsorting[heightChecker +
                                                        1] = SSsorting[heightChecker+1], SSsorting[heightChecker]
    for i in range(NR):
        rect_position[i] = SSsorting[i]
    root.after(50, draw_rect, False, -100, '#FF0000')
    if runAmount == -3:
        runAmount = 0
        for i in range(NR):
            rect_position[i] = SSsorting[i]
        root.after(50, draw_rect, False, -100)
        return
    root.after(1000, radixSort)


def sort():
    global NR
    global SSsorting
    NR = int(Num_rect.get())
    SSsorting = []
    for i in range(NR):
        SSsorting.append(rect_position[i])
    errorLabel.configure(text=' ')
    if SortType.get() == 'Quick Sort':
        SSsorting.sort(reverse=True)
        for i in range(NR):
            rect_position[i] = SSsorting[i]
        draw_rect(False, -100)
    elif SortType.get() == 'Selection Sort':
        selectionSort()
    elif SortType.get() == 'Bubble Sort':
        if NR > 500:
            errorLabel.configure(text='Error:TooMany!')
        elif NR < 2:
            errorLabel.configure(text='Error:NotEnough!')
        else:
            bubbleSort()
    elif SortType.get() == 'Radix Sort':
        if NR > 200:
            errorLabel.configure(text='Error:TooMany!')
        else:
            radixSort()


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
