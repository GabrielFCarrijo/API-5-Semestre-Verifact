import bd
from psycopg2 import Error

def mostrar_resultado():
    connection = None
    try:
        # Conecta ao banco de dados
        connection = bd.conectar()
        cursor = connection.cursor()
        
        # Executa a consulta para obter o resultado
        postgres_select_query = "SELECT * FROM resultados LIMIT 1"
        cursor.execute(postgres_select_query)
        resultado = cursor.fetchone()
        
        if resultado:
            # Formata o resultado
            mostrar_resultado = {
                'id': resultado[0],
                'resultado': resultado[1],
            }
            
            # Executa a consulta para deletar o resultado
            postgres_delete_query = "DELETE FROM resultados WHERE id = %s"
            cursor.execute(postgres_delete_query, (resultado[0],))
            
            # Confirma a transação
            connection.commit()
            
            return mostrar_resultado
        else:
            print("Nenhum resultado encontrado.")
            return None
        
    except Exception as error:
        print(f"Erro ao acessar o banco de dados: {error}")
        # Em caso de erro, reverte as alterações (rollback)
        if connection:
            connection.rollback()
    finally:
        if connection:
            # Fecha o cursor e a conexão
            cursor.close()
            connection.close()

def inserir_resultado(texto):
    connection = None
    try:
        # Conecta ao banco de dados
        connection = bd.conectar()
        cursor = connection.cursor()
        
        # Consulta de inserção
        postgres_insert_query = """INSERT INTO inseretexto (texto) VALUES (%s) RETURNING id"""
        record_to_insert = (texto['texto'],)  # Deve ser uma tupla
        
        cursor.execute(postgres_insert_query, record_to_insert)
        
        # Obtém o ID do novo registro
        texto_id = cursor.fetchone()[0]
        
        # Confirma a transação
        connection.commit()
        
        print("Texto inserido com sucesso:", texto_id)
        return texto_id
    except (Exception, Error) as error:
        print("Erro ao inserir texto:", error)
        if connection:
            connection.rollback()
    finally:
        if cursor:
            cursor.close()  # Fecha o cursor
        if connection:
            connection.close()  # 