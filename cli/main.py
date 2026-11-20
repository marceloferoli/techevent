from database import criar_tabelas, salvar_usuario, salvar_evento, salvar_inscricao
from usuario import Usuario
from evento import Evento
from inscricao import Inscricao

# Suas listas (gavetas vazias) entram aqui:
lista_usuarios = []
lista_eventos = []
lista_inscricoes = []

criar_tabelas()  # Certifique-se de que as tabelas existam antes de iniciar o menu

while True:
    print("\n--- MENU TECHEVENT ---")
    print("1. Cadastrar Usuário")
    print("2. Cadastrar Evento")
    print("3. Realizar Inscrição")
    print("4. Mostrar Relatórios")
    print("0. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "0":
        print("Saindo do sistema... Até logo!")
        break # Esse comando quebra o loop e fecha o programa   

    elif opcao == "1":
        nome = input("Digite o nome: ")
        idade = input("Digite a idade: ")
        email = input("Digite o email: ")
        cpf = input("Digite o CPF: ")

        novo_id = len(lista_usuarios) + 1  # Gerando um ID simples 
        novo_usuario = Usuario(novo_id, nome, idade, email, cpf)
        lista_usuarios.append(novo_usuario)
        salvar_usuario(novo_usuario)  # Salva no banco de dados


    elif opcao == "2":
        nome_evento = input("Digite o nome do evento: ")
        data_evento = input("Digite a data do evento (dd/mm/aaaa): ")
        horario_evento = input("Digite o horário do evento (hh:mm): ")
        local_evento = input("Digite o local do evento: ")

        novo_id_evento = len(lista_eventos) + 1  # Gerando um ID simples 
        novo_evento = Evento(novo_id_evento, nome_evento, data_evento, horario_evento, local_evento)
        lista_eventos.append(novo_evento)
        salvar_evento(novo_evento)  # Salva no banco de dados


    elif opcao == "3":
        input_id_usuario = int(input("Digite o ID do usuário: "))
        input_id_evento = int(input("Digite o ID do evento: "))

        novo_id_inscricao = len(lista_inscricoes) + 1  # Gerando um ID simples

        # Verificando se o usuário e o evento existem

        usuario_encontrado = None
        evento_encontrado = None

        for usuario in lista_usuarios:
            if usuario.id == input_id_usuario:
                usuario_encontrado = usuario
                break

        for evento in lista_eventos:
            if evento.id == input_id_evento:
                evento_encontrado = evento
                break

        if usuario_encontrado and evento_encontrado:
            nova_inscricao = Inscricao(novo_id_inscricao, usuario_encontrado, evento_encontrado)
            lista_inscricoes.append(nova_inscricao)
            salvar_inscricao(nova_inscricao)  # Salva no banco de dados
            print("Inscrição realizada com sucesso!")
        else:
            print("Usuário ou evento não encontrado.")

    elif opcao == "4":

        if len(lista_inscricoes) == 0:
            print("Nenhuma inscrição realizada ainda.")
        else:
            print("\n--- RELATÓRIO DE INSCRIÇÕES ---")
            for inscricao in sorted(lista_inscricoes, key=lambda x: x.id_inscricao):
                print(f"ID Inscrição: {inscricao.id_inscricao}, Usuário: {inscricao.id_usuario.nome}, Evento: {inscricao.id_evento.nome_evento}")


    











