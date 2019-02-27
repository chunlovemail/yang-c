#! /usr/bin/python

import sys
import common

def close_out_file(prefix):
	out_fd = open(prefix + ".h", "a+")
	out_fd.write("#endif\n")
	out_fd.close()

close_out_file(common.cmn_get_prefix(sys.argv[1]))