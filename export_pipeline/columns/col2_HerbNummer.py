from .base import BaseStep
import pandas
class Column2_HerbNummer(BaseStep):

    _column_name="HerbNummer"

    def compute(self) -> pandas.DataFrame:
        result = self._sbirky.apply(
            lambda row: f"{row.get('PorC_S', '')}{'/' + row.get('Lomeni_S', '') if row.get('Lomeni_S', '') != '_' else ''}".strip(),
            axis=1
        )

        return pandas.DataFrame({self._column_name: result})
