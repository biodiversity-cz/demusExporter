from .base import BaseStep
import pandas
class Column24_Bemerkungen(BaseStep):

    _column_name="Bemerkungen"

    def compute(self) -> pandas.DataFrame:
        self._sbirky['Pozn_SX'] = self._sbirky['Pozn_SX'].fillna('')
        result = self._sbirky.apply(
            lambda row: f"{row.get('Pozn_SX', '')}".strip(),
            axis=1
        )

        return pandas.DataFrame({self._column_name: result})
