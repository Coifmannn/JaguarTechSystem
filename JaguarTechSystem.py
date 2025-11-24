import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="856084",
    database="JaguarTech"
)
#Parte dos clientes (cad, att, del e consult) tbl_clientes
def cadastro_cliente():
    nome = input("Nome do cliente: ")
    numero = input("Telefone do cliente: ")
    logradouro = input("Logradouro do cliente: ")
    numero_casa = input("Número da casa: ")
    bairro = input("Bairro: ")
    cep = input("CEP (00000-000): ")
    cursor = conexao.cursor()
    sql = "INSERT INTO tbl_clientes (nome_cliente, numero_cliente, logradouro_cliente, numero_casa, bairro, CEP) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, (nome, numero, logradouro, numero_casa, bairro, cep))
    conexao.commit()
    cursor.close()
    print("Cliente cadastrado com sucesso!")

def atualizar_dados_cliente():
    id_cliente = input("ID do cliente a atualizar: ")
    nome = input("Novo nome: ")
    numero = input("Novo Telefone: ")
    logradouro = input("Novo logradouro: ")
    numero_casa = input("Novo número da casa: ")
    bairro = input("Novo bairro: ")
    cep = input("Novo CEP (00000-000): ")
    cursor = conexao.cursor()
    sql = "UPDATE tbl_clientes SET nome_cliente = %s, numero_cliente = %s, logradouro_cliente = %s, numero_casa = %s, bairro = %s, CEP = %s WHERE id_cliente = %s"
    cursor.execute(sql, (nome, numero, logradouro, numero_casa, bairro, cep, id_cliente))
    conexao.commit()
    cursor.close()
    print("Cliente atualizado!")

def excluir_cliente():
    id_cliente = input("ID do cliente a excluir: ")
    cursor = conexao.cursor()
    sql = "DELETE FROM tbl_clientes WHERE id_cliente = %s"
    cursor.execute(sql, (id_cliente,))
    conexao.commit()
    cursor.close()
    print("Cliente excluído!")

def consultar_cliente_por_ID():
    id_cliente = input("ID do cliente a consultar: ")
    cursor = conexao.cursor()
    sql = "SELECT * FROM tbl_clientes WHERE id_cliente = %s"
    cursor.execute(sql, (id_cliente,))
    resultado = cursor.fetchone()
    if resultado:
        print ("-" * 30)
        print("\n====== Dados do Cliente ======")
        print(f"ID: {resultado[0]}")
        print(f"Nome: {resultado[1]}")
        print(f"Telefone: {resultado[2]}")
        print(f"Logradouro: {resultado[3]}")
        print(f"Número da Casa: {resultado[4]}")
        print(F"Bairro: {resultado[5]}")
        print(F"CEP: {resultado[6]}")
        print("-" * 30)
    else:
        print("Cliente não encontrado.")
    cursor.close()

def consultar_todos_clientes():
    cursor = conexao.cursor()
    sql = "SELECT * FROM tbl_clientes"
    cursor.execute(sql)
    resultados = cursor.fetchall()
    for resultado in resultados:
        print("-" * 30)
        print("\n====== Dados do Cliente ======")
        print(f"ID: {resultado[0]}")
        print(f"Nome: {resultado[1]}")
        print(f"Telefone: {resultado[2]}")
        print(f"Logradouro: {resultado[3]}")
        print(f"Número da Casa: {resultado[4]}")
        print(f"Bairro: {resultado[5]}")
        print(f"CEP: {resultado[6]}")
        print("-" * 30)
        
        cursor.close()

#Parte dos aparelhos(cad, att, del e consult) tbl_aparelhos

def cadastro_aparelhos():
    marca = input("Marca do aparelho: ")
    modelo = input("Modelo do aparelho: ")
    id_cliente = input("ID do cliente dono do aparelho: ")
    cursor = conexao.cursor()
    sql = "INSERT INTO tbl_aparelhos (marca_aparelho, modelo_aparelho, id_cliente) VALUES (%s, %s, %s)"
    cursor.execute(sql, (marca, modelo, id_cliente))
    conexao.commit()
    cursor.close()
    print("Aparelho cadastrado!")

def atualizar_dados_aparelho():
    id_aparelho = input("ID do aparelho a atualizar: ")
    marca = input("Nova marca: ")
    modelo = input("Novo modelo: ")
    cursor = conexao.cursor()
    sql = "UPDATE tbl_aparelhos SET marca_aparelho = %s, modelo_aparelho = %s WHERE id_aparelho = %s"
    cursor.execute(sql, (marca, modelo, id_aparelho))
    conexao.commit()
    cursor.close()
    print("Aparelho atualizado!")

def excluir_aparelho():
    id_aparelho = input("ID do aparelho a excluir: ")
    cursor = conexao.cursor()
    sql = "DELETE FROM tbl_aparelhos WHERE id_aparelho = %s"
    cursor.execute(sql, (id_aparelho,))
    conexao.commit()
    cursor.close()
    print("Aparelho excluído!")

def consultar_aparelho_por_ID():
    id_aparelho = input("ID do aparelho a consultar:")
    cursor = conexao.cursor()
    sql = "SELECT * FROM tbl_aparelhos WHERE id_aparelho = %s"
    cursor.execute(sql, (id_aparelho,))
    resultado = cursor.fetchone()
    if resultado:
        print("-" * 30)
        print("\n====== Dados do Aparelho ======")
        print(f"ID: {resultado[0]}")
        print(f"Marca: {resultado[1]}")
        print(f"Modelo: {resultado[2]}")
        print(f"ID do cliente: {resultado[3]}")
        print("-" * 30)
    else:
        print("Aparelho não encontrado!")

    cursor.close()
    
def consultar_todos_aparelhos():
    cursor = conexao.cursor()
    sql = "SELECT * FROM tbl_aparelhos"
    cursor.execute(sql)
    resultados = cursor.fetchall()
    for resultado in resultados:
        print("-" * 30)
        print("\n====== Dados do Aparelho ======")
        print(f"ID: {resultado[0]}")
        print(f"Marca: {resultado[1]}")
        print(f"Modelo: {resultado[2]}")
        print(f"ID do cliente: {resultado[3]}")
        print("-" * 30)

#Parte dos serviços (cad, del e consult) tbl_servicos

def cadastro_servico():
    tipo = input("Tipo de serviço: ")
    valor = input("Valor do serviço: ")
    descricao = input("Descrição do problema: ")
    status_options = {"1": "Concluido", "2": "Em andamento", "3": "Pendente"}
    while True:
        print("Status do serviço:")
        print("1. Concluido")
        print("2. Em andamento")
        print("3. Pendente")
        escolha = input("Escolha uma opção (1-3): ").strip()
        if escolha in status_options:
            status = status_options[escolha]
            break
        else:
            print("Opção inválida. Tente novamente.")
    tempo_garantia = input("Tempo de garantia (AAAA-MM-DD): ")
    dt_entrada = input("Data de entrada (AAAA-MM-DD): ")
    previsao_entrega = input("Data de entrega (AAAA-MM-DD): ")
    id_aparelho = input("ID do aparelho: ")
    id_cliente = input("ID do cliente: ")
    cursor = conexao.cursor()
    sql = ("INSERT INTO tbl_servicos (tipo_servico, valor_servico, descricao_problema, status_servico, "
            "tempo_garantia, dt_entrada, previsao_entrega, id_aparelho, id_cliente) "
           "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
    cursor.execute(sql, (tipo, valor, descricao, status, tempo_garantia, dt_entrada, previsao_entrega, id_aparelho, id_cliente))
    conexao.commit()
    cursor.close()
    print("Serviço cadastrado!")

def atualizar_status_servico():
    id_servico = input("ID do serviço a atualizar: ")
    status_options = {"1": "Concluido", "2": "Em andamento", "3": "Pendente"}
    while True:
        print("Novo status do serviço:")
        print("1. Concluido")
        print("2. Em andamento")
        print("3. Pendente")
        escolha = input("Escolha uma opção (1-3): ").strip()
        if escolha in status_options:
            novo_status = status_options[escolha]
            break
        else:
            print("Opção inválida. Tente novamente.")
    cursor = conexao.cursor()
    sql = "UPDATE tbl_servicos SET status_servico = %s WHERE id_servico = %s"
    cursor.execute(sql, (novo_status, id_servico))
    conexao.commit()
    cursor.close()
    print("Status do serviço atualizado!")

def excluir_servico():
    id_servico = input("ID do serviço a excluir: ")
    cursor = conexao.cursor()
    sql = """DELETE FROM tbl_servicos WHERE id_servico = %s"""
    cursor.execute(sql, (id_servico,))
    conexao.commit()
    cursor.close()
    print("Serviço Excluido!")

def consultar_servico_por_ID():
    id_servico = input("ID do servico a consultar: ")
    cursor = conexao.cursor()
    sql = "SELECT tbl_clientes.nome_cliente, tbl_servicos.tipo_servico, tbl_servicos.valor_servico, tbl_servicos.descricao_problema, tbl_servicos.status_servico, tbl_servicos.tempo_garantia, tbl_servicos.dt_entrada, tbl_servicos.previsao_entrega, tbl_aparelhos.marca_aparelho, tbl_aparelhos.modelo_aparelho FROM tbl_servicos INNER JOIN tbl_clientes ON tbl_clientes.id_cliente = tbl_servicos.id_cliente INNER JOIN tbl_aparelhos ON tbl_aparelhos.id_aparelho = tbl_servicos.id_aparelho WHERE id_servico = %s"
    cursor.execute(sql, (id_servico,))
    resultado = cursor.fetchone()
    if resultado:
        print("-" * 30)
        print("\n====== Dados do Serviço ======")
        print(f"Nome do cliente: {resultado[0]}")
        print(f"Tipo de serviço: {resultado[1]}")
        print(f"Valor do serviço: {resultado[2]}")
        print(f"Descrição do problema: {resultado[3]}")
        print(f"Status do serviço: {resultado[4]}")
        print(f"Tempo de garantia (AAAA-MM-DD): {resultado[5]}")
        print(f"Data de entrada (AAAA-MM-DD): {resultado[6]}")
        print(f"Data de entrega (AAAA-MM-DD): {resultado[7]}")
        print(f"Marca do aparelho: {resultado[8]}")
        print(f"Modelo do aparelho: {resultado[9]}")
        print("-" * 30)        
    else:
        print("Serviço não encontrado.")
    cursor.close()
    
def consultar_todos_servicos():
    cursor = conexao.cursor()
    sql = 'SELECT tbl_clientes.nome_cliente, tbl_servicos.tipo_servico, tbl_servicos.valor_servico, tbl_servicos.descricao_problema, tbl_servicos.status_servico, tbl_servicos.tempo_garantia, tbl_servicos.dt_entrada, tbl_servicos.previsao_entrega, tbl_aparelhos.marca_aparelho, tbl_aparelhos.modelo_aparelho FROM tbl_servicos LEFT JOIN tbl_clientes ON tbl_clientes.id_cliente = tbl_servicos.id_cliente LEFT JOIN tbl_aparelhos ON tbl_aparelhos.id_aparelho = tbl_servicos.id_aparelho;'
    cursor.execute(sql)
    resultados = cursor.fetchall()
    for resultado in resultados:
        print("-" * 30)
        print("\n====== Dados do Serviço ======")
        print(f"Nome do cliente: {resultado[0]}")
        print(f"Tipo de serviço: {resultado[1]}")
        print(f"Valor do serviço: {resultado[2]}")
        print(f"Descrição do problema: {resultado[3]}")
        print(f"Status do serviço: {resultado[4]}")
        print(f"Tempo de garantia (AAAA-MM-DD): {resultado[5]}")
        print(f"Data de entrada (AAAA-MM-DD): {resultado[6]}")
        print(f"Data de entrega (AAAA-MM-DD): {resultado[7]}")
        print(f"Marca do aparelho: {resultado[8]}")
        print(f"Modelo do aparelho: {resultado[9]}")
        print("-" * 30)   
    cursor.close()

#Parte das peças (cad, att, del e consult) tbl_estoque

def cadastro_peca():
    nome = input("Nome da peça: ")
    descricao = input("Descrição da peça: ")
    quantidade = input("Quantidade em estoque: ")
    custo_unitario = input("Custo unitário: ")
    cursor = conexao.cursor()
    sql = "INSERT INTO tbl_estoque (nome_peca, descricao_peca, quantidade_estoque, custo_unitario) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (nome, descricao, quantidade, custo_unitario))
    conexao.commit()
    cursor.close()
    print("Peça cadastrada!")

def atualizar_peca():
    id_peca = input("ID da peça a atualizar: ")
    nome = input("Novo nome: ")
    descricao = input("Nova descrição: ")
    quantidade = input("Nova quantidade: ")
    custo_unitario = input("Novo custo unitário: ")
    cursor = conexao.cursor()
    sql = "UPDATE tbl_estoque SET nome_peca=%s, descricao_peca=%s, quantidade_estoque=%s, custo_unitario=%s WHERE id_peca=%s"
    cursor.execute(sql, (nome, descricao, quantidade, custo_unitario, id_peca))
    conexao.commit()
    cursor.close()
    print("Peça atualizada!")

def excluir_peca():
    id_peca = input("ID da peça a excluir: ")
    cursor = conexao.cursor()
    sql = "DELETE FROM tbl_estoque WHERE id_peca=%s"
    cursor.execute(sql, (id_peca,))
    conexao.commit()
    cursor.close()
    print("Peça excluída!")

def consultar_peca_por_ID():
    id_peca = input("ID da peça a consultar: ")
    cursor = conexao.cursor()
    sql = "SELECT * FROM tbl_estoque WHERE id_peca = %s"
    cursor.execute(sql, (id_peca,))
    resultado = cursor.fetchone()
    if resultado:
        print("-" * 30)
        print("\n====== Dados da Peça ======")
        print(f"ID da peça: {resultado[0]}")
        print(f"Nome da peça: {resultado[1]}")
        print(f"Descrição da peça: {resultado[2]}")
        print(f"Quantidade: {resultado[3]}")
        print(f"Custo unitário: {resultado[4]}")
        print("-" * 30)
    else:
        print("Peça não encontrada.")
    cursor.close()
    
def consultar_todas_pecas():
    cursor = conexao.cursor()
    sql = "SELECT * FROM tbl_estoque"
    cursor.execute(sql)
    resultados = cursor.fetchall()
    for resultado in resultados:
        print("-" * 30)
        print("\n====== Dados da Peça ======")
        print(f"ID da peça: {resultado[0]}")
        print(f"Nome da peça: {resultado[1]}")
        print(f"Descrição da peça: {resultado[2]}")
        print(f"Quantidade: {resultado[3]}")
        print(f"Custo unitário: {resultado[4]}")
        print("-" * 30)
    cursor.close()

def menu():
    while True:
        print("\n====== SISTEMA ORDEM DE SERVIÇO JAGUAR.TECH ======")
        print("1. Clientes")
        print("2. Aparelhos")
        print("3. Serviços")
        print("4. Peças / Estoque")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_clientes()
        elif opcao == "2":
            menu_aparelhos()
        elif opcao == "3":
            menu_servicos()
        elif opcao == "4":
            menu_pecas()
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

def menu_clientes():
    while True:
        print("\n====== CLIENTES ======")
        print("1. Cadastrar cliente")
        print("2. Atualizar cliente")
        print("3. Excluir cliente")
        print("4. Consultar cadastro de cliente por ID")
        print("5. Consultar todos os clientes")
        print("0. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastro_cliente()
        elif opcao == "2":
            atualizar_dados_cliente()
        elif opcao == "3":
            excluir_cliente()
        elif opcao == "4":
            consultar_cliente_por_ID()
        elif opcao == "5":
            consultar_todos_clientes()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

def menu_aparelhos():
    while True:
        print("\n====== APARELHOS ======")
        print("1. Cadastrar aparelho")
        print("2. Atualizar aparelho")
        print("3. Excluir aparelho")
        print("4. Consultar cadastro de aparelho por ID")
        print("5. Consultar todos os aparelhos")
        print("0. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastro_aparelhos()
        elif opcao == "2":
            atualizar_dados_aparelho()
        elif opcao == "3":
            excluir_aparelho()
        elif opcao == "4":
            consultar_aparelho_por_ID()
        elif opcao == "5":
            consultar_todos_aparelhos()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

def menu_servicos():
    while True:
        print("\n====== SERVIÇOS ======")
        print("1. Cadastrar serviço")
        print("2. Atualizar status do serviço")
        print("3. Excluir serviço")
        print("4. Consultar serviço por ID")
        print("5. Consultar todos os serviços")
        print("0. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastro_servico()
        elif opcao == "2":
            atualizar_status_servico()
        elif opcao == "3":
            excluir_servico()
        elif opcao == "4":
            consultar_servico_por_ID()
        elif opcao == "5":
            consultar_todos_servicos()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

def menu_pecas():
    while True:
        print("\n====== PEÇAS / ESTOQUE ======")
        print("1. Cadastrar peça")
        print("2. Atualizar peça")
        print("3. Excluir peça")
        print("4. Consultar cadastro de peça por ID")
        print("5. Consultar todas as peças")
        print("0. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastro_peca()
        elif opcao == "2":
            atualizar_peca()
        elif opcao == "3":
            excluir_peca()
        elif opcao == "4":
            consultar_peca_por_ID()
        elif opcao == "5":
            consultar_todas_pecas()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

menu()
conexao.close()
print("Conexão com o banco encerrada!.")