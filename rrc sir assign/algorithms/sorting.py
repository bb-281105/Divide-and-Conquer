"""
Sorting Algorithms using Divide and Conquer
"""
import copy

class SortingAlgorithms:
    """Class containing divide and conquer sorting algorithms"""
    
    @staticmethod
    def quick_sort(arr, steps=None, low=0, high=None):
        """Quick Sort Algorithm"""
        if high is None:
            high = len(arr) - 1
            if steps is not None:
                steps.append(f"Starting Quick Sort on: {arr}")
        
        if low < high:
            # Partition the array
            pivot_index = SortingAlgorithms._partition(arr, low, high, steps)
            
            if steps is not None:
                steps.append(f"Partitioned: {arr[low:high+1]} with pivot at index {pivot_index}")
            
            # Recursively sort elements before and after partition
            SortingAlgorithms.quick_sort(arr, steps, low, pivot_index - 1)
            SortingAlgorithms.quick_sort(arr, steps, pivot_index + 1, high)
        
        return arr
    
    @staticmethod
    def _partition(arr, low, high, steps=None):
        """Partition helper for quick sort"""
        pivot = arr[high]
        if steps is not None:
            steps.append(f"Pivot selected: {pivot}")
        
        i = low - 1
        
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    @staticmethod
    def merge_sort(arr, steps=None):
        """Merge Sort Algorithm"""
        if steps is not None:
            steps.append(f"Merge Sort on: {arr}")
        
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        
        if steps is not None:
            steps.append(f"Divided into left: {left}, right: {right}")
        
        left = SortingAlgorithms.merge_sort(left, steps)
        right = SortingAlgorithms.merge_sort(right, steps)
        
        return SortingAlgorithms._merge(left, right, steps)
    
    @staticmethod
    def _merge(left, right, steps=None):
        """Merge helper for merge sort"""
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        
        if steps is not None:
            steps.append(f"Merged {left} and {right} into {result}")
        
        return result
    
    @staticmethod
    def insertion_sort(arr, steps=None):
        """Insertion Sort Algorithm"""
        if steps is not None:
            steps.append(f"Starting Insertion Sort on: {arr}")
        
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            
            if steps is not None:
                steps.append(f"Inserting {key} into correct position")
            
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            
            arr[j + 1] = key
            
            if steps is not None:
                steps.append(f"After inserting {key}: {arr[:i+1]}")
        
        return arr
    
    @staticmethod
    def heap_sort(arr, steps=None):
        """Heap Sort Algorithm"""
        if steps is not None:
            steps.append(f"Starting Heap Sort on: {arr}")
        
        n = len(arr)
        
        # Build max heap
        for i in range(n // 2 - 1, -1, -1):
            SortingAlgorithms._heapify(arr, n, i, steps)
        
        if steps is not None:
            steps.append(f"Max heap built: {arr}")
        
        # Extract elements from heap
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # Swap
            if steps is not None:
                steps.append(f"Swapped root {arr[i]} with last element {arr[0]}")
            SortingAlgorithms._heapify(arr, i, 0, steps)
        
        return arr
    
    @staticmethod
    def _heapify(arr, n, i, steps=None):
        """Heapify helper for heap sort"""
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arr[left] > arr[largest]:
            largest = left
        
        if right < n and arr[right] > arr[largest]:
            largest = right
        
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            if steps is not None:
                steps.append(f"Heapified: swapped {arr[i]} with {arr[largest]}")
            SortingAlgorithms._heapify(arr, n, largest, steps)