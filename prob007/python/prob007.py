#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Above required to handle utf-8 characters.
#http://stackoverflow.com/questions/6289474/working-with-utf-8-encoding-in-python-source

import sys
def whenx_yis_z(x,y,z): 
   "returns a string\"x時のyはz\" where x,y,z are input parameters in order"
   return x+"時の"+y+"は"+z

print whenx_yis_z(sys.argv[1],sys.argv[2],sys.argv[3]) 
