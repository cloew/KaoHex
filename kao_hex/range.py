from .cardinal_directions import CARDINAL_DIRECTIONS
from .ring import ring_around

def range_around(center, distance):
    """ Return all the hexes in the given distance range of the given center """
    range_hexes = []
    for i in range(distance+1):
        ring_hexes = ring_around(center, i)
        range_hexes.extend(ring_hexes)
    return range_hexes
