import sqlite3
import os

conexao = sqlite3.connect("database_aa.db")
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS duplicatas (
    nome CHAR(40),
    numero INTEGER PRIMARY KEY NOT NULL,
    valor REAL(10, 2),
    vencimento DATE,
    banco CHAR(15)
    )
""")

# ---------------------------------
# FUNÇÕES RELACIONADAS AO MENU 

# MENU PRINCIPAL
def menu():
    print(50 * "-")
    print(f"{'MENU':^50}")
    print(50 * "-", "\n")

    print("OPÇÕES\n")
    print("1 - MOSTRAR TABELA")
    print("2 - INSERIR DADOS")
    print("3 - AÇÕES AA")
    print("0 - SAIR")
    resposta_menu = int(input("\n~> "))

    return resposta_menu

def sub_menu():
    while True:
        os.system("cls")
        print("1 - AÇÃO")
        print("2 - AÇÃO")
        print("3 - AÇÃO")
        print("4 - AÇÃO")
        print("5 - AÇÃO")
        print("6 - AÇÃO")
        print("7 - AÇÃO")
        print("8 - AÇÃO")
        print("0 - VOLTAR")

        try:
            resposta_menu = int(input("~> "))

            if resposta_menu == 0:
                break
            elif resposta_menu == 1:
                os.system("cls")
                acao_1()
                input("~> ")
            elif resposta_menu == 2:
                os.system("cls")
                acao_2()
                input("~> ")
            elif resposta_menu == 3:
                os.system("cls")
                acao_3()
                input("~> ")
            elif resposta_menu == 4:
                os.system("cls")
                acao_4()
                input("~> ")
            elif resposta_menu == 5:
                os.system("cls")
                acao_5()
                input("~> ")
            elif resposta_menu == 6:
                os.system("cls")
                acao_6()
                input("~> ")
            elif resposta_menu == 7:
                os.system("cls")
                acao_7()
                input("~> ")
            elif resposta_menu == 8:
                os.system("cls")
                acao_8()
                input("~> ")
            else:
                os.system("cls")
                input("Valor invalido!")  

        except ValueError:
            os.system("cls")
            input("Valor invalido!")  
# ---------------------------------
# FUNÇÕES RELACIONADAS AO DATA BASE

# FUNÇÃO PARA MOSTRAR A TABELA INTEIRA
def tabela_inteira():
    cursor.execute(
        "SELECT * FROM duplicatas"
    )

    saida = cursor.fetchall()

    print(f"{'NOME':>10}  {'NUMERO':>21}  {'VALOR':>16}  {'VENCIMENTO':>18}  {'BANCO':>17}")
    print(100 * "-", "\n")

    for nome, numero, valor, vencimento, banco in saida:
        print(f"{nome:<20} | {numero:^15} | {valor:^15.2f} | {vencimento:^15} | {banco:<15}")

# FUNÇÃO PARA INSERÇÃO DE DADOS
def inserir_dados():
    while True:
        os.system("cls")
        nome = input("Nome: ").strip()
        numero = int(input("Numero: ").strip())
        valor = float(input("Valor: ").replace(",", ".").strip())

        vencimento = input("Vencimento: ")
        dia, mes, ano = vencimento.split("/")
        vencimento = f"{ano}-{mes}-{dia}"

        banco = input("Banco: ").strip()

        cursor.execute(
            "INSERT INTO duplicatas (nome, numero, valor, vencimento, banco) VALUES (?, ?, ?, ?, ?)",
            (nome, numero, valor, vencimento, banco)
            )

        conexao.commit()

        os.system("cls")

        input("\nProduto cadastrado com sucesso!")

        os.system("cls")

        print("1 - INSERIR OUTRO")
        print("0 - VOLTAR")

        resposta = int(input("~> "))

        if resposta == 0:
            break

        elif resposta == 1:
            continue
        else:
            print("CARACTERE INVÁLIDO")
# ---------------------------------
# FUNÇÕES RELACIONADAS AS AÇÕES NO DATA BASE DA AA

# 1º
# FUNÇÃO QUE MOSTRA SOMENTE NOME, VENCIMENTO E VALOR
def acao_1():
    os.system("cls")
    cursor.execute(
        "SELECT nome, strftime('%d/%m/%Y', vencimento), valor FROM duplicatas"
    )

    saida = cursor.fetchall()

    print(54 * "-")
    print(f"{'TABELA COM FILTROS DE NOME, VENCIMENTO E VALOR':^54}")
    print(54 * "-", "\n")

    print(f"{'NOME':20} {'VENCIMENTO':>12} {'VALOR':>9}")
    print(54 * "-", "\n")

    for nome, vencimento, valor in saida:
        print(f"{nome:<20} | {vencimento:<12} | R$ {valor:<15.2f}")

# 2º
# FUNÇÃO QUE MOSTRA O NUMERO DAS DUPLICATAS DEPOSITADAS NO BANCO ITAU
def acao_2():
    cursor.execute(
        "SELECT numero, banco FROM duplicatas WHERE banco = 'ITAU'"
    )

    saida = cursor.fetchall()

    print(100 * "-")
    print(f"{'TABELA COM FILTROS DO NUMERO DAS DUPLICATAS DEPOSITADAS NO BANCO ITAU':^100}")
    print(100 * "-", "\n")

    print(f"{'NUMERO':>10} {'BANCO':>7}")
    print(100 * "-", "\n")
    
    for numero, banco in saida:
        print(f"{numero:>10} | {banco:<10}")

# 3º
# FUNÇÃO QUE MOSTRA O NÚMERO, VENCIMENTO, VALOR E NOME DAS DUPLICATAS QUE VENCEM NO ANO DE 2017
def acao_3():
    cursor.execute(
        "SELECT numero, vencimento, valor, nome FROM duplicatas WHERE vencimento LIKE '2017%'"
    )

    saida = cursor.fetchall()

    print(100 * "-")
    print(f"{'TABELA QUE MOSTRA O NÚMERO, VENCIMENTO, VALOR E NOME DAS DUPLICATAS QUE VENCEM NO ANO DE 2017':^100}")
    print(100 * "-", "\n")

    print(f"{'NUMERO':^10} {'VENCIMENTO':^14} {'VALOR':^10} {'NOME':^16}")
    print(54 * "-", "\n")
    
    for numero, vencimento, valor, nome in saida:
        print(f"{numero:^10} | {vencimento:^10} | {valor:^10} | {nome:^10}")

# 4º
# FUNÇÃO QUE MOSTRA O NÚMERO, VENCIMENTO, VALOR E NOME DAS DUPLICATAS QUE NÃO ESTÃO DEPOSITADAS NOS BANCOS ITAU E SANTANDER
def acao_4():
    cursor.execute(
        "SELECT numero, vencimento, valor, nome FROM duplicatas WHERE banco != 'ITAU' and banco != 'SANTANDER'"
    )

    saida = cursor.fetchall()

    print(100 * "-")
    print(f"{'TABELA QUE MOSTRA O NÚMERO, VENCIMENTO, VALOR E NOME DAS DUPLICATAS QUE NÃO ESTÃO DEPOSITADAS NOS BANCOS ITAU E SANTANDER.':^100}")
    print(100 * "-", "\n")

    print(f"{'NUMERO':^10} {'VENCIMENTO':^14} {'VALOR':^10} {'NOME':^16}")
    print(54 * "-", "\n")
    
    for numero, vencimento, valor, nome in saida:
        print(f"{numero:^10} | {vencimento:^10} | {valor:^10} | {nome:^10}")

# 5º
# FUNÇÃO QUE MOSTRA VALOR DA DIVIDA DO CLIENTE PAPELARIA SILVA E MOSTRA AS DUPLICATAS
def acao_5():
    cursor.execute("""
        SELECT nome, valor,
        SUM (valor) OVER () AS valor_divida
        FROM duplicatas  
        WHERE nome = 'PAPELARIA SILVA'
    """)

    saida = cursor.fetchall()
    
    print(100 * "-")
    print(f"{'TABELA QUE MOSTRA VALOR DA DIVIDA DO CLIENTE PAPELARIA SILVA E MOSTRA AS DUPLICATAS':^100}")
    print(100 * "-", "\n")

    print(f"{'NOME'} {'VALOR':>23}")
    print(54 * "-", "\n")
    
    for nome, valor, valor_divida in saida:
        print(f"{nome:<18} | {valor:^10}")
        
    print(f"\nVALOR TOTAL DA DÍVIDA: R$ {saida[0][2]}")

# 6º
# FUNÇÃO QUE REMOVE DA TABELA A DUPLICATA 770710 DO CLIENTE LIVRARIA FERNANDES

# TODO: VERIFICAR SE A FUNÇÃO ESTÁ FUNCIONANDO.
# TODO: SOMENTE EXECUTAR ESSA OPÇÃO NA HORA DE PRINTAR PARA COLOCAR NO PDF

def acao_6():
    cursor.execute(
        "DELETE FROM duplicatas WHERE numero = 770710 and nome = 'LIVRARIA FERNANDES'"
    )

    conexao.commit()

    os.system("cls")

    input("DUPLICATA REMOVIDA COM SUCESSO!")
# 7º
# FUNÇÃO QUE APRESENTA UMA LISTAGEM EM ORDEM ALFABÉTICA POR NOME JUNTO COM TODOS OS OUTROS CAMPOS DA TABELA
def acao_7():
    cursor.execute(
        "SELECT nome, numero, valor, vencimento, banco FROM duplicatas ORDER BY nome ASC"
    )

    saida = cursor.fetchall()
    
    print(150 * "-")
    print(f"{'TABELA QUE APRESENTA UMA LISTAGEM EM ORDEM ALFABÉTICA POR NOME JUNTO COM TODOS OS OUTROS CAMPOS DA TABELA':^150}")
    print(150 * "-", "\n")

    print(f"{'NOME'} {'NUMERO':>22} {'VALOR':>9} {'VENCIMENTO':>15} {'BANCO':>7}")
    print(75 * "-", "\n")
    
    for nome, numero, valor, vencimento, banco in saida:
        print(f"{nome:<18} | {numero} | {valor:^10} | {vencimento} | {banco}")

# 8º
# FUNÇÃO QUE APRESENTA UMA LISTAGEM EM ORDEM DE DATA DE VENCIMENTO COM O NOME DO CLIENTE, BANCO, VALOR E VENCIMENTO
def acao_8():
    os.system("cls")
    cursor.execute(
        "SELECT nome, banco, valor, vencimento FROM duplicatas ORDER BY vencimento DESC"
    )

    saida = cursor.fetchall()
        
    print(150 * "-")
    print(f"{'TABELA QUE APRESENTA UMA LISTAGEM EM ORDEM DE DATA DE VENCIMENTO COM O NOME DO CLIENTE, BANCO, VALOR E VENCIMENTO':^150}")
    print(150 * "-", "\n")

    print(f"{'NOME'} {'BANCO':>24} {'VALOR':>21} {'VENCIMENTO':>20}")
    print(75 * "-", "\n")
    
    for nome, banco, valor, vencimento in saida:
        print(f"{nome:<18} | {banco:^15} | {valor:^20} | {vencimento:^10}")

    
while True:
    os.system("cls")
    try:
        resposta_menu = menu()
        if resposta_menu == 0:
            break
        elif resposta_menu == 1:
            os.system("cls")
            tabela_inteira()
            input("~> ")
        elif resposta_menu == 2:
            inserir_dados()
        elif resposta_menu == 3:
            sub_menu()
        else:
            os.system("cls")
            input("Valor inválido!")
    except ValueError:
        os.system("cls")
        input("Valor inválido!") 
        
os.system("cls")