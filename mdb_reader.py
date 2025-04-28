import pandas as pd
import io
import subprocess

def read_table(mdb_path: str, table_name: str) -> pd.DataFrame:
    """Reads a table from an MDB file using mdb-tools."""
    cmd = ["mdb-export", mdb_path, table_name]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, text=True, check=True)
    data = pd.read_csv(io.StringIO(result.stdout))
    return data
