#!/usr/bin/python

import os
import re
import sys

byts=[]

def print_byts(n1,n2):
    out=""
    for i in range(n1,n2+1,1):
        out=out+byts[i]
    return out
first_line=1
f=open("filename")
for i in f.readlines():
    if first_line:
        print ("PACA start address is : " + i.split(":")[0])
        first_line = 0
    i=i.split(":")[1]
    i=i.strip();
    for b in i.split(" "):
        for j in range(3,0,-1):
            byts.append(b[2*j:2*j+2])

print "lpaca : 0x" + print_byts(0,7)
print "paca_index: 0x" + print_byts(8,9)
print "paca_lock: 0x" + print_byts(10,11)
print "kernel_toc: 0x" + print_byts(24,31)
print "kernel_base: 0x" + print_byts(32,39)
print "kernel_msr: 0x" + print_byts(40,47)


