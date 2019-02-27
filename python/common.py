#! /usr/bin/python

import re
import sys

def cmn_get_prefix(filename):
	line = filename.strip().split(".")
	if line:
		prefix = line[0]
		return prefix