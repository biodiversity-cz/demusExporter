from demusExporter.exportTypes import ExportTypes
from demusExporter.process_file import process_uploaded_file

input_path = "test/Bezny.mdb"
output_path = "test/output.xlsx"

process_uploaded_file(input_path, output_path, ExportTypes.JACQ)
