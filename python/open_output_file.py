#! /usr/bin/python

import sys
import common

def init_file(prefix):
	if not prefix:
		return
	out_fd = open(prefix + ".h", "wt")
	out_fd.write("#ifndef " + "_" + prefix.upper() + "_" + "\n")
	out_fd.write("#define " + "_" + prefix.upper() + "_" + "\n")
	out_fd.write("\n")
	out_fd.close()
