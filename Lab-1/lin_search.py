arr = [1, 2, 3, 4, 5] 
search = 3 

def linsearch(search, arr):
    n = len(arr)
    for i in range(n):
        if arr[i] == search: 
            return i
    return "not found" 

print(linsearch(search, arr))
