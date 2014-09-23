import sys
import os

if len(sys.argv) == 2:
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        print filename + " is not exist."
        exit(1)
    if not os.access(filename, os.R_OK):
        print filename + " is access denied."
        exit(0)
