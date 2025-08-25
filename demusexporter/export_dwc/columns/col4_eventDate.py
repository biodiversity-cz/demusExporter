from .base import BaseStep
import pandas


class EventDate(BaseStep):
    _column_name = "eventDate"

    def compute(self) -> pandas.DataFrame:
        self._sbirky['DatSberu_S'] = self._sbirky['DatSberu_S'].fillna('s.d.')

        result = self._sbirky.apply(
            lambda row: str(row.get('DatSberu_S', '')).strip(),#pandas.to_datetime(series, errors="coerce").dt.strftime("%Y-%m-%d"),
            axis=1
        )

        return pandas.DataFrame({self._column_name: result})


