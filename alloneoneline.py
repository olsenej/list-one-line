#EVERYTHING ON ONE LINE (separated by a space)
#Edward Olsen
#12/20/12

file=raw_input('File: ')
if file == '':
  file='dbs.txt'
input=open(file, 'r')
output=open('C:\Users\edward\Documents\output.txt', 'w')

for line in input:
	output.write(line.rstrip('\n'))
	output.write(" ")

input.close()
output.close()
