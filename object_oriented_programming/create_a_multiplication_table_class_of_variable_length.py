class MultiplicationTable:

    _table: list[list[int]]

    def __init__(self, length: int):
        """Create a 2D self._table of (x, y) coordinates and
           their calculations (form of caching)"""
        self._table = []
        for row in range(length):
            self._table.append([])
            for col in range(length):
                self._table[row].append((row + 1) * (col + 1))

    def __len__(self):
        """Returns the area of the table (len x* len y)"""
        return len(self._table[0]) * len(self._table)

    def __str__(self):
        """Returns a string representation of the table"""
        res = ""
        for row in range(len(self._table)):
            line = ""
            for col in range(len(self._table[0])):
                line += str(self._table[row][col]) + " | "
            res +=line.rstrip(" | ") + "\n"
        return res.strip()

    def calc_cell(self, x, y):
        """Takes x and y coords and returns the re-calculated result"""
        if len(self._table[0]) < x or len(self._table) < y:
            raise IndexError
        return self._table[0][x - 1] * self._table[y - 1][0]