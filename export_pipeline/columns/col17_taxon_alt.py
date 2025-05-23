from .base import BaseStep
import pandas


class Column17_taxon_alt(BaseStep):
    _column_name = "taxon_alt"

    def compute(self) -> pandas.DataFrame:
        result = self._sbirky.apply(
            lambda row: self._build_revisions(row.get('IdC_S', '')),
            axis=1
        )

        return pandas.DataFrame({self._column_name: result})

    def _build_revisions(self, sbirky_id: int) -> str:
        zaznamy = self._urceni[self._urceni['IdC_UR'] == sbirky_id]
        if zaznamy.empty:
            return ''

        zaznamy = zaznamy.sort_values(by='DatUrc_UR')

        polozky = []
        polozky.append("orig.: ??")
        for _, row in zaznamy.iterrows():
            daturc = str(row.get('DatUrc_UR', '')).strip()
            rok = daturc[:4] if daturc else ''
            text = f"{self._build_adresar(str(row['Urcil_UR']).strip())}"
            if rok:
                text += f" ({rok})"
            text += f": {str(row['Nomen_UR']).strip()}"
            polozky.append(text)

        return "; ".join(polozky)