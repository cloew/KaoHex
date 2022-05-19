from .cardinal_directions import CARDINAL_DIRECTIONS

def find_neighbors(hex):
    """ Find the neighbors of the given Hex """
    return [hex + direction for direction in CARDINAL_DIRECTIONS]
