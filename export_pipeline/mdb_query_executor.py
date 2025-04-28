from sqlalchemy import create_engine

def get_mdb_engine(mdb_path: str):
    connection_string = f"access+pyodbc:///?odbc_connect=DRIVER={{MDBTools}};DBQ={mdb_path};"
    engine = create_engine(connection_string)
    return engine
