#! /usr/bin/python

import re
import sys

#self file
import common

def get_enum_str(source):
	line = re.match(r'enum', source.strip())
	if not line:
		return
	p = re.compile('.+?"(.+?)"')
	enum_name = p.findall(source.strip())
	if enum_name:
		return enum_name[0]

def main(filename):
	source_fd = open(filename, "rt")
	while True:
		line = source_fd.readline()
		if line:
			leaf_enum = common.get_leaf_enum_buf(source_fd, line)
			if leaf_enum:
				#print "\n++++++++++++++++++++++++++++++++++++\n" + leaf_enum + "----------------------------------------\n"
				leaf_name = common.cmn_get_leaf_key(leaf_enum)
				#print "key_name: " + key_name
				common.cmn_get_enum(leaf_enum, leaf_name, common.cmn_get_prefix(sys.argv[1]))
		else:
			break
	source_fd.close()