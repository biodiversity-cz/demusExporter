from .base import BaseStep
import pandas
class Column11_alt_number(BaseStep):

    _column_name="alt_number"

    def compute(self) -> pandas.DataFrame:
        self._sbirky['JinaC_SX'] = self._sbirky['JinaC_SX'].fillna('')

        result = self._sbirky.apply(
            lambda row: str(row.get('JinaC_SX', '')).strip(),
            axis=1
        )

        return pandas.DataFrame({self._column_name: result})
