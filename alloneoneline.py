#EVERYTHING ON ONE LINE (separated by a space)
#Edward Olsen
#12/20/12

import os,sys
print 'CWD: ' + os.getcwd()
file=raw_input('File to work on: ')
if file == '':
	file='C:\Users\edward\Documents\dbs.txt' #Hardcoded for my leisure

input=open(file, 'r')
output=open(file[0:file.rfind('\\')+1] + 'output.txt', 'w')

for line in input:
	output.write(line.rstrip('\n'))
	output.write(" ")
print 'Output written to ' + file[0:file.rfind('\\')+1] + 'output.txt'
input.close()
output.close()
