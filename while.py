# Creating a list and appending the names upto 5 members to that list.
friendslist=[]
i=0
while(i<=5):
    friends=raw_input("Enter your friend name:")
    friends=str(friends)
    friendslist.append(friends)
    i=i+1
print "List of my 5 friends: ",friendslist

# Filtering based on length of the name
for j in friendslist:
    if len(j)<5:
        print "Short named friend: ",j
    elif len(j)>=5:
        print "Long named friend: ",j
    else:
        print "Wrong input, Please try again"

