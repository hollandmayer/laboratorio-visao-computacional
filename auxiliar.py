# -*- coding: utf-8 -*-
"""
    Biblioteca auxiliar
    para executar funcoes
    de outras bibliotecas
"""

import matplotlib.pyplot as plt

def exibeImagem(imagem):
    plt.figure(figsize=(3, 3))
    im = plt.imshow(imagem, aspect='auto')
    plt.axis('off')
    plt.show()
