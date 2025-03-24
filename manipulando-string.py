texto = "Nossa aula manipulando String."

print(texto[0:20:2])
'''Exibe todas as letras entre 0 a 20'''

print(len(texto))
'''Indica o tamanho do texto, quantos caracteres ele possui'''

print(texto.count("a"))
'''Conta quantas vezes o caracter foi usado na String'''

print(texto.count("a", 5, 30))
'''Conta quantas vezes o caracter foi usado na String entre 5 a 30'''

print(texto.find("aula"))
'''Procura a palavra pesquisada na string e indica a posição'''

print(texto.find("Python"))
'''Caso não encontre, dará o resultado -1'''

print('String' in texto)
'''Confere se a palavra a ser exibida está no texto'''

print('Raphael' in texto)
'''Caso não esteja, dará o resultado False'''

print(texto.split())
'''Separa o texto por cada palavra'''