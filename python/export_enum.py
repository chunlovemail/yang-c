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
	p = re.compile('.+?"(.+?)"')
	enum_name = p.findall(source.strip())
	if enum_name:
		return enum_name[0]

def get_enum(f_fd, key_name):
	enumeration = ''
	while True:
		tmp = ''
		tmp = f_fd.readline()
		if not tmp:
			continue;
		enumeration += tmp
		
		enum_name = get_enum_str(tmp)
		if enum_name:
			print key_name + '-' + enum_name
			
		m = re.findall('{', enumeration)
		n = re.findall('}', enumeration)
		if (len(m) == len(n)):
			#print enumeration
			break;
	
def init_out_file(prefix):
	out_fd = open(prefix + ".h", "wt")
	tmp = tran_underline(prefix)
	out_fd.write("#ifndef " + "_" + tmp.upper() + "_" + "\n")
	out_fd.write("#define " + "_" + tmp.upper() + "_" + "\n")
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
			print g_prefix + ':' + key_name
			get_enum(g_source_fd, key_name)
	else:
		break
g_source_fd.close()
