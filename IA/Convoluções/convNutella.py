import numpy as np
import matplotlib.pyplot as plt

# Definir a imagem
imagem = np.array([
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [5, 4, 3, 1, 2],
    [1, 1, 3, 5, 4],
    [5, 4, 3, 1, 5]
])

# Definir o filtro
filtro = np.array([
    [-1, 0, 1],
    [0, 0, 1],
    [1, -1, 1]
])

# Função para aplicar padding
def aplicar_padding(imagem, padding):
    if padding == 0:
        return imagem
    return np.pad(imagem, pad_width=padding, mode='constant', constant_values=0)

# Função para aplicar a convolução
def aplicar_convolucao(imagem, filtro, padding=1, stride=1):
    # Aplicar padding na imagem
    imagem_padded = aplicar_padding(imagem, padding)
    # Dimensões da imagem e do filtro
    h_imagem, w_imagem = imagem_padded.shape
    h_filtro, w_filtro = filtro.shape
    # Dimensões da saída
    h_saida = (h_imagem - h_filtro) // stride + 1
    w_saida = (w_imagem - w_filtro) // stride + 1
    # Inicializar a matriz de saída
    saida = np.zeros((h_saida, w_saida))
    # Aplicar o filtro na imagem
    for i in range(0, h_saida):
        for j in range(0, w_saida):
            saida[i, j] = np.sum(imagem_padded[i*stride:i*stride+h_filtro, j*stride:j*stride+w_filtro] * filtro)
    return saida

# Aplicar a convolução
resultado = aplicar_convolucao(imagem, filtro, padding=1, stride=1)

# Função para exibir a matriz com valores
def mostrar_matriz_com_valores(ax, matriz, titulo):
    ax.matshow(matriz, cmap='gray')
    for (i, j), val in np.ndenumerate(matriz):
        ax.text(j, i, f'{val:.1f}', ha='center', va='center', color='red')
    ax.set_title(titulo)
    ax.axis('off')

# Exibir as imagens lado a lado
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

mostrar_matriz_com_valores(axs[0], imagem, 'Imagem Original')
mostrar_matriz_com_valores(axs[1], resultado, 'Imagem Convoluída')

plt.show()
