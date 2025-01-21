import dict_to_db as d_t_db
import pandas as pd
import os

def csv_to_dict():
  file_path = os.path.join(os.getcwd(), "send_data_to_db", "Clientes.csv")
  df = pd.read_csv(file_path)
  d = df.to_dict(orient='list')
  return d

data = csv_to_dict()

for i in range(30):
  print(d_t_db.send_data_to_db(i, data))