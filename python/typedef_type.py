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

def get_typedef_not_enum(f_fd, source, prefix):
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
	
	ret = re.search("enumeration", tmp_buf)
	if not ret:
		return tmp_buf

def function(source, key_name, prefix):
	name = common.cmn_get_typedef_type(source)
	if not name:
		return
	
	trans_key_name = common.cmn_trans_underline(key_name)
	common.cmn_append_file(prefix, "/* typedef " + prefix + ":"+ key_name + " "+ name + " */")
	if ((name == "int8") and (name == "int16") and (name == "int32") and (name == "int64") and (name == "uint8") and (name == "uint16") and (name == "uint32") and (name == "uint64")):
		common.cmn_append_file(prefix, "typedef " +  name + "_t " + trans_key_name + ";\n")
	elif (name == "decimal64"):
		common.cmn_append_file(prefix, "typedef " + "double " + trans_key_name + ";\n")
	elif (name == "string"):
		common.cmn_append_file(prefix, "typedef " + "char " + trans_key_name + ";\n")
	elif (name == "boolean"):
		common.cmn_append_file(prefix, "typedef " + "bool " + trans_key_name + ";\n")
	elif (name == "enumeration"):
		print "Error: enumeration is not in this function"
	else:
		print "unknown type: " + name
		common.cmn_append_file(prefix, "typedef " + name + " "+ trans_key_name + ";\n")

def main(filename):
	source_fd = open(filename, "rt")
	while True:
		key_name = ''
		source = source_fd.readline()
		if source:
			key_name = common.cmn_get_typedef_key(source)
			if key_name:
				tmp_buf = get_typedef_not_enum(source_fd, source, common.cmn_get_prefix(sys.argv[1]))
				if tmp_buf:
					function(tmp_buf, key_name, common.cmn_get_prefix(sys.argv[1]))
		else:
			break
	source_fd.close()