#!/usr/bin/env python3

import os
import inspect

file_path = os.path.join(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))),"test.txt")

with open(file_path,"w") as f:
    f.write("TESTING, I HAVE NO IDEA IF THIS WILL WORK!")
