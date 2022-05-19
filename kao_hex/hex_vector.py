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
        
    def __add__(self, other):
        """ Add this Hex Vector to another Vector """
        return HexVector(self.x+other.x, self.y+other.y)
        
    def __repr__(self):
        """ Return the String representation of the Grid Coord """
        return "<HexVector(x={}, y={}, z={})>".format(self.x, self.y, self.z)