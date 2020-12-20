def mean_index(low_limti: int or float, high_limit: int or float) -> int:

    mid_index = (low_limti + high_limit)/2
    return int(mid_index)

def doc() -> str:
    part1 = "Given a sorted array arr[] of n elements, write a function to search a given element x in arr[]. A simple approach is to do linear search.The time complexity of above algorithm is O(n).\n"
    part2 = " Another approach to perform the same task is using Binary Search.\n\n" 
    part3 = "Binary Search: Search a sorted array by repeatedly dividing the search interval in half. Begin with an interval covering the whole array. If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. Otherwise narrow it to the upper half. Repeatedly check until the value is found or the interval is empty."
    defination = part1 + part2 + part3
    return defination

def binary_search(array: list, target: int or float) -> int:

    """Binary Serach Algorithm
    Given a sorted array arr[] of n elements, write a function to search a given element x in arr[].

    A simple approach is to do linear search.The time complexity of above algorithm is O(n). Another approach to perform the same task is using 
    Binary Search.

    Binary Search: Search a sorted array by repeatedly dividing the search interval in half. Begin with an interval covering the whole array. 
    If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. Otherwise narrow
    it to the upper half. Repeatedly check until the value is found or the interval is empty.
    
    This algorithm returns the index of the target as a value if found but the target isn't found in the array then it returns -1.
    
    """
    low = 0
    high = len(array) - 1
    target_index = -1    

    while True:
        if high == low + 1:
            break
        
        elif array[low] == target:
            target_index = low
            break
        
        elif array[high] == target:
            target_index = high
            break

        else:
            mid = mean_index(low_limti=low, high_limit=high)
            if target == array[mid]:
                target_index = mid
                break
            elif target < array[mid]:
                high = mid
            elif target > array[mid]:
                low = mid

    return target_index
