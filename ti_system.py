"""
Originally on Ti Nspire CX II Calculator, this file is for cpython on computer.
a system api for calculator.
"""
#COPYRIGHT Texas Instruments Inc. 2025
#USING DEDICATED LICENSE.
import keyboard
import sys
import os
import json
from time import *

_SAVEFILE = "varsave.json"

def store_value(var, amount):
    """save a value to dedicated json file"""
    if os.path.exists(_SAVEFILE):
        with open(_SAVEFILE, "r") as f:
            data = json.load(f)
    else:
        data = {}
    data[var] = amount
    with open(_SAVEFILE, "w") as f:
        json.dump(data, f)

def recall_value(var):
    """load a value from dedicated json file"""
    if os.path.exists(_SAVEFILE):
        with open(_SAVEFILE, "r") as f:
            data = json.load(f)
        return data.get(var, None)
    return None

def clear_history():
    os.system('cls' if os.name == 'nt' else 'clear')

def ticks_cpu():
    """get cpu tick"""
    return int(time())

def get_mouse():
    return (-1,-1)

def get_platform():
    """get platform name"""
    return "pc"

_excluded_keys = {"up", "down", "left", "right"}
_pressed_keys = set()

def get_key():
    global _pressed_keys
    while True:
        event = keyboard.read_event()
        
        if event.event_type == keyboard.KEY_DOWN:
            key = event.name
            if key not in _excluded_keys and key not in _pressed_keys:
                _pressed_keys.add(key)
                return key

        elif event.event_type == keyboard.KEY_UP:
            key = event.name
            _pressed_keys.discard(key)

import tkinter as tk

root = tk.Tk()
root.title("Running...")
canvas = tk.Canvas(root, width=318, height=212, bg="white")
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