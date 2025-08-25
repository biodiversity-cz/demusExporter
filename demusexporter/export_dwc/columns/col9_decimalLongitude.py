from .base import BaseStep
import pandas
import re


class DecimalLongitude(BaseStep):
    _column_name = "decimalLongitude"

    def compute(self) -> pandas.DataFrame:

        self._sbirky['Grid_'] = self._sbirky['Grid_S'].fillna('')
        self._sbirky['ZDelka_S'] = self._sbirky['ZDelka_S'].fillna('')
        result = self._sbirky.apply(
            lambda row: self.parse_row(row),
            axis=1
        )

        return pandas.DataFrame({self._column_name: result})

    def parse_row(self, row):
        grid = str(row.get('Grid_S', '')).strip()

        if not grid or grid != 'WGS-84':
            return None


        lon = self.parse_coord(row.get('ZDelka_S', ''))

        return lon

    def parse_coord(self, value):
        if not value or pandas.isna(value):
            return None
        if len(value) == 8 and value[1] == '0':
            raw = value[0] + value[2:]
        else:
            raw = value

        cleaned = re.sub(r'[?#\s]', '', str(raw).strip())

        if not cleaned or len(cleaned) < 3:
            return None

        direction = cleaned[0].upper()
        if direction not in {'N', 'S', 'E', 'W'}:
            return ['Neznámý směr']

        digits = cleaned[1:]
        if not digits[:2].isdigit():
            return ['Chyba ve stupních']

        try:
            deg = float(digits[0:2])
            min_ = float(digits[2:4]) if len(digits) >= 4 else 0
            sec = float(digits[4:]) if len(digits) == 6 else 0

            number = deg + (min_ / 60.0) + (sec / 3600.0)
            if 'S' in direction or 'W' in direction or '-' in direction:
                number = -abs(number)
        except ValueError:
            return ['Chyba při převodu']

        return number