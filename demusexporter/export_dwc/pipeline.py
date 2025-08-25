import pandas as pd

from demusexporter.export_dwc.columns.col10_verbatimElevation import VerbatimElevation
from demusexporter.export_dwc.columns.col11_occurrenceRemarks import OccurrenceRemarks
from demusexporter.export_dwc.columns.col12_verbatimIdentification import VerbatimIdentification
from demusexporter.export_dwc.columns.col13_basisOfRecord import BasisOfRecord
from demusexporter.export_dwc.columns.col1_occurrenceID import OccurenceId
from demusexporter.export_dwc.columns.col2_scientificName import ScientificName
from demusexporter.export_dwc.columns.col3_recordedBy import RecordedBy
from demusexporter.export_dwc.columns.col4_eventDate import EventDate
from demusexporter.export_dwc.columns.col5_identifiedBy import IdentifiedBy
from demusexporter.export_dwc.columns.col6_dateIdentified import DateIdentified
from demusexporter.export_dwc.columns.col7_locality import Locality
from demusexporter.export_dwc.columns.col8_decimalLatitude import DecimalLatitude
from demusexporter.export_dwc.columns.col9_decimalLongitude import DecimalLongitude

from demusexporter.workers.mdb_reader import read_table


class Pipeline:
    TBL_SBIRKY = "Sbirky"
    TBL_LOKALITY = "Lokality"
    TBL_ADRESAR = "Adresar"
    TBL_URCENI = "Urceni"
    _steps = [OccurenceId(),
              ScientificName(),
              RecordedBy(),
              EventDate(),
              IdentifiedBy(),
              DateIdentified(),
              Locality(),
              DecimalLatitude(),
              DecimalLongitude(),
              VerbatimElevation(),
              OccurrenceRemarks(),
              VerbatimIdentification(),
              BasisOfRecord()
              ]

    def __init__(self, path: str):
        self._tbl_Sbirky = read_table(path, self.TBL_SBIRKY)
        self._tbl_Lokality = read_table(path, self.TBL_LOKALITY)
        self._tbl_Adresar = read_table(path, self.TBL_ADRESAR)
        self._tbl_Urceni = read_table(path, self.TBL_URCENI)

        self._tbl_Sbirky = self._tbl_Sbirky.sort_values(by='PorC_S').reset_index(drop=True)
        self._tbl_Sbirky['Var_S'] = self._tbl_Sbirky['Var_S'].fillna('')
        self._tbl_Sbirky['Grid_S'] = self._tbl_Sbirky['Grid_S'].fillna('')
        self._tbl_Adresar['Jmeno_A'] = self._tbl_Adresar['Jmeno_A'].fillna('')

    def run(self) -> pd.DataFrame:
        all_dataframes = []
        for step in self._steps:
            df = step.proceed(self._tbl_Sbirky, self._tbl_Lokality, self._tbl_Adresar, self._tbl_Urceni)
            all_dataframes.append(df)

        final_df = pd.concat(all_dataframes, axis=1)

        return final_df
