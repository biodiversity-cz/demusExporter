from .base import BaseStep
import pandas

class Column6_taxon(BaseStep):

    _column_name="taxon"

    def compute(self) -> pandas.DataFrame:
        result = self._sbirky.apply(
            lambda row: f"{row.get('Nomen_SX', '')} {row.get('Var_SX', '') if pandas.notna(row.get('Var_SX')) and row.get('Var_SX', '') != '' else ''}".strip(),
            axis=1
        )

        return pandas.DataFrame({self._column_name: result})
