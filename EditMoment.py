import os
import time

file = open('Mg', 'r')
line = file.readline()
file.close()
os.system("rm Mg")
time.sleep(1)
file = open('Mg', 'w')
line = line.strip()
file.write(line)