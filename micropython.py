"""
Originally on Ti Nspire CX II Calculator, this file is for micropython lib for cpython.
"""
#COPYRIGHT Texas Instruments Inc. 2025
#USING DEDICATED LICENSE.
import sys
import traceback

def pystack_use():
    return len(traceback.extract_stack())

def stack_use():
    return sys.getrecursionlimit() - pystack_use()