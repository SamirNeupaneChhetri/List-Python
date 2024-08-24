thislist = ["apple", "banana", "cherry"]
# index
#             0        1          2
#            -3       -2          -1
print(thislist[1]) 

# Negative indexing means start from the end
print(thislist[-3])

# ----------------------------------------------------------------------------

thislist2 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# index
#              0        1          2         3         4        5       6
#             -7       -6         -5        -4        -3       -2      -1

print(thislist2[2:6])  # start from 2 and but not include 6 
#               [start:End]

print(thislist2[:5]) # print from the start but not include position 5 
print(thislist2[-4:-1]) # here start from the -4 but not include -1

# --------------------------------------------------------------------

# Change List Items

thislist3 = ["apple", "banana", "cherry"]
thislist3[1:2] = ["blackcurrant", "watermelon"]
print(thislist3) # this changed in positon 1 to 2 items..

# we can also insert() method.
thislist3.insert(2,"watermelon") # (position, value)

