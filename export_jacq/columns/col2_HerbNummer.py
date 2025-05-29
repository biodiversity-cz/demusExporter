from .base import BaseStep
import pandas
class Column2_HerbNummer(BaseStep):

    _column_name="HerbNummer"

    def _convert_row(self, row) -> str:
        por_c = row.get('PorC_S', '')
        lomeni = row.get('Lomeni_S', '')
        if lomeni != '_':
            result = f"{por_c}/{lomeni}"
        else:
            result = por_c

        result_str = str(result)
        if len(result_str) < 7:
            result_str = result_str.zfill(7)
        return result_str

    def compute(self) -> pandas.DataFrame:
        result = self._sbirky.apply(
            lambda row: self._convert_row(row),
            axis=1
        )
        return pandas.DataFrame({self._column_name: result})
