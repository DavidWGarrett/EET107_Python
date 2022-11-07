aaa = [2,4,7,4,8,1]
for b in aaa:
    print(b)

print(aaa[2])
print(aaa[-1]) # gives last element of the list

#print('a' + strlen(aaa)) # gives highest index value minus 1, how many items are in your list

#maximum index items is dependant on memory

# vales inside of a list can change, tuple can't
# lists can change size add remove elements
print(str(aaa[1]+aaa[2]))

#can sstitch lists together

#strings and lists are very similar functionality

print(aaa*2)

print(aaa[1:3])

print(aaa[:3])
#lists slicing
print(aaa[-2:-1])

# dot append method

aaa.append(80)
print(aaa)
# remove value from list that doesn't exist causes error
7 in aaa
# returns a true or false

aaa.remove(4)

#removes the FIRST one
print(aaa)

#remove a specific index position
aaa.index(7)
aaa.pop(4)
print(aaa)
aaa.insert(2,66.77)
#(index pos, value)
print(aaa)

aaa.sort()
print(aaa)

print(min(aaa))
print(max(aaa))

#^^^^^doesn't work if strs are in the list

# If you equate two lists like aa=bb , the lists are the same, not a copy

bb = []

aa = bb
print(bb)
aa.append(62.23)
print(bb)


