from .base import BaseStep
import pandas
class Column18_nation_engl(BaseStep):

    _column_name="nation_engl"

    def compute(self) -> pandas.DataFrame:
        self._sbirky['Stat_SX'] = self._sbirky['Stat_SX'].fillna('')

        result = self._sbirky.apply(
            lambda row: str(row.get('Stat_SX', '')).strip(),
            axis=1
        )

        return pandas.DataFrame({self._column_name: result})
