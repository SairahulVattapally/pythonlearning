ten_things= "Hi, I'm Sai Prasanna, getting familiar with Python "
print "Wait, there are no ten things above. Let's fix that"

stuff=ten_things.split() # It is forming the list by splitting the string.
print "Length of the stuff: ",len(stuff)
print "Since, length of the stuff is less than 11, Let's add some items to a new list."
print "You have to enter 5 items to the new 'more_stuff' list."

i=0
more_stuff=[]
while(i<=4):
    enter_item=raw_input("Enter an item to a list:")
    more_stuff.append(enter_item)
    i=i+1
print "Here's the new list: ", more_stuff
while len(stuff)<=11:
    next_one= more_stuff.pop()
    print "Adding: ",next_one
    stuff.append(next_one)
    print "There's %d items now: " %len(stuff)
print "Here is the new list:", stuff

print "Lets play with lists"

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[4:6])