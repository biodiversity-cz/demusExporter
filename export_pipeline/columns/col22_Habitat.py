from .base import BaseStep
import pandas
class Column22_Habitat(BaseStep):

    _column_name="Habitat"

    def compute(self) -> pandas.DataFrame:
        self._sbirky['EkoChar_SX'] = self._sbirky['EkoChar_SX'].fillna('')
        result = self._sbirky.apply(
            lambda row: f"{row.get('EkoChar_SX', '')}".strip(),
            axis=1
        )

        return pandas.DataFrame({self._column_name: result})
