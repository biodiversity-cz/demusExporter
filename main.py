from excel_writer import write_to_excel
from export_pipeline.columns.col10_Nummer import Column10_Nummer
from export_pipeline.columns.col2_HerbNummer import Column2_HerbNummer
from export_pipeline.columns.col3_collectionID import Column3_CollectionID
from export_pipeline.columns.col4_Collection import Column4_Collection
from export_pipeline.columns.col50_helper import Column50_helper
from export_pipeline.columns.col5_status import Column5_status
from export_pipeline.columns.col6_taxon import Column6_taxon
from export_pipeline.columns.col7_Sammler import Column7_Sammler
from export_pipeline.columns.col8_series import Column8_series
from export_pipeline.columns.col9_series_number import Column9_series_number
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
        Column10_Nummer()
    ]

    pipeline = Pipeline(steps, MDB_PATH)
    output_data = pipeline.run()
    write_to_excel(output_data, OUTPUT_PATH)
    print("Conversion completed!")

if __name__ == "__main__":
    main()
