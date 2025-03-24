def exemplo_find(txt: str) -> str:
    '''Função para encontrar índice inicial da palavra pesquisada'''

    return txt.find('Ciao')

if __name__ == "__main__":
    print(exemplo_find("Olá"))