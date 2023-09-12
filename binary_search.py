

def binary_search(searchlist, numtosearch):

  sorted_searchlist = sorted(searchlist)
  
  first = 0
  last = len(searchlist)-1


  while first < last:
    midpoint = int((last - first)/2)
    if numtosearch < sorted_searchlist[midpoint]:
      last = midpoint
    elif numtosearch > sorted_searchlist[midpoint]:
      first = midpoint
    elif numtosearch == sorted_searchlist[midpoint]:
      return midpoint
  return None
    
numstotest = [1,2,3,4,5,6,7,8,9]
print(binary_search(numstotest, 12))
print(binary_search(numstotest, 6))
