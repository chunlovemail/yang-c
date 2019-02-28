#! /usr/bin/python

import re
import sys

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
	#print source.strip()
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

def cmn_has_enumeration(source):
	ret = re.search("enumeration", source)
	if ret:
		return True

def cmn_has_leaf(source):
	ret = re.search("leaf", source)
	if ret:
		return True

def cmn_get_leaf_key(source):
	line = re.match(r'leaf', source.strip())
	if line:
		name = source.strip().split(" ")
		return name[1]

def cmn_write_list_to_file(filename, lists):
	for i in range(0, len(lists)):
		cmn_append_file(filename, lists[i])

def get_leaf_enum_buf(source_fd, source):
	ret = cmn_has_leaf(source)
	if not ret:
		return
	tmp_buf = source
	while True:
		line = source_fd.readline()
		if not line:
			continue;
		tmp_buf += line

		m = re.findall('{', tmp_buf)
		n = re.findall('}', tmp_buf)
		if ((len(m) == len(n)) and (len(m) != 0)):
			break;
	
	ret = cmn_has_enumeration(tmp_buf)
	if ret:
		return tmp_buf

def get_typedef_enum(f_fd, source):
	ret = cmn_get_typedef_key(source)
	if not ret:
		return
		
	tmp_buf = source
	while True:
		line = f_fd.readline()
		if not line:
			continue;
		tmp_buf += line
		
		m = re.findall('{', tmp_buf)
		n = re.findall('}', tmp_buf)
		if ((len(m) == len(n)) and (len(m) != 0)):
			break;
	
	ret = re.search("typedef", tmp_buf)
	if ret:
		return tmp_buf

def cmn_get_enum(source, key_name, prefix):
	name_list = []
	value_list = []
	enum_list = []
	start = 0
	
	lists = source.replace('"', '').strip().split("\n")
	if lists:
		for i in range(0, len(lists)):
			line = re.search(r'enum ', lists[i].strip())
			if line:
				name = lists[i].strip().split(" ")
				#print name[1].strip()
				name_list.append(name[1].strip())
			line = re.search(r'value ', lists[i].strip())
			if line:
				name = lists[i].strip().split(" ")
				#print name[1].strip()[0:len(name[1].strip()) - 1]
				value_list.append(name[1].strip()[0:len(name[1].strip()) - 1])
	
	enum_list.append("/* " + prefix + ':' + key_name + " enumeration" + " */")
	enum_list.append("typedef enum en_" + cmn_trans_underline(key_name).upper())
	enum_list.append("{")
	if not ('0' == value_list[0]):
		define = key_name
		enum_list.append("    " + cmn_trans_underline(define).upper() + "_NONE = 0,")
		start = 0
	else:
		define = key_name + '-' + name_list[0]
		enum_list.append("    " + cmn_trans_underline(define).upper() + " = 0,")
		start = 1
	
	for i in range(start, len(name_list)):
		define = key_name + '-' + name_list[i]
		enum_list.append("    " + cmn_trans_underline(define).upper() + ",")

	enum_list.append("    " + cmn_trans_underline(key_name).upper() + "_MAX")
	enum_list.append("} EN_" + cmn_trans_underline(key_name).upper() + ";\n")
	cmn_write_list_to_file(prefix, enum_list)