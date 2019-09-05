from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
# Copyright 2009 National Research Foundation (South African Radio Astronomy Observatory)
# BSD license - see LICENSE for details

from optparse import OptionParser

def standard_parser(default_port=1235):
    parser = OptionParser()
    parser.add_option('--port', dest='port', type=int, default=default_port)
    return parser
