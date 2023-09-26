newlist = [1,2,3,4,5,6,7,8,9]

if 3 in newlist: # linear time
  print("Found")


for n in newlist: 
  # this is also linear search, however for smaller arrays this is enough, bcoz for binary search to wrok sorting should be done first , which takes time
  if n == 3:
    print("Found")
    break


