from .base import BaseStep
import pandas


class Column17_taxon_alt(BaseStep):
    _column_name = "taxon_alt"

    def compute(self) -> pandas.DataFrame:
        result = self._sbirky.apply(
            lambda row: 'problém!',
            axis=1
        )
        return pandas.DataFrame({self._column_name: result})
