def linear_search(L, x):
    n = len(L) 
    i = 0  
    found = False 

    while i < n and not found:
        if L[i] == x:  
            found = True  
        i += 1  
    
    
    if found:
        return i - 1 
    else:
        return -1  
    
    L = [4, 8, 18, 15, 16, 1, 1]
x = 16
result = linear_search(L, x)
print(result)  # Expected output: 4

L = [4, 8, 18, 15, 16, 1, 1]
x = 1
result = linear_search(L, x)
print(result)  # Expected output: 5



def binary_search(L, low, high, x):
    if high < low:  
        return -1
    mid = (low + high) // 2 

    if L[mid] == x:  
        return mid
    elif L[mid] > x:  
        return binary_search(L, low, mid - 1, x)
    else:  
        return binary_search(L, mid + 1, high, x)


L = [3, 9, 16, 21, 22, 26, 30]
low = 0
high = 6
x = 9
result = binary_search(L, low, high, x)
print(result)  # Expected output: 1

L = [3, 9, 16, 21, 22, 26, 30]
low = 0
high = 6
x = 22
result = binary_search(L, low, high, x)
print(result)  # Expected output: 4

L = [3, 9, 16, 21, 22, 26, 30]
low = 0
high = 6
x = 10
result = binary_search(L, low, high, x)
print(result)  