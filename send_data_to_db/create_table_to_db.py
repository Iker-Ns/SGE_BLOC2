import psycopg2

def create_tables():
   conn = psycopg2.connect(
      dbname="the_bear",
      user="2223_iker.rivera@iticbcn.com",
      password="system",
      host="localhost",
      port=5432
   )
   cursor = conn.cursor()  
   sql_clients = '''
      CREATE TABLE Clientes (
      Nombre_Cliente VARCHAR(100),
      Dirección_Cliente VARCHAR(200),
      Teléfono_Cliente VARCHAR(100),
      Correo_Electrónico_Cliente VARCHAR(100),
      Fecha_Cumpleaños VARCHAR(50));'''

   cursor.execute(sql_clients)

   conn.commit()

   conn.close()
   cursor.close()

   return {"Tables created succesfully"}

print(create_tables())