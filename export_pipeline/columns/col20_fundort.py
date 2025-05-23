from .base import BaseStep
import pandas
class Column20_Fundort(BaseStep):

    _column_name="Fundort"

    def compute(self) -> pandas.DataFrame:
        self._sbirky['Lokalita_SX'] = self._sbirky['Lokalita_SX'].fillna('')
        result = self._sbirky.apply(
            lambda row: f"{row.get('Lokalita_SX', '')}".strip(),
            axis=1
        )

        return pandas.DataFrame({self._column_name: result})
