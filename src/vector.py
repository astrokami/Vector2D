import math


class Vector2D:
    """A 2D vector class with common vector operations."""
    
    def __init__(self, x=0.0, y=0.0):
        """Initialize a 2D vector with x and y components.
        
        Args:
            x (float): X component of the vector. Default is 0.0.
            y (float): Y component of the vector. Default is 0.0.
        """
        self.x = float(x)
        self.y = float(y)
    
    def __repr__(self):
        """Return string representation of the vector."""
        return f"Vector2D({self.x}, {self.y})"
    
    def __str__(self):
        """Return readable string format."""
        return f"({self.x}, {self.y})"
    
    def __add__(self, other):
        """Add two vectors together.
        
        Args:
            other (Vector2D): Vector to add.
            
        Returns:
            Vector2D: New vector representing the sum.
        """
        if not isinstance(other, Vector2D):
            raise TypeError(f"Cannot add Vector2D and {type(other).__name__}")
        return Vector2D(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """Subtract one vector from another.
        
        Args:
            other (Vector2D): Vector to subtract.
            
        Returns:
            Vector2D: New vector representing the difference.
        """
        if not isinstance(other, Vector2D):
            raise TypeError(f"Cannot subtract {type(other).__name__} from Vector2D")
        return Vector2D(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        """Multiply vector by a scalar value.
        
        Args:
            scalar (float): Scalar value to multiply by.
            
        Returns:
            Vector2D: New scaled vector.
        """
        if not isinstance(scalar, (int, float)):
            raise TypeError(f"Cannot multiply Vector2D by {type(scalar).__name__}")
        return Vector2D(self.x * scalar, self.y * scalar)
    
    def __rmul__(self, scalar):
        """Support scalar * vector syntax.
        
        Args:
            scalar (float): Scalar value to multiply by.
            
        Returns:
            Vector2D: New scaled vector.
        """
        return self.__mul__(scalar)
    
    def __truediv__(self, scalar):
        """Divide vector by a scalar value.
        
        Args:
            scalar (float): Scalar value to divide by.
            
        Returns:
            Vector2D: New scaled vector.
        """
        if not isinstance(scalar, (int, float)):
            raise TypeError(f"Cannot divide Vector2D by {type(scalar).__name__}")
        if scalar == 0:
            raise ValueError("Cannot divide by zero")
        return Vector2D(self.x / scalar, self.y / scalar)
    
    def __eq__(self, other):
        """Check if two vectors are equal.
        
        Args:
            other (Vector2D): Vector to compare with.
            
        Returns:
            bool: True if vectors have same components, False otherwise.
        """
        if not isinstance(other, Vector2D):
            return False
        return math.isclose(self.x, other.x) and math.isclose(self.y, other.y)
    
    def magnitude(self):
        """Calculate the magnitude (length) of the vector.
        
        Returns:
            float: The magnitude of the vector.
        """
        return math.sqrt(self.x**2 + self.y**2)
    
    def length(self):
        """Alias for magnitude(). Calculate the length of the vector.
        
        Returns:
            float: The length of the vector.
        """
        return self.magnitude()
    
    def dot(self, other):
        """Calculate the dot product with another vector.
        
        Args:
            other (Vector2D): Vector to calculate dot product with.
            
        Returns:
            float: The dot product.
        """
        if not isinstance(other, Vector2D):
            raise TypeError(f"Cannot calculate dot product with {type(other).__name__}")
        return self.x * other.x + self.y * other.y
    
    def normalize(self):
        """Normalize the vector to unit length (magnitude = 1).
        
        Returns:
            Vector2D: New normalized vector.
            
        Raises:
            ValueError: If the vector has zero magnitude.
        """
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector")
        return self / mag
    
    def distance_to(self, other):
        """Calculate the distance between this vector and another.
        
        Args:
            other (Vector2D): The other vector.
            
        Returns:
            float: The distance between the two vectors.
        """
        if not isinstance(other, Vector2D):
            raise TypeError(f"Cannot calculate distance to {type(other).__name__}")
        return (self - other).magnitude()
    
    def copy(self):
        """Create a copy of this vector.
        
        Returns:
            Vector2D: A new independent copy of this vector.
        """
        return Vector2D(self.x, self.y)
