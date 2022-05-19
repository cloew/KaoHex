from .hex_vector import HexVector

CARDINAL_DIRECTIONS = [
    HexVector(x=1, y=-1),
    HexVector(x=1, z=-1),
    HexVector(y=1, z=-1),
    HexVector(x=-1, y=1),
    HexVector(x=-1, z=1),
    HexVector(y=-1, z=1),
]
