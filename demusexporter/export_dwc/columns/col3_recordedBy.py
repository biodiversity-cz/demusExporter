from .base import BaseStep
import pandas


class RecordedBy(BaseStep):
    _column_name = "recordedBy"

    def compute(self) -> pandas.DataFrame:
        result = self._sbirky.apply(
            lambda row: self._build_adresar(row.get('Sberatel_S', '')),
            axis=1
        )

        return pandas.DataFrame({self._column_name: result})