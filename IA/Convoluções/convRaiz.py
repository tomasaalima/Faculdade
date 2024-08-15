# Definir a imagem
imagem = [
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [5, 4, 3, 1, 2],
    [1, 1, 3, 5, 4],
    [5, 4, 3, 1, 5]
]

# Definir o filtro
filtro = [
    [-1, 0, 1],
    [0, 0, 1],
    [1, -1, 1]
]

# Função para aplicar padding
def aplicar_padding(imagem, padding):
    if padding == 0:
        return imagem
    h_imagem = len(imagem)
    w_imagem = len(imagem[0])
    imagem_padded = [[0] * (w_imagem + 2 * padding) for _ in range(h_imagem + 2 * padding)]
    
    for i in range(h_imagem):
        for j in range(w_imagem):
            imagem_padded[i + padding][j + padding] = imagem[i][j]
    
    return imagem_padded

# Função para aplicar a convolução
def aplicar_convolucao(imagem, filtro, padding=1, stride=1):
    imagem_padded = aplicar_padding(imagem, padding)
    h_imagem = len(imagem_padded)
    w_imagem = len(imagem_padded[0])
    h_filtro = len(filtro)
    w_filtro = len(filtro[0])
    h_saida = (h_imagem - h_filtro) // stride + 1
    w_saida = (w_imagem - w_filtro) // stride + 1
    saida = [[0] * w_saida for _ in range(h_saida)]
    
    for i in range(h_saida):
        for j in range(w_saida):
            soma = 0
            for m in range(h_filtro):
                for n in range(w_filtro):
                    soma += imagem_padded[i * stride + m][j * stride + n] * filtro[m][n]
            saida[i][j] = soma
    
    return saida

# Função para exibir matrizes lado a lado com valores
def mostrar_matrizes_com_valores(matriz1, titulo1, matriz2, titulo2):
    print(titulo1)
    for linha in matriz1:
        print(" ".join(f"{val:4}" for val in linha))
    
    print("\n" + titulo2)
    for linha in matriz2:
        print(" ".join(f"{val:4}" for val in linha))

# Aplicar a convolução
resultado = aplicar_convolucao(imagem, filtro, padding=1, stride=1)

# Exibir as matrizes
mostrar_matrizes_com_valores(imagem, 'Imagem Original', resultado, 'Imagem Convoluida')
