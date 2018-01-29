from string import letters
from excel import OpenExcel
from inputoutput import IO

class XLSXOpenExcel(IO):

    def read(self, filename):
        self.sheet = OpenExcel(filename)
        self.row_count = self.sheet.read().nrows
        self.col_count = self.sheet.read().ncols

    def _float_to_string(self, sheet, col):
        values = sheet.read(col)
        if values[0] in self.column_names:
            return values
        for i, value in enumerate(values):
            if isinstance(value, float):
                values[i] = str(int(value))
            elif isinstance(value, unicode):
                values[i] = str(value)
        return values

    def column_heading_letter(self, heading_name):
        for letter in self.column_letters():
            if self.sheet.read(letter)[0] == heading_name:
                return letter

    @property
    def column_names(self):
        return tuple(
            [col[0] for col in [self.sheet.sheets.col_values(i) for i in
             range(self.sheet.getCols())]])

    @property
    def column_letters(self):
        _letters = letters[26:]
        num_cols = self.sheet.read().ncols
        double_letters, triple_letters = ([],) * 2
        for l in _letters:
            for m in _letters:
                double_letters += [l + m]
        for l in _letters:
            for m in _letters:
                for n in _letters:
                    triple_letters += [l + m + n]
        _letters = list(_letters) + double_letters + triple_letters
        res = zip(_letters, range(1, num_cols))
        return tuple([r[0] for r in res])
