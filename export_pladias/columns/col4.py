from sqlalchemy.engine import row

from .base import BaseStep
import pandas


class Column4(BaseStep):
    _column_name = "nejbližší obec"

    def compute(self) -> pandas.DataFrame:
        result = self._sbirky.apply(
            lambda row: self._build_item(row),
            axis=1
        )

        return pandas.DataFrame({self._column_name: result})

    def _build_item(self, row) -> str:

        return f"tento a obdobné sloupce - u záznamů s přesnou souřadnicí můžeme provolávat api pro georeferencování, ale co u těch (mnoha) záznamů které mají #? v souřadnicícch?".strip()

