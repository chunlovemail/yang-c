#! /usr/bin/python

import sys
import common

def init_out_file(prefix):
	if not prefix:
		return
	out_fd = open(prefix + ".h", "wt")
	out_fd.write("#ifndef " + "_" + prefix.upper() + "_" + "\n")
	out_fd.write("#define " + "_" + prefix.upper() + "_" + "\n")
	out_fd.write("\n")
	out_fd.close()

init_out_file(common.cmn_get_prefix(sys.argv[1]))