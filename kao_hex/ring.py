from .cardinal_directions import CARDINAL_DIRECTIONS

def ring_around(center, distance):
    """ Return all the hexes in a ring around the given center at the given distance """
    if distance == 0:
        return [center]
        
    ring_hexes = []
    current = center + distance*CARDINAL_DIRECTIONS[0]
    centerToCurrentCorner = CARDINAL_DIRECTIONS[0]
    
    for centerToNextCorner in CARDINAL_DIRECTIONS[1:] + [centerToCurrentCorner]:
        cornerToNextCorner =  centerToNextCorner - centerToCurrentCorner
        for i in range(distance):
            ring_hexes.append(current)
            current = current + cornerToNextCorner
        centerToCurrentCorner = centerToNextCorner
    return ring_hexes
