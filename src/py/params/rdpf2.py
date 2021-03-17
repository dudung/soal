# 
# rdpf2.py
# Read parameters file and process its content
# 
# Sparisoma Viridi | https://github.com/dudung
# 
# Execute: python3 rdpf2.py params.txt
# 
# 20200922
# 2001 Derive it from redpf.py
# 2009 Removel trailing newline from file [1] and append array.
# 2025 Split line [2].
# 2029 Print non-empty array [3].
#
# References
# 1. -, "How to remove a trailing newline in Python", Kite, url
#    https://www.kite.com/python/answers/how-to-remove-a
#    -trailing-newline-in-python [20200922].
# 2. John La Rooy, "Answer to 'Python split() String into a
#    list with spaces'", StackOverflow, 11 Dec 2015, url
#    https://stackoverflow.com/a/34216612 [20200922].
# 3. John Kugelman, "Answer to 'How to check if array is not
#    empty? [duplicate]'", StackOverflow, 23 Feb 2011, url
#    https://stackoverflow.com/a/5086185 [20200922].
# 

# Import necessary modules
import sys

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

# Show params
for p in params:
	b = p.split();
	if b:
		print("Name = ", b[0])
		print("Value = ", b[1])
