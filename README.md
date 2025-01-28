# Connection
![ConnectionToDb](imgs/connect_success.png)

La imagen muestra que se ha podido establecer correctamente la conexión a la base de datos y está imprimiendo el estado del conector y la información como el usuario, el nombre de la base de datos, el puerto y si la conexión está abierta (0) o cerrada (1).

# Inserción
![Insert](imgs/insert/insert_data.png)

La imagen muestra los datos que ha leído del [.CSV](send_data_to_db/Clientes.csv) previamente, y los ha insertado en la base de datos.

# Crear Registro
![Create](imgs/create/create_table_success.png)

La imagen muestra que [create_registre.py](postgresql_python/create_registre.py) se ha ejecutado correctamente, y si vamos al PgAdmin podremos ver cómo se han creado correctamente.

![PgAdmin](imgs/create/create_pgadmin.png)

# Leer Registro
![Read](imgs/read/read_registre.png)

La imagen muestra la información que hay en la tabla de Clientes.

# Actualizar Registro
![Actualizar](imgs/updates/update_registre.png)

![Before](imgs/updates/update_registre_before.png)
![After](imgs/updates/update_register_after.png)

Actualizamos el teléfono donde el nombre de cliente sea 'Roger'.

## Otros Updates
![Actualizar](imgs/updates/update_calle_juan_manuel.png)

En esta imagen estamos actualizando la calle de cualquier cliente que se llame 'Juan Manuel'.

![Actualizar](imgs/updates/update_fecha_mireia.png)

En esta imagen estamos actualizando la fecha de nacimiento de cualquier cliente que se llame 'Mireia'.

![Actualizar](imgs/updates/update_nombre_josepe.png)

En esta imagen estamos actualizando el nombre de cualquier cliente que se llame 'Josep Oriol'.

![Actualizar](imgs/updates/after_pgadmin.png)

Y estos son los resultados después de hacer una Query en el PgAdmin.

# Borrar Registro
![Borrar](imgs/delete/delete_registre.png)

En esta imagen estamos borrando todos los clientes donde su nombre sean 'Roger'.

Este es el antes:
![Before](imgs/delete/count_before_pgadmin.png)

Como podemos ver hay dos clientes con el nombre de 'Roger'

Y el despues:
![After](imgs/delete/count_after_pgadmin.png)