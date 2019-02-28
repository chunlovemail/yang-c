#! /usr/bin/python

import re
import sys

#def cmn_get_prefix(filename):
#	line = filename.strip().split(".")
#	if line:
#		prefix = line[0]
#		return prefix

def cmn_get_prefix(filename):
	names = filename.strip().split("/")
	if names:
		prefix = names[len(names) - 1].strip().split(".")
		return prefix[0]


def cmn_append_file(filename_prefix, line):
	out_fd = open(filename_prefix + ".h", "a+")
	out_fd.write(line + "\n")
	out_fd.close()

def cmn_trans_underline(source):
	line = source.strip().split("-")
	out = ''
	for i in range(0, len(line)):
		out += line[i]
		if i < (len(line) - 1):
			out += "_"
	return out

def cmn_get_typedef_type(source):
	print source.strip()
	p = re.compile(r'.* type .*')
	lists = p.findall(source.strip())
	if lists:
		names = lists[0].strip().split(" ")
		if names:
			return names[1]
	print "cmn_get_typedef_type get error"		

def cmn_get_typedef_key(source):
	line = re.match(r'typedef', source.strip())
	if line:
		name = source.strip().split(" ")
		return name[1]

def cmn_write_list_to_file(filename, lists):
	for i in range(0, len(lists)):
		cmn_append_file(filename, lists[i])