#!/usr/bin/env python
from __future__ import print_function

import sys

# input comes from the system
for line in sys.stdin:
    
    line = line.strip() 
   
    words = line.split()
  
    for word in words:
        
        print ('%s\t%s' % (word, 1))

