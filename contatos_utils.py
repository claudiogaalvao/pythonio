import csv, pickle, json
from contato import Contato

def read_csv(caminho, encoding='latin_1'):
    contatos = []

    with open(caminho, encoding=encoding) as arquivo:
        leitor = csv.reader(arquivo)        

        for linha in leitor:
            id, nome, email = linha
            
            contato = Contato(id, nome, email)

            contatos.append(contato)

    return contatos

def contatosToPickle(contatos, caminho):
    with open(caminho, mode='wb') as arquivo:
        pickle.dump(contatos, arquivo)
    
def pickleToContatos(caminho):
    with open(caminho, mode='rb') as arquivo:
        contatos = pickle.load(arquivo)

    return contatos

def contatosToJson(contatos, caminho):
    with open(caminho, mode='w') as arquivo:
        json.dump(contatos, arquivo, default=_contatoToJson)

def _contatoToJson(contato):
    return contato.__dict__

def jsonToContatos(caminho):
    with open(caminho) as arquivo:
        contatos_json = json.load(arquivo)
    
    return _jsonToContato(contatos_json)

def _jsonToContato(contatos_json):
    contatos = []

    for contato_json in contatos_json:
        contato = Contato(**contato_json)
        contatos.append(contato)
    
    return contatos