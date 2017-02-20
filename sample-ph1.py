# Prompt for entering the file name.
filename=raw_input("Enter the filename: ")
# Open the file
file=open(filename)
# Displaying the file name
print "Here's your file:",filename
# Reading the file
x=file.read()
# Displaying the content of file
print "Here's the content of file: ",x
y=file.close()
print "Closed-Output : " ,y