arquivo = open(file='dados/contatos_escrita.csv', encoding='latin_1', mode='a')

print(type(arquivo.buffer))

contato = bytes('3,Verônica,veronica@veronica.com', 'latin_1')

arquivo.buffer.write(contato)



