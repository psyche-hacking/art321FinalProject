import imageio
import matplotlib.pyplot as plt
from pygifsicle import optimize
import re


import os

os.chdir("results")
filenames = [f for f in os.listdir() if (f.endswith(".jpg"))]
filenames.sort(key=lambda var:[int(x) if x.isdigit() else x for x in re.findall(r'[^0-9]|[0-9]+', var)])

i = -1

with imageio.get_writer("../test.gif", mode='I') as writer:
	for filename in filenames:
		#if (filename == "scribble2635.jpg"):
		#	break
		i = i+1
		if(i % 3 == 0):
			image = imageio.imread(filename)
			writer.append_data(image)

optimize("../test.gif")