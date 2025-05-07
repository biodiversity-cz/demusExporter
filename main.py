from excel_writer import write_to_excel
from export_pipeline.columns.col10_Nummer import Column10_Nummer
from export_pipeline.columns.col12_datum import Column12_datum

from export_pipeline.columns.col13_Datum2 import Column13_Datum2
from export_pipeline.columns.col14_det import Column14_det
from export_pipeline.columns.col15_typified import Column15_typified
from export_pipeline.columns.col16_typus import Column16_typus
from export_pipeline.columns.col17_taxon_alt import Column17_taxon_alt
from export_pipeline.columns.col18_nation_engl import Column18_nation_engl
from export_pipeline.columns.col19_provinz import Column19_provinz
from export_pipeline.columns.col20_fundort import Column20_Fundort
from export_pipeline.columns.col21_Fundort_engl import Column21_Fundort_engl
from export_pipeline.columns.col22_Habitat import Column22_Habitat
from export_pipeline.columns.col23_Habitus import Column23_Habitus
from export_pipeline.columns.col24_Bemerkungen import Column24_Bemerkungen
from export_pipeline.columns.col2_HerbNummer import Column2_HerbNummer
from export_pipeline.columns.col3_collectionID import Column3_CollectionID
from export_pipeline.columns.col4_Collection import Column4_Collection
from export_pipeline.columns.col50_helper import Column50_helper
from export_pipeline.columns.col5_status import Column5_status
from export_pipeline.columns.col6_taxon import Column6_taxon
from export_pipeline.columns.col7_Sammler import Column7_Sammler
from export_pipeline.columns.col8_series import Column8_series
from export_pipeline.columns.col9_series_number import Column9_series_number
from export_pipeline.columns.col11_alt_number import Column11_alt_number
from export_pipeline.pipeline import Pipeline
from export_pipeline.columns.col1_id import Column1_ID

OUTPUT_PATH = "output/1.xlsx"
MDB_PATH = "data/example.mdb"

def main():
    steps = [
        Column1_ID(),
        Column2_HerbNummer(),
        Column3_CollectionID(),
        Column4_Collection(),
        Column5_status(),
        Column6_taxon(),
        Column7_Sammler(),
        Column50_helper(),
        Column8_series(),
        Column9_series_number(),
        Column10_Nummer(),
        Column11_alt_number(),
        Column12_datum(),
        Column13_Datum2(),
        Column14_det(),
        Column15_typified(),
        Column16_typus(),
        Column17_taxon_alt(),
        Column18_nation_engl(),
        Column19_provinz(),
        Column20_Fundort(),
        Column21_Fundort_engl(),
        Column22_Habitat(),
        Column23_Habitus(),
        Column24_Bemerkungen()
    ]

    pipeline = Pipeline(steps, MDB_PATH)
    output_data = pipeline.run()
    write_to_excel(output_data, OUTPUT_PATH)
    print("Conversion completed!")

if __name__ == "__main__":
    main()
