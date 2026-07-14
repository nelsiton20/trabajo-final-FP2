import os
import sys

print("CWD:", os.getcwd())
print("sys.path:")
for p in sys.path:
    print(" ", repr(p))