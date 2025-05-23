from .base import BaseStep
import pandas
class Column14_det(BaseStep):

    _column_name="det"

    def compute(self) -> pandas.DataFrame:
        self._sbirky['Urcil_SX'] = self._sbirky['Urcil_SX'].fillna('')

        result = self._sbirky.apply(
            lambda row: self._process_det(row.get('Urcil_SX', '')),
            axis=1
        )

        return pandas.DataFrame({self._column_name: result})

    def _process_det(self, det_str: str) -> str:
        if not pandas.notna(det_str) or det_str == '':
            return ''
        det_str = det_str.replace(' et all.', ' €')
        det_str = det_str.replace(' et ', ' & ')
        return det_str.replace(' €', ' & et all.')