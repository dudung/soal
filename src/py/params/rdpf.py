# 
# rdpf.py
# Read parameters file
# 
# Sparisoma Viridi | https://github.com/dudung
# 
# 20200922
# 1637 Start this example.
# 1723 Collect references [1-4].
# 1735 Test simple args and add [5].
# 1751 Get newline problem in printing output.
# 1828 Solve it using python 3 [6].
# 
# References
# 1. agold, "Asnwer to 'Python file naming convention?'", 
#    Software Engineering, 6 Jun 2019, url https:// 
#    softwareengineering.stackexchange.com/a/308976 [20200922].
# 2. Dan Bader, "Python Multi-line Comments: Your Two Best
#    Options", url https://dbader.org/blog/python-multiline
#    -comment [20200922].
# 3. -,"1. Command line and environment", Python, 22 Sep 2020, 
#    url https://docs.python.org/3/using/cmdline.html
#    [20200922].
# 4. Sayak Paul, "Argument Parsing in Python", DataCamp, 16 May
#    2019, url https://www.datacamp.com/community/tutorials
#    /argument-parsing-in-python [20200922].
# 5. -, "Open a File on the Server", W3Schools, url https://www
#    .w3schools.com/python/python_file_open.asp [20200922].
# 6. codelogic, "Answer to 'How to print without newline or
#    space?'", StackOverflow, 29 Jan 2009, url https://
#    stackoverflow.com/a/493399 [20200922].
# 

import sys

# Get command line arguments
argv = sys.argv

# Get parameters filename
fn = argv[1]

# Open parameters file
fp = open(fn, "r")

# Show parameters
for line in fp:
	print(line, end="")
