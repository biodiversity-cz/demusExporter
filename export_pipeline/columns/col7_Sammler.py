from .base import BaseStep
import pandas
import re

class Column7_Sammler(BaseStep):

    _column_name="Sammler"

    def compute(self) -> pandas.DataFrame:
        result = self._sbirky.apply(
            lambda row: self._process_sberatel(row.get('Sberatel_SX', '')),
            axis=1
        )

        return pandas.DataFrame({self._column_name: result})

    def _process_sberatel(self, sberatel_str: str) -> str:
        if not pandas.notna(sberatel_str) or sberatel_str == '':
            return ''

        sberatel_str = sberatel_str.replace(';', '')
        sberatel_str = sberatel_str.replace(' et all.', ' €')
        sberatel_str = sberatel_str.replace(' et ', ' & ')
        sberatel_str = sberatel_str.replace(' €', ' & et all.')

        sberatele = [s.strip() for s in re.split(r',\s*|\s+a\s+|\s+\+\s+|\s+&\s+', sberatel_str) if s.strip()]

        if len(sberatele) > 2:
            return ', '.join(sberatele[:-1]) + ' & ' + sberatele[-1]
        elif len(sberatele) == 2:
            return ' & '.join(sberatele)

        return sberatele[0]