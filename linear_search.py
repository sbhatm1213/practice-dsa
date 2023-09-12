
def linear_search(searchlist, numtosearch):

  for i in range(len(searchlist)):
    if searchlist[i] == numtosearch:
      return i
  return None

numstotest = [1,3,5,2,4,6,8,7,9]
linear_search(numstotest, 12)

linear_search(numstotest, 6)
