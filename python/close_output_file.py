#! /usr/bin/python

import sys
import common

def tail_file(prefix):
	if not prefix:
		return
	out_fd = open(prefix + ".h", "a+")
	out_fd.write("#endif\n")
	out_fd.close()