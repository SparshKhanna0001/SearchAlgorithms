import math


def linear_search(array: list, query: int or float) -> int:

    try:
        return array.index(query)
    except ValueError:
        return -1


def jump_measure(length_of_array: int or float) -> int:

    return int(math.sqrt(length_of_array))


def jump_indices(length_of_array: int or float) -> list:

    jump_indices = []
    var_jump_measure = jump_measure(length_of_array)
    item = jump_measure(length_of_array)    

    while item <= length_of_array:
        jump_indices.append(item)
        item += var_jump_measure

    return jump_indices


def jump_search(array: list, target: int or float) -> int:

    """Jump Search Algorithm
    Like Binary Search, Jump Search is a searching algorithm for sorted arrays. The basic idea is to check fewer elements (than linear search) 
    by jumping ahead by fixed steps or skipping some elements in place of searching all elements.

    For example, suppose we have an array arr[] of size n and block (to be jumped) size m. Then we search at the indexes 
    arr[0], arr[m], arr[2m]…..arr[km] and so on. Once we find the interval (arr[km] < x < arr[(k+1)m]), we perform a linear search operation 
    from the index km to find the element x.

    Let’s consider the following array: (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610). Length of the array is 16. Jump search will find the value of 55 with the following steps assuming that the block size to be jumped is 4.
    STEP 1: Jump from index 0 to index 4;
    STEP 2: Jump from index 4 to index 8;
    STEP 3: Jump from index 8 to index 12;
    STEP 4: Since the element at index 12 is greater than 55 we will jump back a step to come to index 8.
    STEP 5: Perform linear search from index 8 to get the element 55.

    What is the optimal block size to be skipped?
    In the worst case, we have to do n/m jumps and if the last checked value is greater than the element to be searched for, we perform m-1 comparisons more for linear search. Therefore the total number of comparisons in the worst case will be ((n/m) + m-1). The value of the function ((n/m) + m-1) will be minimum when m = √n. Therefore, the best step size is m = √n.
   
    This algorithm returns the index of the target as a value if found but the target isn't found in the array then it returns -1.
    """
    
    var_jump_indices = jump_indices(len(array))
    low = 0
    high = 0
    target_index = -1

    for i in var_jump_indices:

        if target > array[i]:
            low = i
        elif target < array[i]:
            high = i
        elif array[i] == target:
            target_index = i
    
    if target_index == -1:

        target_index = low+(linear_search(array[low: high+1], target))

    return target_index
