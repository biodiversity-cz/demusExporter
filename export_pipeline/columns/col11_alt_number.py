from .base import BaseStep
import pandas
class Column11_alt_number(BaseStep):

    _column_name="alt_number"

    def compute(self) -> pandas.DataFrame:
        self._sbirky['JinaC_S'] = self._sbirky['JinaC_S'].fillna('')

        result = self._sbirky.apply(
            lambda row: str(row.get('JinaC_S', '')).strip(),
            axis=1
        )

        return pandas.DataFrame({self._column_name: result})
