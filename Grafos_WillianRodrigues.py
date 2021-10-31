
def criaMatriz(matriz, tamanho):
    for i in range (tamanho):
        linha = [] 
        for j in range (tamanho):
            linha += [0]
        matriz += [linha]
    print('\n')

def criaAresta (matriz, vertices):
    for i in range(len(vertices)):
        matriz[0][i+1] = vertices[i]
        matriz[i+1][0] = vertices[i]
    
def adicionaPeso (matriz, tamanho):
    while True:
        while True:
            linha = int(input('\n\n== Digita a posicao que deseja adicionar seu peso ==\n\t LINHA: '))
            coluna = int(input('\tCOLUNA: '))
            
            if linha > 0 and linha < tamanho:
                if coluna > 0 and coluna < tamanho:
                    peso = int(input('\tDigite o peso: ' ))
                    matriz [linha][coluna] = peso
                    break
            else: 
                print('\n\tLinha ou coluna invalido!')
        escolha = int(input('\nDeseja adicionar mais um peso? SIM[1] NAO [0]: '))
        if escolha == 0:
            break

def imprime (matriz, tamanho):
    print('-=' *20)
    for i in range (tamanho):
        for j in range (tamanho):
            if(i==0 or j==0):
                print (f' \t{matriz[i][j]:^8}  ', end='')
            else:
                print (f' \t[{matriz[i][j]:^5}] ', end='')
        print()
    print('-=' *20)



while True:
    tamanho = int(input('Digite a quantidade de vertices: '))
    if tamanho > 1 & tamanho < 20:
        break
    else:
        print('Digite apenas valores entre 1 e 20')

vertices = []
for i in range (tamanho):
    vertices.append((input('Digite o vertice %i: ' %i)))

tamanho = tamanho+1
matriz = []

criaMatriz(matriz, tamanho)
criaAresta(matriz, vertices)
imprime(matriz, tamanho)
adicionaPeso(matriz, tamanho)
imprime(matriz, tamanho)


