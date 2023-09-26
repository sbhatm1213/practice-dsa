newlist = [1,2,3,4,5,6,7,8,9]

if 3 in newlist: # linear time O(n)
  print("Found")


for n in newlist: 
  # this is also linear search, however for smaller arrays this is enough, bcoz for binary search to wrok sorting should be done first , which takes time
  if n == 3:
    print("Found")
    break

newlist.append(23) # constant time to add elem at end of list O(1)
print(newlist)

newlist.extend([16,13,47]) # time taken is whatever the length of the list you pass to extend O(k)
print(newlist)

newlist.insert(4, 55) # insert 55 at index 4, linear time O(n)
print(newlist)

newlist.remove(3) # removes first occurence of 3, linear time O(n)
print(newlist)

newlist.index(9) # gives index of the elem, linear time O(n)
print(newlist)


