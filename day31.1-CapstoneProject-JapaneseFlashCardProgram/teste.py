nome_produto = input("Insira o nome do produto: ")
categoria_produto = input("Insira a categoria do produto: ")
estoque = input("Insira sua quantidade em estoque: ")

if nome_produto == "" or categoria_produto == "" or estoque == "":
    print("Insira os dados corretamente.")

if categoria_produto == "alimentos" and int(estoque) < 50:
    print(f"Solicitar {nome_produto} à equipe de compras. Temos {estoque} em estoque.")

if categoria_produto == "bebidas" and int(estoque) < 75:
    print(f"Solicitar {nome_produto} à equipe de compras. Temos apenas {estoque} em estoque.")

if categoria_produto == "limpeza" and int(estoque) < 30:
    print(f"Solicitar {nome_produto} à equipe de compras. Temos apenas {estoque} em estoque.")