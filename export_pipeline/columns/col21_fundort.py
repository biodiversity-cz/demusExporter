from .base import BaseStep
import pandas
class Column21_Fundort(BaseStep):

    _column_name="Fundort"

    def compute(self) -> pandas.DataFrame:
        result = self._sbirky.apply(
            lambda row: f"{row.get('XOrigLok_SX', '')} {row.get('Herbar_SX', '')}".strip(),
            axis=1
        )

        return pandas.DataFrame({self._column_name: result})
