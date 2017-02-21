value1=raw_input("Enter the value 1: \n")
value1=int(value1)
value2=raw_input("Enter the value 2: \n")
value2=int(value2)
if value1 > value2:
    value3=value1-value2
    print "Subtracting the value2: %r from value1: %r to give = " %(value2,value1), value3
elif value1 < value2:
    value3=value1+value2
    print "Adding the value1: %r & value2: %r to give = "%(value1,value2),value3
else:
    print "Both are equal"