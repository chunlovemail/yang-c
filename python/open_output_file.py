#! /usr/bin/python

import sys
import common

def init_file(prefix):
	if not prefix:
		return
	out_fd = open(prefix + ".h", "wt")
	out_fd.write("#ifndef " + "_" + common.cmn_trans_underline(prefix).upper() + "_" + "\n")
	out_fd.write("#define " + "_" + common.cmn_trans_underline(prefix).upper() + "_" + "\n")
	out_fd.write("\n")
	out_fd.close()
