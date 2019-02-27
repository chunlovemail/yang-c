#! /usr/bin/python

import re
import sys

typedef_index = 0
g_source_filename = sys.argv[1]
g_prefix = ''
g_brefix_flag = False

def tran_underline(source):
	line = source.strip().split("-")
	out = ''
	for i in range(0, len(line)):
		out += line[i]
		if i < (len(line) - 1):
			out += "_"
	return out

def append_file(line):
	out_fd = open(g_prefix + ".h", "a+")
	out_fd.write(line + "\n")
	out_fd.close()

def export_list_to_file(enum_list):
	for i in range(0, len(enum_list)):
		append_file(enum_list[i])

def get_prefix(source):
	line = re.match(r'module', source)
	if line:
		prefix = source.strip().split(" ")
		return prefix[1]

def get_typedef_key(source):
	line = re.match(r'typedef', source.strip())
	if line:
		name = source.strip().split(" ")
		return name[1]

def get_enum_str(source):
	line = re.match(r'enum', source.strip())
	if not line:
		return
	p = re.compile('.+?"(.+?)"')
	enum_name = p.findall(source.strip())
	if enum_name:
		return enum_name[0]

def get_typedef_type(source):
	line = re.match(r'type', source.strip())
	if line:
		name = source.strip().split(" ")
		return name[1]

def get_typedef(f_fd, key_name):
	tmp_buf = ''
	b_enum_flag = False
	enum_list = []
	while True:
		line = f_fd.readline()
		if not line:
			continue;
		tmp_buf += line
		
		get_typedef_type(line)
		enum_name = get_enum_str(line)
		if enum_name:
			define = key_name + '-' + enum_name
			if not b_enum_flag:
				enum_list.append("/* " + g_prefix + ':' + key_name + " */")
				enum_list.append("typedef enum en_" + tran_underline(key_name).upper())
				enum_list.append("{")
				enum_list.append("    " + tran_underline(define).upper() + "_NONE = 0,")
				b_enum_flag = True
			enum_list.append("    " + tran_underline(define).upper() + ",")
			
		m = re.findall('{', tmp_buf)
		n = re.findall('}', tmp_buf)
		if ((len(m) == len(n)) and (len(m) != 0)):
			break;
	if b_enum_flag:
		enum_list.append("    " + tran_underline(key_name).upper() + "_MAX")
		enum_list.append("} EN_" + tran_underline(key_name).upper() + ";\n")
		export_list_to_file(enum_list)
	
def init_out_file(prefix):
	out_fd = open(prefix + ".h", "wt")
	tmp = tran_underline(prefix)
	out_fd.write("#ifndef " + "_" + tmp.upper() + "_" + "\n")
	out_fd.write("#define " + "_" + tmp.upper() + "_" + "\n")
	out_fd.write("\n")
	out_fd.close()


def close_out_file(prefix):
	out_fd = open(prefix + ".h", "a+")
	out_fd.write("#endif\n")
	out_fd.close()

g_source_fd = open(g_source_filename, "rt")
while True:
	source = g_source_fd.readline()
	if source:
		if not g_brefix_flag:
			tmp = get_prefix(source)
			if tmp:
				g_prefix = tmp
				g_brefix_flag = True
				tran_underline(g_prefix)
				init_out_file(g_prefix)

		key_name = get_typedef_key(source)
		if key_name:
			get_typedef(g_source_fd, key_name)
	else:
		break
g_source_fd.close()
close_out_file(g_prefix)