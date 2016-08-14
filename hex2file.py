#!/usr/bin/python
# Filename: hex2file.py
# Author: JollyFrogs
# This work is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License.
#
import sys

def print_usage():
  print("Usage: python hex2file.py hexfile.bin \"4142434445\"")
  print("Usage: python hex2file.py hexfile.bin \"\\x41\\x42\\x43\\x44\\x45\"")
  print("Note: To show binary contents of new file use: hexdump -C hexfile.bin")
  exit()

if not len(sys.argv) == 3: print_usage()

if sys.argv[1].find("x") != -1: sys.argv[2] = sys.argv[2].replace("\\x", "")
binfile = open(sys.argv[1], 'w')
try: binfile.write(sys.argv[2].decode('hex'))
except: print("Error - Could not write file"); exit()
else: print("Success - %s bytes written to %s" % (len(sys.argv[2])/2,sys.argv[1]))
binfile.close()

