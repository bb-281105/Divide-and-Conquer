"""
Mathematical Algorithms using Divide and Conquer
"""

class MathAlgorithms:
    """Class containing mathematical divide and conquer algorithms"""
    
    @staticmethod
    def karatsuba_multiply(x, y, steps=None):
        """Karatsuba Multiplication Algorithm"""
        if steps is not None:
            steps.append(f"Multiplying {x} × {y}")
        
        # Base case for single digit numbers
        if x < 10 or y < 10:
            return x * y
        
        # Calculate the size of the numbers
        n = max(len(str(x)), len(str(y)))
        m = n // 2
        
        # Split the digit sequences
        high1 = x // 10**m
        low1 = x % 10**m
        high2 = y // 10**m
        low2 = y % 10**m
        
        if steps is not None:
            steps.append(f"Split: x={high1}*10^{m} + {low1}, y={high2}*10^{m} + {low2}")
        
        # 3 recursive calls
        z0 = MathAlgorithms.karatsuba_multiply(low1, low2, steps)
        z1 = MathAlgorithms.karatsuba_multiply((low1 + high1), (low2 + high2), steps)
        z2 = MathAlgorithms.karatsuba_multiply(high1, high2, steps)
        
        if steps is not None:
            steps.append(f"z0 = {low1}×{low2} = {z0}")
            steps.append(f"z1 = ({low1}+{high1})×({low2}+{high2}) = {z1}")
            steps.append(f"z2 = {high1}×{high2} = {z2}")
        
        # Combine the results
        result = (z2 * 10**(2*m)) + ((z1 - z2 - z0) * 10**m) + z0
        
        if steps is not None:
            steps.append(f"Result = z2*10^{2*m} + (z1-z2-z0)*10^{m} + z0 = {result}")
        
        return result