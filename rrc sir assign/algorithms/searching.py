"""
Searching Algorithms using Divide and Conquer
"""

class SearchingAlgorithms:
    """Class containing divide and conquer searching algorithms"""
    
    @staticmethod
    def binary_search(arr, target, steps=None, low=0, high=None):
        """Binary Search Algorithm"""
        if high is None:
            high = len(arr) - 1
        
        if steps is not None:
            steps.append(f"Searching for {target} in subarray {arr[low:high+1]}")
        
        if low > high:
            if steps is not None:
                steps.append(f"Target {target} not found")
            return -1
        
        mid = (low + high) // 2
        
        if steps is not None:
            steps.append(f"Middle element at index {mid} is {arr[mid]}")
        
        if arr[mid] == target:
            if steps is not None:
                steps.append(f"Found {target} at index {mid}")
            return mid
        elif arr[mid] > target:
            if steps is not None:
                steps.append(f"{arr[mid]} > {target}, searching left half")
            return SearchingAlgorithms.binary_search(arr, target, steps, low, mid - 1)
        else:
            if steps is not None:
                steps.append(f"{arr[mid]} < {target}, searching right half")
            return SearchingAlgorithms.binary_search(arr, target, steps, mid + 1, high)