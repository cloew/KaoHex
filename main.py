import sys

from kao_hex import HexCircle, HexCoord
from kao_hex.hex_grid_printer import HexGridPrinter


def main(args):
    coord = HexCoord(3, 3)
    circle = HexCircle(coord, 1)
    print(circle.coords)
    circle2 = HexCircle(coord, 2)
    circle3 = HexCircle(coord, 3)
    print(circle2.coords)
    
    printer = HexGridPrinter(rows=10, cols=10, cell_length=3, topright=HexCoord(-4, 9), long_row_first=False)
    contents = {}
    
    for x in range(-printer.cols*2, printer.cols*2):
        for y in range(-printer.rows, printer.rows):
            contents[HexCoord(x, y)] = "{}{}".format(("-" if x < 0 else "") + chr(ord("A") + abs(x)), y)
    
    for hex in circle3.coords:
      contents[hex] = "+2"
    
    for hex in circle2.coords:
      contents[hex] = "+1"
    
    for hex in circle.coords:
      contents[hex] = "+0"
    printer.print_grid(contents)
    
if __name__ == '__main__':
    main(sys.argv[1:])
