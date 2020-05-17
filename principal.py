try:
    with open('dados/contatos.csv', encoding='latin_1') as arquivo_contatos:
        for contato in arquivo_contatos:
            print(contato, end='')
except FileNotFoundError:
    print("Arquivo não existe")