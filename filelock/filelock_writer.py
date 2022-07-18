"""
FileLock package.

This py is to test filelock behavior
"""
import time
from datetime import datetime
# For argument
import sys
from filelock import FileLock

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Require at least one argument")
        sys.exit(-1)

    FILENAME = "test.dat"
    lock = FileLock(FILENAME+".lock")
    with lock:
        for i in range(100):
            with open(FILENAME, "+a", encoding="utf-8") as f:
                print(sys.argv[1] + " is writing to "+FILENAME
                      + " for " + str(i) + " time")
                f.write(f"Writing at {datetime.now()}")
                time.sleep(1)
    sys.exit(0)
