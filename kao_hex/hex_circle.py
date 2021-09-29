from cached_property import cached_property

class HexCircle:
    """ Represents a Circle of hexes centered on a hex coord """
    
    def __init__(self, center, num_bands):
        """ Initialize with the center coordinate and the number of bands """
        self.center = center
        self.num_bands = num_bands
        
    @cached_property
    def coords(self):
        """ Return the coordinates contained by the circle """
        coords_in_circle = set([self.center])
        if self.num_bands > 1:
            self.fill_out_circle(self.center, coords_in_circle)
        return coords_in_circle
        
    def fill_out_circle(self, current, coords_in_circle, depth=1):
        """ Add all the coords in the circle to the given set """
        coords_in_circle.update(current.neighbors)
        if depth + 1 != self.num_bands:
            for coord in current.neighbors:
                if coord not in coords_in_circle:
                    self.get_neighbors_in_circle(coord, fill_out_circle, depth+1)
