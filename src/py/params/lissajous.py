# 
# lissajous.py
# Read parameters file and process its content to produce
# Lissajous pattern in PNG format
# 
# Sparisoma Viridi | https://github.com/dudung
# 
# Execute: python3 lissajous.py params.txt out.png
# 
# 20200922
# 2108 Derive it from redpf2.py and plan to implement [1].
# 2152 Install NumPy through Cygwin.
# 2203 Install PIL through Cygwin python37-imaging package (x).
# 2226 Install for 37 NumPy and execute with python 37, ok.
# 2229 Test the example [1] and it works.
# 2242 Create empty white image 10x10.
# 20200923
# 0501 Change output from argv[2] to OUTF in parameters file.
# 0517 Create emty white PNG image with size (2Ax)x(2Ay).
# 0543 Change pixel color in two-dimensional array [3], pixels.
# 0553 Reduce Ax and Ay with 0.98 for better Lissajous curve.
# 
# References
# 1. Jebby, "Answer to 'How to create image from a list of
#    pixel values in Python3?'", StackOverflow, 25 Oct 2017,
#    url https://stackoverflow.com/a/46924413 [20200922].
# 2. -, "https://wiki.python.org/moin/ForLoop", Python, url
#    https://wiki.python.org/moin/ForLoop [20200923].
# 3. -, "Python - 2D Array", TutorialsPoint, url https://www.
#    tutorialspoint.com/python_data_structure/python_2darray
#    .htm [20200923].
# 

# Import necessary modules
import sys
from PIL import Image
import numpy as np
import math

# Get command line arguments
argv = sys.argv

# Get parameters filename
fn = argv[1]

# Open parameters file
fp = open(fn, "r")

# Declare array
params = []

# Iterate throug line in opened file
for line in fp:
	# Remove trailing new line
	line2 = line.rstrip("\n")
	
	# Append line to params
	params.append(line2)

# Close file
fp.close()

# Get params
for p in params:
	b = p.split();
	if b:
		if b[0] == "AMPX": Ax = float(b[1])
		if b[0] == "AMPY": Ay = float(b[1])
		if b[0] == "TPEX": Tx = float(b[1])
		if b[0] == "TPEY": Ty = float(b[1])
		if b[0] == "PHAX": phx = float(b[1])
		if b[0] == "PHAY": phy = float(b[1])
		if b[0] == "TBEG": tbeg = float(b[1])
		if b[0] == "TEND": tend = float(b[1])
		if b[0] == "TSTP": dt = float(b[1])
		if b[0] == "OUTF": fn2 = b[1]

# Define default color
o = (255, 255, 255)
i = (255, 0, 0)

# Ilustrate plus or '+' in a PNG file -- not used
pixels = [
	[o, o, o, o, i, i, o, o, o, o],
	[o, o, o, o, i, i, o, o, o, o],
	[o, o, o, o, i, i, o, o, o, o],
	[o, o, o, o, i, i, o, o, o, o],
	[i, i, i, i, i, i, i, i, i, i],
	[i, i, i, i, i, i, i, i, i, i],
	[o, o, o, o, i, i, o, o, o, o],
	[o, o, o, o, i, i, o, o, o, o],
	[o, o, o, o, i, i, o, o, o, o],
	[o, o, o, o, i, i, o, o, o, o],
]

# Create empty image
pixels = []
for row in range(int(2 * Ay)):
	rows = []
	for col in range(int(2 * Ax)):
		rows.append(o)
	pixels.append(rows)

# Iterate from tbeg to tend with step dt
N = int((tend - tbeg)/dt)
for j in range(0, N + 1):
	t = round(tbeg + j * dt, 4)
	x = 0.98 * Ax * math.sin(2 * math.pi * t / Tx + phx)
	y = 0.98 * Ay * math.sin(2 * math.pi * t / Ty + phy)
	xx = int(Ax + x)
	yy = int(Ay - y)
	if xx in range(int(2 * Ax)) and yy in range(int(2 * Ay)):
		pixels[yy][xx] = i

# Convert the pixels into an array using numpy
array = np.array(pixels, dtype=np.uint8)

# Use PIL to create an image from the new array of pixels
new_image = Image.fromarray(array)
new_image.save(fn2)
