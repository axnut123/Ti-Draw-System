"""
Originally on Ti Nspire CX II Calculator, this file is for cpython on computer.
a system api for calculator.
"""
#COPYRIGHT Texas Instruments Inc. 2025
#USING DEDICATED LICENSE.
from keyboard import *
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
    sys.version()

_last_key = None

def get_key():
    '''get last key pressed'''
    global _last_key

    k = read_key()

    arrow_keys = ("up", "down", "left", "right")

    if k in arrow_keys:
        return k

    if k and k != _last_key:
        _last_key = k
        return k

    elif not k:
        _last_key = None

    return None
