#PROGRAM 1: Maximum Value in a List
def find_maximum(L):
    max = L[0]
    for e in L:
        if e > max:
            max = e
    return max
# Example usage:
numbers = [3, 1, 4, 1, 5, 9, 2]
max_value = find_maximum(numbers)
print(max_value)



#PROGRAM 2: Filtering Even Numbers
def filter_even(L):
    result = []
    for x in L:
        if x % 2 == 0:
            result.append(x)
    return result
# Example usage:
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter_even(numbers)
print(even_numbers)



#PROGRAM 3: List Reversal
def ReverseList(L):
    if len(L) <= 1:
        return L
    else:
        first = L[0]
        rest = L[1:]
        return ReverseList(rest) + [first]

# Example usage:
L = ['e', 'n', 'o', 'd', 'l', 'l', 'e', 'w']
print("Original List:", L)

reversed_L = ReverseList(L)
print("Reversed List:", reversed_L)



#PROGRAM 4 Binary Search
def BinarySearch(L, target):
    left = 0
    right = len(L) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if L[mid] == target:
            return mid
        elif L[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

L = [1, 3, 5, 7, 9]
target = 7 # Changed target to 10, which is not in the list
result = BinarySearch(L, target)

if result != -1:
    print(f"Target {target} found at index {result}. Search successful!")
else:
    print(f"Target {target} not found in the list. Search unsuccessful.")



#PROGRAM 5: Bubble Sort
def bubble_sort(L):
    n = len(L)
    
    for i in range(n-1):
        for j in range(n-i-2+1):  
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]  
    
    return L

# Example usage:
L = [5, 2, 8, 12, 1, 6]
print("Original list:", L)
sorted_L = bubble_sort(L)
print("Sorted list:", sorted_L)