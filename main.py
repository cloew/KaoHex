import sys

from kao_hex import HexCircle, HexCoord
from kao_hex.hex_grid_printer import HexGridPrinter


def main(args):
    coord = HexCoord(5, 3)
    circle = HexCircle(coord, 1)
    print(circle.coords)
    circle2 = HexCircle(coord, 2)
    circle3 = HexCircle(coord, 3)
    print(circle2.coords)
    printer = HexGridPrinter(rows=10, cols=6, cell_length=2)
    contents = {
        HexCoord(0, 0): "A0",
        HexCoord(0, 1): "B0",
        HexCoord(0, 2): "C0",
        HexCoord(0, 3): "D0",
        HexCoord(0, 4): "E0",
        HexCoord(1, 1): "B1",
        HexCoord(1, 2): "C1",
        HexCoord(1, 3): "D1",
        HexCoord(1, 4): "E1",
        HexCoord(2, 2): "B2",
        HexCoord(2, 3): "C2",
        HexCoord(2, 4): "D2",
        HexCoord(2, 5): "E2",
        HexCoord(2, 6): "F2",
        HexCoord(3, 3): "C3",
        HexCoord(3, 4): "D3",
        HexCoord(3, 5): "E3",
        HexCoord(3, 6): "F3",
    }
    
    # for hex in circle3.coords:
      # contents[hex] = "C3"
    
    # for hex in circle2.coords:
      # contents[hex] = "C2"
    
    # for hex in circle.coords:
      # contents[hex] = "C1"
    printer.print_grid(contents)
    
if __name__ == '__main__':
    main(sys.argv[1:])
