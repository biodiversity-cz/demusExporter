from demusexporter.exportTypes import ExportTypes
from demusexporter.process_file import process_uploaded_file

input_path = "test/Bezny.mdb"
# output_path = "test/output.xlsx"
output_path = "test/output.zip"

process_uploaded_file(input_path, output_path, ExportTypes.DWC.value)
