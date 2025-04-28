from .base import BaseStep
import pandas
class Column20_Provinz(BaseStep):

    _column_name="provinz"

    def compute(self) -> pandas.DataFrame:
        result = self._sbirky.apply(
            lambda row: f"".strip(),
            axis=1
        )

        return pandas.DataFrame({self._column_name: result})
