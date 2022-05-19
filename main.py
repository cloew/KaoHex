import sys

from kao_hex import HexCircle, HexCoord, HexVector, find_neighbors, ring_around
from kao_hex.hex_grid_printer import HexGridPrinter


def main(args):
    center = HexVector(0,0,0)
    coord = HexVector(x=1,y=-1)
    print(coord)
    coord = HexVector(x=1,z=-1)
    print(coord)
    coord = HexVector(y=1,z=-1)
    print(coord)
    
    print(center + HexVector(y=1, z=-1))
    print(HexVector(x=1,y=-1) + HexVector(y=1, z=-1))
    
    print(find_neighbors(center))
    
    distantPoint = HexVector(x=2, y=10)
    otherPoint = HexVector(x=1, y=10)
    print(distantPoint.magnitude)
    print(distantPoint - otherPoint)
    print(otherPoint - distantPoint)
    
    l = HexVector(x=-1, z=1)
    tr = HexVector(y=1, z=-1)
    print(tr-l)
    print((tr-l).magnitude)
    
    coord = HexVector(x=1,y=-1)
    print(coord*5)
    print(5*coord)
    print(coord/5)
    print(5/coord)
    
    print(HexVector(x=1,y=-1) == HexVector(x=1,y=-1))
    print(HexVector(x=1,y=-1) != HexVector(x=1,y=-1))
    print(hash(HexVector(x=1,y=-1)), hash(HexVector(x=1,y=-1)))
    
    print(ring_around(center, 0))
    print(ring_around(center, 1))
    print(ring_around(center, 2))

    # coord = HexCoord(3, 3)
    # circle = HexCircle(coord, 1)
    # print(circle.coords)
    # circle2 = HexCircle(coord, 2)
    # circle3 = HexCircle(coord, 3)
    # print(circle2.coords)
    
    # printer = HexGridPrinter(rows=10, cols=10, cell_length=3, topright=HexCoord(-4, 9), long_row_first=False)
    # contents = {}
    
    # for x in range(-printer.cols*2, printer.cols*2):
        # for y in range(-printer.rows, printer.rows):
            # contents[HexCoord(x, y)] = "{}{}".format(("-" if x < 0 else "") + chr(ord("A") + abs(x)), y)
    
    # for hex in circle3.coords:
      # contents[hex] = "+2"
    
    # for hex in circle2.coords:
      # contents[hex] = "+1"
    
    # for hex in circle.coords:
      # contents[hex] = "+0"
    # printer.print_grid(contents)
    
if __name__ == '__main__':
    main(sys.argv[1:])
