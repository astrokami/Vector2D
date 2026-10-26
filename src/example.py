"""Example usage of the Vector2D class."""
# testing script
# testing feature dev branch 
from vector import Vector2D


if __name__ == "__main__":
    # Create vectors
    v1 = Vector2D(3, 4)
    v2 = Vector2D(1, 2)
    print()
    
    print("=== Vector Creation ===")
    print(f"Vector 1: {v1}")
    print(f"Vector 2: {v2}")
    print()
    
    # Addition
    print("=== Addition ===")
    v_sum = v1 + v2
    print(f"{v1} + {v2} = {v_sum}")
    print()
    
    # Subtraction
    print("=== Subtraction ===")
    v_diff = v1 - v2
    print(f"{v1} - {v2} = {v_diff}")
    print()
    
    # Scalar multiplication
    print("=== Scalar Multiplication ===")
    v_scaled = v1 * 2
    print(f"{v1} * 2 = {v_scaled}")
    print()
    
    # Magnitude
    print("=== Magnitude ===")
    mag = v1.magnitude()
    print(f"Magnitude of {v1} = {mag}")
    print()
    
    # Dot product
    print("=== Dot Product ===")
    dot = v1.dot(v2)
    print(f"{v1} · {v2} = {dot}")
    print()
    
    # Normalization
    print("=== Normalization ===")
    v_normalized = v1.normalize()
    print(f"Normalized {v1} = {v_normalized}")
    print(f"Magnitude of normalized vector = {v_normalized.magnitude()}")
    print()
    
    # Distance
    print("=== Distance ===")
    distance = v1.distance_to(v2)
    print(f"Distance between {v1} and {v2} = {distance}")
    print()
    
    # Copy
    print("=== Copy ===")
    v_copy = v1.copy()
    print(f"Original: {v1}")
    print(f"Copy: {v_copy}")
    print(f"Are they equal? {v1 == v_copy}")
    print()
