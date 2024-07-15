import sys
import os
for path in sys.path:
    print(path)

print("Sys exec", sys.executable)
print(os.listdir("/usr/bin/"))
print(os.listdir("/usr/lib/"))
import flask