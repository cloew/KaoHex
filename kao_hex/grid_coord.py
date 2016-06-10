
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
        
    @property
    def neighbors(self):
        """ Return the neighboring coordinates """
        return [GridCoord(x=self.x+1, y=self.y), GridCoord(x=self.x, y=self.y+1), GridCoord(x=self.x-1, y=self.y+1),
                GridCoord(x=self.x-1, y=self.y), GridCoord(x=self.x, y=self.y-1), GridCoord(x=self.x+1, y=self.y-1)]
        
    def __repr__(self):
        """ Return the String representation of the Grid Coord """
        return "<GridCoord(x={}, y={}, z={})>".format(self.x, self.y, self.z)