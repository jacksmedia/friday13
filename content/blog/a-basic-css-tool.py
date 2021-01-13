### prints the filenames of this directory into a file called a-test.css
# python a-basic-css-tool.py
import os

with open("a-test.css", 'wb') as fd: # create the css file ('write binary')
	for root, dirs, files in os.walk("."):
		for filename in files:
			print filename # terminal print of filename
			fd.write(filename+'\n') # writes a filename to css file, jumps cursor to nextline ('\n')