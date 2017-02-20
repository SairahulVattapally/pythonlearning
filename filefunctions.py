# Writing a file and copying into another file
f=raw_input("Enter the file name? \n")
fileopen=open(f,'w')
line1=raw_input("Enter the first line into file:")
line2=raw_input("Enter the second line into file:")
line3=raw_input("Enter the third line into file:")
print 'Writing to the file %r..'%f
fileopen.write('%s \n %s \n %s \n'%(line1,line2,line3))
fileopen.close()
print "Written!"
f2=raw_input("Enter the second file name? \n")
fileopen2=open(f2,'w')
fileopen=open(f).read()
print "Copying to the file %r..." %f2
fileopen2.write(fileopen)
fileopen2.close()
print "Copied!"

# Defining fucnctions for file operations on 'another file'

def print_all(f):
    print f.read()
def rewind(f):
    f.seek(0)
def print_a_line(linecount,f):
    print linecount, f.readline()

# Passing the parameters to the file.

fileopen3=open(f2)
print "Let's print the whole file"
print_all(fileopen3)

print "Lets take a rewind"
rewind(fileopen3)

print "Lets print three lines"
currentline=1
print_a_line(currentline,fileopen3)
currentline=currentline+1
print_a_line(currentline, fileopen3)
currentline=currentline+1
print_a_line(currentline,fileopen3)

