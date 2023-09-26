

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


def recursive_binary_search(list, target, start=0, end=None):
    if end is None:
        end = len(list) - 1
    if start > end:
        return -1

    mid = (start + end) // 2

    if target == list[mid]:
        return mid
    else:
        if target < list[mid]:
            return recursive_binary_search(list, target, start, mid-1)
        else:
            return recursive_binary_search(list, target, mid+1, end)

numstotest = [1,2,3,4,5,6,7,8,9]
print(binary_search_recursive(numstotest, 12))
print(binary_search_recursive(numstotest, 6))  
print("===========================================")
print(recursive_binary_search(numstotest, 12))
print(recursive_binary_search(numstotest, 6))

  
