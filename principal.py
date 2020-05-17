import contatos_utils

try:
    # contatos = contatos_utils.read_csv('dados/contatos.csv')
    # contatos_utils.contatosToPickle(contatos, 'dados/contatos.pickle')
    
    # contatos = contatos_utils.pickleToContatos('dados/contatos.pickle')
    # contatos_utils.contatosToJson(contatos, 'dados/contatos.json')

    contatos = contatos_utils.jsonToContatos('dados/contatos.json')

    for contato in contatos:
        print(f"{contato.id} - {contato.nome} - {contato.email}")
except FileNotFoundError:
    print("Arquivo não existe")