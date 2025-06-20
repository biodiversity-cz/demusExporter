from demusExporter.exportTypes import ExportTypes
from demusExporter.workers.excel_writer import write_to_excel
from demusExporter.export_jacq.pipeline import Pipeline as Jacq
from demusExporter.export_pladias.pipeline import Pipeline as Pladias

def process_uploaded_file(input_path, output_path, type):
    if type == ExportTypes.JACQ:
        pipeline = Jacq(input_path)
    else:
        pipeline = Pladias(input_path)

    output_data = pipeline.run()
    write_to_excel(output_data, output_path)