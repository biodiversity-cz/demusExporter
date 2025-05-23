from typing import List
import pandas as pd

from mdb_reader import read_table

class Pipeline:
    TBL_SBIRKY = "Sbirky"
    TBL_LOKALITY = "Lokality"
    TBL_ADRESAR = "Adresar"
    TBL_URCENI = "Urceni"

    def __init__(self, steps: List, path: str):
        self.steps = steps
        self._tbl_Sbirky = read_table(path, self.TBL_SBIRKY)
        self._tbl_Lokality = read_table(path, self.TBL_LOKALITY)
        self._tbl_Adresar = read_table(path, self.TBL_ADRESAR)
        self._tbl_Urceni = read_table(path, self.TBL_URCENI)

        self._tbl_Sbirky = self._tbl_Sbirky.sort_values(by='PorC_S').reset_index(drop=True)
        self._tbl_Sbirky['Grid_S'] = self._tbl_Sbirky['Grid_S'].fillna('')
        self._tbl_Adresar['Jmeno_A'] = self._tbl_Adresar['Jmeno_A'].fillna('')

    def run(self) -> pd.DataFrame:
        all_dataframes = []
        for step in self.steps:
            df = step.proceed(self._tbl_Sbirky, self._tbl_Lokality, self._tbl_Adresar, self._tbl_Urceni)
            all_dataframes.append(df)

        final_df = pd.concat(all_dataframes, axis=1)

        return final_df
