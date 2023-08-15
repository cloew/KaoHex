def _compute_third(first, second):
    """ Compute a third coordinate given the other two """
    return -first - second

class HexVector:
    """ Represents a Vector in Hex space """
    
    def __init__(self, x=None, y=None, z=None):
        """ Initialize the Hex Vector """
        self.x = x if x is not None else _compute_third(y, z)
        self.y = y if y is not None else _compute_third(x, z)
        
    @property
    def z(self):
        """ Return the z coordinate """
        return _compute_third(self.x, self.y)
        
    @property
    def magnitude(self):
        """ Return the magnitude of the vector """
        return (abs(self.x) + abs(self.y) + abs(self.z))//2
        
    def __add__(self, other):
        """ Add this Hex Vector to another Vector """
        return HexVector(self.x+other.x, self.y+other.y)
        
    def __sub__(self, other):
        """ Add this Hex Vector to another Vector """
        return HexVector(self.x-other.x, self.y-other.y)
        
    def __mul__(self, scalar):
        """ Multiply this hex vector times a scalar """
        return HexVector(self.x*scalar, self.y*scalar)
    __rmul__ = __mul__
        
    def __truediv__(self, scalar):
        """ Divide this hex vector by a scalar """
        return HexVector(self.x/scalar, self.y/scalar)
    __rtruediv__ = __truediv__
        
    def __round__(self):
        """ Return a rounded version of this HexVector """
        result = HexVector(round(self.x), round(self.y))
        print(self, result, (self.x, self.y), (round(self.x), round(self.y)))
        return result
        
    def __eq__(self, other):
        """ Return whether self and other are equal """
        return (self.x, self.y) == (other.x, other.y)
        
    def __ne__(self, other):
        """ Return whether self and other are not equal """
        return not self == other
        
    def __hash__(self):
        """ Return the hash code for the Coordinate """
        return hash((self.x, self.y))
        
    def __repr__(self):
        """ Return the String representation of the Grid Coord """
        return "<HexVector(x={}, y={}, z={})>".format(self.x, self.y, self.z)
