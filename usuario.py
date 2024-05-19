import bd
from psycopg2 import Error

def criar_usuario(usuario):
    connection = bd.conectar()
    try:
        cursor = connection.cursor()
        postgres_insert_query = """ INSERT INTO usuarios (nome, senha) VALUES (%s, %s) RETURNING id"""
        record_to_insert = (usuario['nome'], usuario['senha'])
        cursor.execute(postgres_insert_query, record_to_insert)
        usuario_id = cursor.fetchone()[0]
        connection.commit()
        print("Usuário criado com sucesso! ID:", usuario_id)
        return usuario_id
    except (Exception, Error) as error:
        print("Erro ao inserir usuário:", error)
    finally:
        if connection:
            connection.close()

def listar_usuarios():
    connection = bd.conectar()
    try:
        cursor = connection.cursor()
        postgres_select_query = """ SELECT * FROM usuarios """
        cursor.execute(postgres_select_query)
        usuarios = cursor.fetchall()
        lista_usuarios = []
        for usuario in usuarios:
            lista_usuarios.append({
                'id': usuario[0],
                'nome': usuario[1],
                'senha': usuario[2]
            })
        return lista_usuarios
    except (Exception, Error) as error:
        print("Erro ao listar usuários:", error)
    finally:
        if connection:
            connection.close()

def ler_usuario(id):
    connection = bd.conectar()
    try:
        cursor = connection.cursor()
        postgres_select_query = """ SELECT * FROM usuarios WHERE id = %s """
        cursor.execute(postgres_select_query, (id,))
        usuario = cursor.fetchone()
        if usuario:
            print("Usuário encontrado:")
            print(usuario)
            return {
                'id': usuario[0],
                'nome': usuario[1],
                'senha': usuario[2]
            }
        else:
            print("Usuário não encontrado.")
            return None
    except (Exception, Error) as error:
        print("Erro ao ler usuário:", error)
    finally:
        if connection:
            connection.close()

def atualizar_usuario(id, novo_nome, nova_senha):
    connection = bd.conectar()
    try:
        cursor = connection.cursor()
        postgres_update_query = """ UPDATE usuarios SET nome = %s, senha = %s WHERE id = %s"""
        cursor.execute(postgres_update_query, (novo_nome, nova_senha, id))
        connection.commit()
        print("Usuário atualizado com sucesso!")
    except (Exception, Error) as error:
        print("Erro ao atualizar usuário:", error)
    finally:
        if connection:
            connection.close()

def deletar_usuario(id):
    connection = bd.conectar()
    try:
        cursor = connection.cursor()
        postgres_delete_query = """ DELETE FROM usuarios WHERE id = %s"""
        cursor.execute(postgres_delete_query, (id,))
        connection.commit()
        print("Usuário deletado com sucesso!")
    except (Exception, Error) as error:
        print("Erro ao deletar usuário:", error)
    finally:
        if connection:
            connection.close()
