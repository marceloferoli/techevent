import mysql.connector

def conectar():
    # Faz a ponte com o MySQL do XAMPP
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="techevent"
    )

def criar_tabelas():
    conexao = conectar()
    cursor = conexao.cursor()

    # 1. Tabela de Usuários (Pronta como exemplo de sintaxe MySQL)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            idade INT NOT NULL,
            email VARCHAR(100) NOT NULL,
            cpf VARCHAR(20) NOT NULL
        )
    """)

    # 2. Sua vez! Crie a tabela 'eventos' usando cursor.execute(""" ... """)
    # Campos necessários: id (INT AUTO_INCREMENT PRIMARY KEY), nome_evento (VARCHAR(100)), data (VARCHAR(20)), hora (VARCHAR(10)), local (VARCHAR(100))
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS eventos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome_evento VARCHAR(100) NOT NULL,
            data VARCHAR(20) NOT NULL,
            hora VARCHAR(10) NOT NULL,
            local VARCHAR(100) NOT NULL
        )
    """)


    # 3. Sua vez! Crie a tabela 'inscricoes' usando cursor.execute(""" ... """)
    # Campos necessários: id (INT AUTO_INCREMENT PRIMARY KEY), id_usuario (INT), id_evento (INT)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS inscricoes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            id_usuario INT NOT NULL,
            id_evento INT NOT NULL        )
    """)

    conexao.commit()
    cursor.close()
    conexao.close()
    print("Tabelas verificadas/criadas com sucesso!")

def salvar_usuario(usuario):
    conexao = conectar()
    cursor = conexao.cursor()
    
    # O %s funciona como um espaço reservado seguro contra invasões (SQL Injection)
    sql = "INSERT INTO usuarios (nome, idade, email, cpf) VALUES (%s, %s, %s, %s)"
    valores = (usuario.nome, usuario.idade, usuario.email, usuario.cpf)
    
    cursor.execute(sql, valores)
    conexao.commit()
    
    cursor.close()
    conexao.close()

def salvar_evento(evento):
    conexao = conectar()
    cursor = conexao.cursor()
    
    sql = "INSERT INTO eventos (nome_evento, data, hora, local) VALUES (%s, %s, %s, %s)"
    valores = (evento.nome_evento, evento.data, evento.hora, evento.local)
    
    cursor.execute(sql, valores)
    conexao.commit()
    
    cursor.close()
    conexao.close()

def salvar_inscricao(inscricao):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "INSERT INTO inscricoes (id_usuario, id_evento) VALUES (%s, %s)"
    valores = (inscricao.id_usuario.id, inscricao.id_evento.id)

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()

# Permite testar esse arquivo rodando ele diretamente
if __name__ == "__main__":
    criar_tabelas()
