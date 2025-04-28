from .base import BaseStep
import pandas
class Column2_HerbNummer(BaseStep):

    _column_name="HerbNummer"

    def compute(self) -> pandas.DataFrame:
        result = self._sbirky.apply(
            lambda row: f"{row.get('PorC_SX', '')}{'/' + row.get('Lomeni_SX', '') if row.get('Lomeni_SX', '') != '_' else ''}".strip(),
            axis=1
        )

        return pandas.DataFrame({self._column_name: result})
