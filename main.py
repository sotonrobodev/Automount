#!/usr/bin/python3

import sys, time, os, traceback, inspect
file_path =os.path.join(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))),"test.txt")
f = open(file_path,"w")
f.write("TESTING, I HAVE NO IDEA IF THIS WILL WORK!")
f.close()