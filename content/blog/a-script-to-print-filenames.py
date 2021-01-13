# simply prints the filenames of this directory in the terminal
# python a-script-to-print-filenames.py
import os

for root, dirs, files in os.walk("."):
	for filename in files:
		print filename