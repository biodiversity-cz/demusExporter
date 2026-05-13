from demusexporter.exportTypes import ExportTypes
from demusexporter.workers.excel_writer import write_to_excel
from demusexporter.export_jacq.pipeline import Pipeline as Jacq
from demusexporter.export_pladias.pipeline import Pipeline as Pladias

def process_uploaded_file(input_path, output_path, type_str: str):
    pipeline_map = {
        ExportTypes.JACQ.value: Jacq,
        ExportTypes.PLADIAS.value: Pladias
    }

    entry = pipeline_map.get(type_str)
    if not entry:
        raise ValueError(f"Neznámý exportní typ: {type_str}")

    pipeline_class = entry
    pipeline = pipeline_class(input_path)
    output_data = pipeline.run()

    write_to_excel(output_data, output_path)