#!/bin/bash
# filename: showop.sh
# Script source: http://stackoverflow.com/questions/12476548/checking-up-intel-assembly-opcodes-easily-in-linux
#
if [[ $# -eq 0 ]] ; then echo 'Usage: showop.sh "mov eax,edx;nop" [64|32]'; exit 1; fi
asminstr=${1:-"mov eax,edx;nop"}; bits=${2:-64}
numberofinstr=`echo $asminstr | grep -o ";" | wc -l`; ((numberofinstr++))
if [ -f tempasmfile.asm ]; then rm tempasmfile.asm;fi
if [ -f tempobjfile.o ]; then rm tempobjfile.o; fi
if [ -f tempexefile ]; then rm tempexefile;fi
printf "[bits $bits]\nsection .text\nglobal _start\n\n_start:\n`echo $asminstr | sed 's/;/\\n/g'`\n" >tempasmfile.asm
nasm -f elf$bits tempasmfile.asm -o tempobjfile.o
ld tempobjfile.o -o tempexefile
if [ $bits -eq 32 ]; then ndisasm -b $bits -e 0x60 tempexefile | head -n $numberofinstr
elif [ $bits -eq 64 ]; then ndisasm -b $bits -e 0x80 tempexefile | head -n $numberofinstr; fi
rm tempasmfile.asm; rm tempobjfile.o; rm tempexefile
