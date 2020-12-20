def linear_search(array: list, query: int or float) -> int:
    """Linear Search Algorithm 
    In computer science, a linear search or sequential search is a method for finding an element within a list. It sequentially checks each 
    element of the list until a match is found or the whole list has been searched
    In this algorithm if the value is found then it returns index of the target as a value and if not found returns -1.
    Time Taken in worse case : O(n)
    Space Taken in worse case : O(n)
    """
    
    try:
        return array.index(query)
    except ValueError:
        return -1

