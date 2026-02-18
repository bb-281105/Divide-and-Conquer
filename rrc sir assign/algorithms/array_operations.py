"""
Array Operations using Divide and Conquer
"""

class ArrayOperations:
    """Class containing array operations using divide and conquer"""
    
    @staticmethod
    def count_inversions(arr, steps=None):
        """Count Inversions Algorithm"""
        if steps is not None:
            steps.append(f"Counting inversions in: {arr}")
        
        if len(arr) <= 1:
            return arr, 0
        
        mid = len(arr) // 2
        left, inv_left = ArrayOperations.count_inversions(arr[:mid], steps)
        right, inv_right = ArrayOperations.count_inversions(arr[mid:], steps)
        merged, inv_split = ArrayOperations._count_split_inversions(left, right, steps)
        
        total_inversions = inv_left + inv_right + inv_split
        
        if steps is not None:
            steps.append(f"Left inversions: {inv_left}, Right inversions: {inv_right}, Split inversions: {inv_split}")
            steps.append(f"Total inversions: {total_inversions}")
        
        return merged, total_inversions
    
    @staticmethod
    def _count_split_inversions(left, right, steps=None):
        """Count split inversions helper"""
        merged = []
        i = j = 0
        inversions = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                inversions += len(left) - i
                j += 1
        
        merged.extend(left[i:])
        merged.extend(right[j:])
        
        if steps is not None:
            steps.append(f"Merged {left} and {right} with {inversions} split inversions")
        
        return merged, inversions
    
    @staticmethod
    def find_max_min(arr, steps=None, low=0, high=None):
        """Find maximum and minimum in array"""
        if high is None:
            high = len(arr) - 1
        
        if steps is not None:
            steps.append(f"Finding max/min in subarray {arr[low:high+1]}")
        
        # Base cases
        if low == high:  # Only one element
            return arr[low], arr[low]
        
        if high == low + 1:  # Two elements
            if arr[low] < arr[high]:
                return arr[low], arr[high]
            else:
                return arr[high], arr[low]
        
        # Divide
        mid = (low + high) // 2
        min1, max1 = ArrayOperations.find_max_min(arr, steps, low, mid)
        min2, max2 = ArrayOperations.find_max_min(arr, steps, mid + 1, high)
        
        # Conquer
        overall_min = min(min1, min2)
        overall_max = max(max1, max2)
        
        if steps is not None:
            steps.append(f"Subarray {arr[low:high+1]}: min={overall_min}, max={overall_max}")
        
        return overall_min, overall_max