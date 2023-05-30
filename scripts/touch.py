import os
import time

def touch_file(filepath):
    """change file modification time to current time"""
    os.utime(filepath, times=(time.time(), time.time()))
