arquivo_contatos = open(file='dados/contatos_escrita.csv', encoding='latin_1', mode='a+')

contatos = ['13,Claudio,claudio@claudio.com.br\n',
            '14,Carina,carina@carina.com.br\n',
            '15,Felipe,felipe@felipe.com\n',
            '16,André,andre@andre.com\n']

for contato in contatos:
    arquivo_contatos.write(contato)

#salva alterações no arquivo, então o ponteiro vai para o final do arquivo
arquivo_contatos.flush()

#para realizar a leitura dos dados em seguida, é necessário resetar o ponteiro para a posição 0 do arquivo
arquivo_contatos.seek(0)

for linha in arquivo_contatos:
    print(linha, end='')