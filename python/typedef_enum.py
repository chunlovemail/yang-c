#! /usr/bin/python

import re
import sys

#self file
import common

g_source_filename = sys.argv[1]
g_prefix = common.cmn_get_prefix(sys.argv[1])

def get_enum_str(source):
	line = re.match(r'enum', source.strip())
	if not line:
		return
	p = re.compile('.+?"(.+?)"')
	enum_name = p.findall(source.strip())
	if enum_name:
		return enum_name[0]

def get_typedef(f_fd, key_name):
	tmp_buf = ''
	b_enum_flag = False
	enum_list = []
	while True:
		line = f_fd.readline()
		if not line:
			continue;
		tmp_buf += line
		
		enum_name = get_enum_str(line)
		if enum_name:
			define = key_name + '-' + enum_name
			if not b_enum_flag:
				enum_list.append("/* " + g_prefix + ':' + key_name + " */")
				enum_list.append("typedef enum en_" + common.cmn_trans_underline(key_name).upper())
				enum_list.append("{")
				enum_list.append("    " + common.cmn_trans_underline(define).upper() + "_NONE = 0,")
				b_enum_flag = True
			enum_list.append("    " + common.cmn_trans_underline(define).upper() + ",")
			
		m = re.findall('{', tmp_buf)
		n = re.findall('}', tmp_buf)
		if ((len(m) == len(n)) and (len(m) != 0)):
			break;
	if b_enum_flag:
		enum_list.append("    " + common.cmn_trans_underline(key_name).upper() + "_MAX")
		enum_list.append("} EN_" + common.cmn_trans_underline(key_name).upper() + ";\n")
		common.cmn_write_list_to_file(g_prefix, enum_list)

def main(filename):
	g_source_fd = open(g_source_filename, "rt")
	while True:
		source = g_source_fd.readline()
		if source:
			key_name = common.cmn_get_typedef_key(source)
			if key_name:
				get_typedef(g_source_fd, key_name)
		else:
			break
	g_source_fd.close()