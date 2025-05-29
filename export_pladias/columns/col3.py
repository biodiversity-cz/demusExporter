from sqlalchemy.engine import row

from .base import BaseStep
import pandas


class Column3(BaseStep):
    _column_name = "lokalita"

    def compute(self) -> pandas.DataFrame:
        self._sbirky['OrigLok_S'] = self._sbirky['OrigLok_S'].fillna('')
        result = self._sbirky.apply(
            lambda row: self._build_item(row),
            axis=1
        )

        return pandas.DataFrame({self._column_name: result})

    def _build_item(self, row) -> str:
        lokalita = row.get('OrigLok_S', '')
        return f"{lokalita}".strip()

