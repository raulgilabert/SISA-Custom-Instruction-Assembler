#!/bin/bash

FILE=$1

filename="${FILE%.*}"

python3 main.py $filename.S > ${filename}_translated.S
sisa-as ${filename}_translated.S -o ${filename}_translated.o

sisa-objdump -d -z --section=.text ${filename}_translated.o > ${filename}_translated.code
./limpiar.pl codigo ${filename}_translated.code
