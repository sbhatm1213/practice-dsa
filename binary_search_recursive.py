

def binary_search_recursive(sortedlist, x):

  if len(sortedlist) == 0:
    return "Not Found"
    
  n = int(len(sortedlist)/2)
  
  
  if x > sortedlist[n]:
    binary_search_recursive(sortedlist[n+1:], x)
  elif x < sortedlist[n]:
    binary_search_recursive(sortedlist[:n], x)
  elif x == sortedlist[n]:
    return "Found "


  
  
  
