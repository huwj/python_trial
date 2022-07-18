"""
FileLock package.

This py is to test filelock behavior
"""
import time
from datetime import datetime
from filelock import SoftFileLock


FILENAME = "test.dat"

lock = SoftFileLock(FILENAME+".lock")
with lock:
    for i in range(20):
        with open(FILENAME, "+a", encoding="utf-8") as f:
            print("Writing to "+FILENAME)
            f.write(f"Writing at {datetime.now()}")
            time.sleep(1)
