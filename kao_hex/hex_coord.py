
class HexCoord:
    """ Represents a Coordinate in a hex grid """
    
    def __init__(self, x=0, y=0):
        """ Initialize with the x and y coordinate """
        self.x = x
        self.y = y
        
    @property
    def z(self):
        """ Return the z coordinate """
        return -self.x - self.y
        
    @property
    def neighbors(self):
        """ Return the neighboring coordinates """
        return [HexCoord(x=self.x+1, y=self.y), HexCoord(x=self.x, y=self.y+1), HexCoord(x=self.x-1, y=self.y-1),
                HexCoord(x=self.x-1, y=self.y), HexCoord(x=self.x, y=self.y-1), HexCoord(x=self.x+1, y=self.y+1)]
        
    def coordsInRange(self, n):
        """ Return the coordinates in the given range """
        results = set()
        for dx in range(-n, n+1):
            for dy in range(max(-n, -n-dx), min(n, n-dx)+1):
                results.add(HexCoord(self.x+dx, self.y+dy))
        return results
                
    def distanceTo(self, other):
        """ Return the distance between two coordinates """
        return (abs(self.x-other.x) + abs(self.y-other.y) + abs(self.z-other.z))/2
        
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
        return "<HexCoord(x={}, y={}, z={})>".format(self.x, self.y, self.z)