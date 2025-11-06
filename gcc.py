#gc module translation.
import gc
def mem_alloc():
    pass
def mem_free():
    pass
def threshold(inputs=-1):
    gc.set_threshold(inputs)
def collect():
    gc.collect()
def isenabled():
    return gc.isenabled()
def enable():
    gc.enable()
def disable():
    gc.disable()
