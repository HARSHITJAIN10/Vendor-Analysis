import pandas as pd
import os 
from sqlalchemy import create_engine
import logging
import time

logging.basicConfig(
    filename="log/ingestion_db.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

engine = create_engine('sqlite:///inventory.db')
folder_path = r'C:\Users\user\Downloads\data\data' 

def ingest_db(df, table_name, engine):
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)

def load_raw_data():
    start = time.time()
    for file in os.listdir(folder_path):
        if file.endswith('.csv'):
            file_path = os.path.join(folder_path, file)
            df = pd.read_csv(file_path)
            logging.info(f'Ingesting {file} into DB')
            ingest_db(df, file[:-4], engine)
    end = time.time()
    total_time = (end - start) / 60
    logging.info(f'Total ingestion time: {total_time:.2f} minutes')

if __name__ == '__main__':
    load_raw_data()
