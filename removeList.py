# remove() method
thislist1 = ["apple", "banana", "cherry"]
thislist1.remove("banana")
print(thislist1)

# pop() method 
thislist2 = ["apple", "banana", "cherry"]
# index
#              0        1          2
thislist2.pop(1) # Remove the 1 index item
print(thislist2)

thislist3 = ["apple", "banana", "cherry"]
thislist3.pop() # Remove the last item:
print(thislist3)


# clear() method

thislist4 = ["apple", "banana", "cherry"]
thislist4.clear() # The list still remains, but it has no content.
print(thislist4)
