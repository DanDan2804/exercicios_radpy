def exemplo_encontrar(txt: str) -> str:
    '''Função para encontrar índice inicial da palavra pesquisada'''

    return txt.find('Olá')

if __name__ == "__main__":
    print(exemplo_encontrar("Olá"))