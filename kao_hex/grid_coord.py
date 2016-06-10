
class GridCoord:
    """ Represents a Coordinate in a grid """
    
    def __init__(self, x=0, y=0):
        """ Initialize with the x and y coordinate """
        self.x = x
        self.y = y
        
    @property
    def z(self):
        """ Return the z coordinate """
        return -self.x - self.y
        
    def __repr__(self):
        """ Return the String representation of the Grid Coord """
        return "<GridCoord(x={}, y={}, z={})>".format(self.x, self.y, self.z)