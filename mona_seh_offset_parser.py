#!/usr/bin/python
'''
Filename: mona_seh_offset_parser.py
Description: parses seh.txt from "!mona seh" for bad characters and returns valid addresses in seh.log
Author: JollyFrogs
'''
badchars = "\x0a\x0d\x2f\x3a\x3f\x40\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff"
goodchars = "\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0b\x0c\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3b\x3c\x3d\x3e\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f"

logfile = open('seh.log', 'w')    # open seh.log in write mode (overwrite old seh.log)
logfile.write("Addresses found:"+"\n") # initialize seh.log
logfile.close()                   # close seh.log
sehfile = open('seh.txt', 'r')    # open seh.txt as read-only
linelist = sehfile.readlines()    # create a list of all lines in seh.txt
sehfile.close()                   # close seh.txt now that we have all lines in RAM

goodbytesfound = True             # used to check if we found at least one valid address
for line in linelist:
  if line.startswith('0x'):       # for all lines that start with "0x"
    badbytefound = False          # used to check if we find bad chars in the address
    address_bytes = line.partition(' ')[0][2:].decode("hex") # get bytes from address
    for addrbyte in address_bytes:# check each byte in address
      for badbyte in badchars:    # check each bad byte against address bytes
        if addrbyte.lower() == badbyte.lower(): badbytefound = True
    if badbytefound == False:     # No badbytes found; this address is good
      logfile = open('seh.log', 'a') # append the seh.log file with this address
      logfile.write(line)         # write the address to the file
      logfile.close()             # close the seh.log file
      goodbytesfound = True       # we found at least one good address
if goodbytesfound == False:       # we found no good addresses at all
  logfile = open('seh.log', 'a');logfile.write("No addresses found!");logfile.close()

