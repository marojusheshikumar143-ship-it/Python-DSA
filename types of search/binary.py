def binarysearch(a,el):
    low = 0
    high =len(a) - 1
    while low <= high:
        mid = (low + high)
        if a[mid] == el:
            print(f"Element {el} at index {mid}")
            return mid
        elif a[mid] < el:
            low = mid + 1
        else:
            high = mid - 1
    return - 1
a=[1,2,9,20,25,10]
print(binarysearch(a,9))