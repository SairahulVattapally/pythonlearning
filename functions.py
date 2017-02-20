# Prompting users for numbers and adding it.
x=raw_input("value of x:")
x=int(x)
y=raw_input("value of y:")
y=int(y)
def print_two(x,y):
    z=x+y
    return z
print "Adding x=%d and y=%d to get:"%(x,y), print_two(x,y)

# Passing direct numbers to the function.
x=10
y=5
print "Pasing two numbers %d & %d directly"%(x,y)
print "Adding directly by calling function: " ,print_two(x,y)

# Passing different variables through function
first_number=55
second_number=25
print "Passing different variables first_number: %d & second_number=%d into the function by calling it."%(first_number,second_number)
print "Adding by pasing values through different variables:", print_two(first_number,second_number)
