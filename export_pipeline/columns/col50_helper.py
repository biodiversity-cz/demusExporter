from .base import BaseStep
import pandas
import re

class Column50_helper(BaseStep):

    _column_name="helper"

    def compute(self) -> pandas.DataFrame:
        result = self._sbirky.apply(
            lambda row: self._process_sberatel(row.get('Sberatel_SX', '')),
            axis=1
        )

        return pandas.DataFrame({self._column_name: result})

    def _process_sberatel(self, sberatel_str: str) -> str:
        return sberatel_str