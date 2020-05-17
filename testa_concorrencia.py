contato1='1,Raira,raira@raira.com\n'
contato2='2,Bruno,bruno@bruno.com\n'

with open(file='dados/contatos_escrita.csv', encoding='latin_1', mode='w') as arquivo1:
    arquivo1.write(contato1)

with open(file='dados/contatos_escrita.csv', encoding='latin_1', mode='a') as arquivo2:
    arquivo2.write(contato2)