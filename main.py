import sys

from kao_hex import HexVector, find_neighbors, line_to, ring_around, range_around, steps_to
from kao_hex.hex_grid_printer import HexGridPrinter


def main(args):
    center = HexVector(0,0,0)
    
    # destination = HexVector(0,1,0)
    # path = line_to(destination, start=center)
    # print(path)
    
    # destination = HexVector(-2,1,0)
    # path = line_to(destination, start=center)
    # print(path)
    
    # destination = HexVector(-2,3,0)
    # path = line_to(destination, start=center)
    # print(path)
    
    # destination = HexVector(-2,3,0)*2
    # path = line_to(destination, start=center)
    # print(path)
    
    destination = HexVector(1,-2,0)*2
    path = line_to(destination, start=center)
    print(path)
    
    print(steps_to(destination, start=center))
    
    # coord = HexVector(x=1,y=-1)
    # print(coord)
    # coord = HexVector(x=1,z=-1)
    # print(coord)
    # coord = HexVector(y=1,z=-1)
    # print(coord)
    
    # print(center + HexVector(y=1, z=-1))
    # print(HexVector(x=1,y=-1) + HexVector(y=1, z=-1))
    
    # print(find_neighbors(center))
    
    # distantPoint = HexVector(x=2, y=10)
    # otherPoint = HexVector(x=1, y=10)
    # print(distantPoint.magnitude)
    # print(distantPoint - otherPoint)
    # print(otherPoint - distantPoint)
    
    # l = HexVector(x=-1, z=1)
    # tr = HexVector(y=1, z=-1)
    # print(tr-l)
    # print((tr-l).magnitude)
    
    # coord = HexVector(x=1,y=-1)
    # print(coord*5)
    # print(5*coord)
    # print(coord/5)
    # print(5/coord)
    
    # print(HexVector(x=1,y=-1) == HexVector(x=1,y=-1))
    # print(HexVector(x=1,y=-1) != HexVector(x=1,y=-1))
    # print(hash(HexVector(x=1,y=-1)), hash(HexVector(x=1,y=-1)))
    
    # print(ring_around(center, 0))
    # print(ring_around(center, 1))
    # print(ring_around(center, 2))
    
    # rangeCells = range_around(center, 2)
    # print(rangeCells, len(rangeCells))
    
    # coord = HexVector(3, 3)
    # circle = range_around(coord, 0)
    # circle1 = range_around(coord, 1)
    # circle2 = range_around(coord, 2)
    
    # printer = HexGridPrinter(rows=10, cols=10, cell_length=3, topright=HexVector(-4, 9), long_row_first=False)
    # contents = {}
    
    # for x in range(-printer.cols*2, printer.cols*2):
        # for y in range(-printer.rows, printer.rows):
            # contents[HexVector(x, y)] = "{}{}".format(("-" if x < 0 else "") + chr(ord("A") + abs(x)), y)
    
    # for hex in circle2:
      # contents[hex] = "+2"
    
    # for hex in circle1:
      # contents[hex] = "+1"
    
    # for hex in circle:
      # contents[hex] = "+0"
    # printer.print_grid(contents)
    
if __name__ == '__main__':
    main(sys.argv[1:])
