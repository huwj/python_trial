"""
FileLock package.

This py is to test filelock behavior
"""
import time
from datetime import datetime
# For argument
import os
import sys
# from filelock import SoftFileLock
from filelock import FileLock

if __name__ == "__main__":
    FILENAME = "test.dat"
    
    # lock = SoftFileLock(FILENAME+".lock")
    lock = FileLock(FILENAME+".lock")
    with lock:
        try:
            os.remove(FILENAME)
        except OSError as e:
            sys.exit(f"Failed to delete {FILENAME}: {e.errno}")
    sys.exit(0)
