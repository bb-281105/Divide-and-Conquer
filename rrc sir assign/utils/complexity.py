"""
Complexity Analysis for Algorithms
"""

class ComplexityAnalyzer:
    """Analyze time and space complexity of algorithms"""
    
    @staticmethod
    def get_complexity(algorithm_name):
        """Return complexity information for each algorithm"""
        complexities = {
            "Quick Sort": {
                "time_best": "O(n log n)",
                "time_avg": "O(n log n)",
                "time_worst": "O(n²)",
                "space": "O(log n)",
                "description": "Quick Sort picks a pivot and partitions the array around it.",
                "divide": "Partitions array into two subarrays based on pivot",
                "conquer": "Recursively sorts subarrays",
                "combine": "Subarrays are already in place after partitioning"
            },
            "Merge Sort": {
                "time_best": "O(n log n)",
                "time_avg": "O(n log n)",
                "time_worst": "O(n log n)",
                "space": "O(n)",
                "description": "Merge Sort divides array into halves, sorts them, then merges.",
                "divide": "Divides array into two equal halves",
                "conquer": "Recursively sorts both halves",
                "combine": "Merges two sorted halves"
            },
            "Insertion Sort": {
                "time_best": "O(n)",
                "time_avg": "O(n²)",
                "time_worst": "O(n²)",
                "space": "O(1)",
                "description": "Insertion Sort builds the final sorted array one item at a time.",
                "divide": "Divides array into sorted and unsorted parts",
                "conquer": "Inserts next element into correct position in sorted part",
                "combine": "Array becomes sorted after all insertions"
            },
            "Heap Sort": {
                "time_best": "O(n log n)",
                "time_avg": "O(n log n)",
                "time_worst": "O(n log n)",
                "space": "O(1)",
                "description": "Heap Sort uses a binary heap data structure to sort elements.",
                "divide": "Builds a max heap from the array",
                "conquer": "Repeatedly extracts maximum element from heap",
                "combine": "Extracted elements form sorted array"
            },
            "Binary Search": {
                "time_best": "O(1)",
                "time_avg": "O(log n)",
                "time_worst": "O(log n)",
                "space": "O(1)",
                "description": "Binary Search finds position of a target value within a sorted array.",
                "divide": "Divides search interval in half",
                "conquer": "Searches in the appropriate half",
                "combine": "Returns the found position or -1"
            },
            "Count Inversions": {
                "time_best": "O(n log n)",
                "time_avg": "O(n log n)",
                "time_worst": "O(n log n)",
                "space": "O(n)",
                "description": "Count Inversions counts how far an array is from being sorted.",
                "divide": "Divides array into two halves",
                "conquer": "Recursively counts inversions in each half",
                "combine": "Counts split inversions while merging"
            },
            "Find Max & Min": {
                "time_best": "O(n)",
                "time_avg": "O(n)",
                "time_worst": "O(n)",
                "space": "O(log n)",
                "description": "Finds both maximum and minimum elements using divide and conquer.",
                "divide": "Divides array into two halves",
                "conquer": "Finds max/min in each half recursively",
                "combine": "Compares max/min from both halves"
            },
            "Karatsuba Multiplication": {
                "time_best": "O(n^log₂3) ≈ O(n¹·⁵⁸)",
                "time_avg": "O(n^log₂3) ≈ O(n¹·⁵⁸)",
                "time_worst": "O(n^log₂3) ≈ O(n¹·⁵⁸)",
                "space": "O(log n)",
                "description": "Fast multiplication algorithm that reduces multiplication of two n-digit numbers.",
                "divide": "Splits numbers into high and low parts",
                "conquer": "Recursively computes three products",
                "combine": "Combines results with appropriate shifts"
            }
        }
        
        return complexities.get(algorithm_name, {})
    
    @staticmethod
    def get_time_complexity_chart():
        """Return time complexity comparison data"""
        return {
            "Algorithm": ["Quick Sort", "Merge Sort", "Insertion Sort", "Heap Sort", 
                         "Binary Search", "Count Inversions", "Find Max & Min", "Karatsuba"],
            "Best Case": ["O(n log n)", "O(n log n)", "O(n)", "O(n log n)", 
                         "O(1)", "O(n log n)", "O(n)", "O(n^1.58)"],
            "Average Case": ["O(n log n)", "O(n log n)", "O(n²)", "O(n log n)", 
                           "O(log n)", "O(n log n)", "O(n)", "O(n^1.58)"],
            "Worst Case": ["O(n²)", "O(n log n)", "O(n²)", "O(n log n)", 
                          "O(log n)", "O(n log n)", "O(n)", "O(n^1.58)"],
            "Space": ["O(log n)", "O(n)", "O(1)", "O(1)", 
                     "O(1)", "O(n)", "O(log n)", "O(log n)"]
        }