from .base import BaseStep
import pandas

class Column19_provinz(BaseStep):

    _column_name="provinz"

    def compute(self) -> pandas.DataFrame:
        self._sbirky['Okres_SX'] = self._sbirky['Okres_SX'].fillna('')
        result = self._sbirky.apply(
            lambda row: f"{row.get('Okres_SX', '')}".strip(),
            axis=1
        )

        return pandas.DataFrame({self._column_name: result})
