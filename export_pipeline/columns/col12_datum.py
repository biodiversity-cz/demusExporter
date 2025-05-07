from .base import BaseStep
import pandas
class Column12_datum(BaseStep):

    _column_name="datum"

    def compute(self) -> pandas.DataFrame:
        self._sbirky['DatSberu_SX'] = self._sbirky['DatSberu_SX'].fillna('s.d.')

        result = self._sbirky.apply(
            lambda row: str(row.get('DatSberu_SX', '')).strip(),
            axis=1
        )

        return pandas.DataFrame({self._column_name: result})
