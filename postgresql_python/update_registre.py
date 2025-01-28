import connect

def update_reg():
    conn = connect.connection_db()
    cursor = conn.cursor()

    sql_update = """
        UPDATE clientes
        SET fecha_cumpleaños = '1990-01-01'
        WHERE nombre_cliente = 'Mireia'
    """
    cursor.execute(sql_update)
    conn.commit()

    cursor.close()
    conn.close()

    return {"Update Successfully"}