"""
Originally on Ti Nspire CX II Calculator, this file is for cpython on computer.
a drawing lib, support for drawing lines, circles, rectangles, and text.
"""
#COPYRIGHT Texas Instruments Inc. 2025
#USING DEDICATED LICENSE.
import tkinter as tk
from time import sleep

root = tk.Tk()
root.title("Running...")
canvas = tk.Canvas(root, width=320, height=240, bg="white")
canvas.pack()

current_color = "#000000"
current_pen = ("thin", "solid")
virtual_window = (0, 0, 320, 240)

def set_color(r, g, b):
    global current_color
    current_color = f"#{r:02x}{g:02x}{b:02x}"

def fill_rect(x, y, w, h):
    canvas.create_rectangle(x, y, x+w, y+h, fill=current_color, outline="")

def fill_circle(x, y, r):
    canvas.create_oval(x - r, y - r, x + r, y + r, fill=current_color, outline="")

def fill_arc(x, y, w, h, start, extent):
    canvas.create_arc(x, y, x+w, y+h, start=start, extent=extent, fill=current_color)

def use_buffer():
    pass

def paint_buffer():
    root.update()
    sleep(0.01)
def draw_text(x, y, text):
    canvas.create_text(x, y, text=text, anchor="nw", fill=current_color, font=("Arial", 10))

def draw_line(x1, y1, x2, y2):
    canvas.create_line(x1, y1, x2, y2, fill=current_color)

def draw_rect(x, y, w, h):
    canvas.create_rectangle(x, y, x+w, y+h, outline=current_color)

def clear():
    canvas.delete("all")

def set_pen(thickness, style):
    global current_pen
    current_pen = (thickness, style)

def set_window(xmin, ymin, xmax, ymax):
    global virtual_window
    virtual_window = (xmin, ymin, xmax, ymax)