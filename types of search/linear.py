def linearsearch(a,el):
  for i in range(len(a)):
    if a[i] == el :
      print(f"Element {el} at index {i} ")
      return i
  return -1
a=[1,31,12,9,18,2]
print(linearsearch(a,9))