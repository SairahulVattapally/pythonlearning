filename=raw_input("Enter the filename:")
print "Opening the file..."
txt=open(filename,'a')
print "Appending the file."
print "Entering the content of the file."
line1=raw_input('>')
line2=raw_input(">")
line3=raw_input(">")
print "Writing the content into the file"
txt.write('%s \n %s \n %s \n' %(line1,line2,line3))
print "Saving the file."
txt.close()


