from .base import BaseStep
import pandas
class Column14_det(BaseStep):

    _column_name="det"

    def compute(self) -> pandas.DataFrame:
        self._sbirky['Urcil_SX'] = self._sbirky['Urcil_SX'].fillna('')

        result = self._sbirky.apply(
            lambda row: str(row.get('Urcil_SX', '')).strip(),
            axis=1
        )

        return pandas.DataFrame({self._column_name: result})
