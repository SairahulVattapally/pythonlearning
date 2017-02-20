# Writing a file and copying the content to a new file
from os.path import exists
file1=raw_input("Enter the filename-1:")
open1=open(file1,'w')
line1=raw_input(">")
line2=raw_input(">")
open1.write('%s \n %s \n'%(line1,line2))
open1.close()

file1=raw_input("Enter the filename-1:")
open1=open(file1)
read1=open1.read()

file2=raw_input("Enter the filename-2:")
open2=open(file2,'w')
open2.write(read1)


open2.close()