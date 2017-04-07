#!/usr/bin/python

import os
import re
import sys

byts=[]

def print_byts(n1,n2):
    out=""
    for i in range(n2,n1-1,-1):
        print str(i)+" : "+byts[i]
        out=out+byts[i]
    return out
if (len(sys.argv) != 2) :
    print "Usage ./prase_paca_dump.py <dump_file>"
first_line=1
f=open(sys.argv[1])
for i in f.readlines():
    if first_line:
        print ("PACA start address is : " + i.split(":")[0])
        first_line = 0
    i=i.split(":")[1]
    i=i.strip();
    for b in i.split(" "):
        print b
        for j in range(0,8,2):
            byts.append(b[j:j+2])

print byts[0]
print byts[1]
print "lpaca : 0x" + print_byts(0x0,0x7)
print "paca_index: 0x" + print_byts(0x8,0x9)
print "paca_lock: 0x" + print_byts(0x10,0x11)
print "kernel_toc: 0x" + print_byts(0x10,0x17)
print "kernel_base: 0x" + print_byts(0x18,0x1F)
print "kernel_msr: 0x" + print_byts(0x20,0x27)
