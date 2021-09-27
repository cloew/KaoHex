from .hex_coord import HexCoord

class HexGridPrinter:
    """ Helper class to print a hex grid to the console """
    
    def __init__(self, *, rows, cols, cell_length=3, empty=" ", long_row_first=True):
        """ Initialize the HexGridPrinter with the grid size (in rows/cols) and the size of each cell and what to print if the cell is empty """
        self.rows = rows
        self.cols = cols
        self.long_row_first = long_row_first
        self.cell_length = cell_length
        self.empty = empty

    def print_grid(self, coord_to_content):
        """ Print the hex grid with the given contents """
        spacer = " "*self.cell_length
        for row in range(self.rows):
            content = self.build_contents_for_row(row, coord_to_content)
            text_content = spacer.join(content)
            if not self.is_long_row(row):
                text_content = spacer + text_content
            print(text_content)        
        
    def build_contents_for_row(self, x, coord_to_content):
        """ Build the contents for the given x row """
        row_contents = []
        cols_in_row = self.get_num_cols_for_row(x)
        for dy in range(cols_in_row + 1):
            coord = HexCoord(x=x, y=x+dy)
            content = self.get_coord_content(coord, coord_to_content)
            row_contents.append(content)
        return row_contents
        
    def get_coord_content(self, coord, coord_to_content):
        """ Return the coord content """
        return str(coord_to_content[coord]).ljust(self.cell_length)[:self.cell_length] if coord in coord_to_content else self.empty*self.cell_length
    
    def get_num_cols_for_row(self, x):
        """ Return the number of cols in row x """
        return self.cols if self.is_long_row(x) else self.cols - 1

    def is_long_row(self, x):
        """ Return if the given row is a long row """
        return not x%2 if self.long_row_first else x%2
