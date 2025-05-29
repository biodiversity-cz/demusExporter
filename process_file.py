from workers.excel_writer import write_to_excel
from export_jacq.pipeline import Pipeline

def process_uploaded_file(input_path, output_path):
    pipeline = Pipeline(input_path)
    output_data = pipeline.run()
    write_to_excel(output_data, output_path)