"""
Helper functions for the application
"""
import random
import time

class HelperFunctions:
    """Helper functions for algorithm operations"""
    
    @staticmethod
    def generate_random_array(size=10, min_val=1, max_val=100):
        """Generate a random array of given size"""
        return [random.randint(min_val, max_val) for _ in range(size)]
    
    @staticmethod
    def format_array(arr):
        """Format array for display"""
        return ', '.join(map(str, arr))
    
    @staticmethod
    def parse_input(input_str):
        """Parse comma-separated input string into list of integers"""
        try:
            return [int(x.strip()) for x in input_str.split(',') if x.strip()]
        except ValueError:
            return []
    
    @staticmethod
    def measure_execution_time(func, *args, **kwargs):
        """Measure execution time of a function"""
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        return result, (end_time - start_time) * 1000  # Convert to milliseconds
    
    @staticmethod
    def get_algorithm_info(algorithm_name):
        """Get information about algorithm"""
        info = {
            "Quick Sort": "Efficient, in-place sorting algorithm using pivot",
            "Merge Sort": "Stable sorting algorithm with guaranteed O(n log n)",
            "Insertion Sort": "Simple sorting good for small or nearly sorted arrays",
            "Heap Sort": "Uses heap data structure for sorting",
            "Binary Search": "Fast search algorithm for sorted arrays",
            "Count Inversions": "Measures how far array is from being sorted",
            "Find Max & Min": "Finds both maximum and minimum efficiently",
            "Karatsuba Multiplication": "Fast multiplication for large numbers"
        }
        return info.get(algorithm_name, "")