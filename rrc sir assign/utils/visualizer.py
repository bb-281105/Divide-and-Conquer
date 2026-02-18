"""
Visualization functions for algorithms
"""
import matplotlib.pyplot as plt
import numpy as np

class AlgorithmVisualizer:
    """Class for visualizing algorithm operations"""
    
    @staticmethod
    def plot_sorting_comparison(original, sorted_arr, algorithm_name):
        """Plot comparison of original vs sorted array"""
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))
        
        # Original array
        bars1 = ax1.bar(range(len(original)), original, color='skyblue', alpha=0.7, edgecolor='black')
        ax1.set_title(f"Original Array", fontsize=14, fontweight='bold')
        ax1.set_xlabel("Index")
        ax1.set_ylabel("Value")
        ax1.grid(True, alpha=0.3)
        
        # Sorted array
        bars2 = ax2.bar(range(len(sorted_arr)), sorted_arr, color='lightgreen', alpha=0.7, edgecolor='black')
        ax2.set_title(f"Sorted Array ({algorithm_name})", fontsize=14, fontweight='bold')
        ax2.set_xlabel("Index")
        ax2.set_ylabel("Value")
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        return fig
    
    @staticmethod
    def plot_binary_search(arr, target_idx, target_value):
        """Visualize binary search result"""
        fig, ax = plt.subplots(figsize=(10, 4))
        
        colors = ['lightblue'] * len(arr)
        if target_idx != -1:
            colors[target_idx] = 'red'
        
        bars = ax.bar(range(len(arr)), arr, color=colors, alpha=0.7, edgecolor='black')
        ax.set_title(f"Binary Search: Target {target_value} {'Found' if target_idx != -1 else 'Not Found'}", 
                    fontsize=14, fontweight='bold')
        ax.set_xlabel("Index")
        ax.set_ylabel("Value")
        ax.grid(True, alpha=0.3)
        
        if target_idx != -1:
            ax.annotate(f'Target Found!', xy=(target_idx, arr[target_idx]),
                       xytext=(target_idx+0.5, arr[target_idx]+5),
                       arrowprops=dict(facecolor='black', shrink=0.05),
                       fontsize=12, fontweight='bold')
        
        plt.tight_layout()
        return fig
    
    @staticmethod
    def plot_max_min(arr, min_val, max_val):
        """Visualize maximum and minimum in array"""
        fig, ax = plt.subplots(figsize=(10, 4))
        
        colors = ['lightblue'] * len(arr)
        min_indices = [i for i, val in enumerate(arr) if val == min_val]
        max_indices = [i for i, val in enumerate(arr) if val == max_val]
        
        for idx in min_indices:
            colors[idx] = 'green'
        for idx in max_indices:
            colors[idx] = 'red'
        
        bars = ax.bar(range(len(arr)), arr, color=colors, alpha=0.7, edgecolor='black')
        ax.set_title(f"Find Max & Min: Min={min_val} (green), Max={max_val} (red)", 
                    fontsize=14, fontweight='bold')
        ax.set_xlabel("Index")
        ax.set_ylabel("Value")
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        return fig
    
    @staticmethod
    def plot_time_complexity():
        """Plot time complexity comparison chart"""
        algorithms = ["Quick Sort", "Merge Sort", "Insertion Sort", "Heap Sort", 
                     "Binary Search", "Count Inversions", "Max/Min", "Karatsuba"]
        
        # Approximate time complexities for comparison
        n_sizes = [10, 50, 100, 500, 1000]
        
        # This is a simplified visualization
        fig, ax = plt.subplots(figsize=(12, 6))
        
        # Sample data for visualization
        x = np.arange(len(algorithms))
        width = 0.25
        
        # Mock data for visualization purposes
        time_small = [15, 12, 8, 14, 3, 16, 6, 10]
        time_medium = [45, 38, 95, 42, 5, 44, 18, 32]
        time_large = [120, 98, 450, 105, 7, 112, 35, 85]
        
        ax.bar(x - width, time_small, width, label='Small (n=100)', color='lightblue')
        ax.bar(x, time_medium, width, label='Medium (n=1000)', color='lightgreen')
        ax.bar(x + width, time_large, width, label='Large (n=10000)', color='salmon')
        
        ax.set_xlabel('Algorithms', fontsize=12)
        ax.set_ylabel('Relative Time', fontsize=12)
        ax.set_title('Algorithm Time Complexity Comparison', fontsize=14, fontweight='bold')
        ax.set_xticks(x)
        ax.set_xticklabels(algorithms, rotation=45, ha='right')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        return fig