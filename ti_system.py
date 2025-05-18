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

def get_platform():
    """get platform name"""
    return sys.version()

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