from typing import List
import pandas as pd

from mdb_reader import read_table

class Pipeline:
    TBL_SBIRKY = "SbirkyX"

    def __init__(self, steps: List, path: str):
        self.steps = steps
        self._tbl_Sbirky = read_table(path, self.TBL_SBIRKY)

    def run(self) -> pd.DataFrame:
        all_dataframes = []
        for step in self.steps:
            df = step.proceed(self._tbl_Sbirky)
            all_dataframes.append(df)

        final_df = pd.concat(all_dataframes, axis=1)

        return final_df
