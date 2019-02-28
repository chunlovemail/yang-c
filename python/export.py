#! /usr/bin/python

import re
import sys

#self file
import common
import close_output_file
import open_output_file
import typedef_enum
import typedef_type

g_source_filename = sys.argv[1]

#create output file, and init header
open_output_file.init_file(common.cmn_get_prefix(sys.argv[1]))

#trans typedef enum
#typedef_enum.main(g_source_filename)

#trans typedef not enum
#typedef_type.main(g_source_filename)

#add tail to output file
close_output_file.tail_file(common.cmn_get_prefix(sys.argv[1]))

