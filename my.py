# -*- coding: utf-8 -*-
"""
    Biblioteca que armazena
    funcoes para manipulacao
    de imagens no Python
"""

import os
import numpy as np
import matplotlib.pyplot as plt

def imread(path_imagem):
    return plt.imread(path_imagem, np.uint8)
    
def nchannels(imagem):
    if(len(imagem.shape) == 2):
        return 1
    else:
        return len(imagem[0][0])

def size(imagem):
    return [len(imagem[0]), len(imagem)]

def rgb2gray(imagem):
    imgGS = np.zeros([len(imagem), len(imagem[0])], dtype=np.uint8)
    if(len(imagem.shape) > 2):        
        for i in range(len(imagem)):
            for j in range(len(imagem[i])):
                imgGS[i][j] = (imagem[i][j][0]*0.299)+(imagem[i][j][1]*0.587)+(imagem[i][j][2]*0.114)    
    else:
        imgGs = imagem        
    return imgGS    
        
                        
def imreadgray(path_imagem):
    imagem = imread(path_imagem)
    imagemGS = rgb2grey(imagem)
    return imagemGS

def imshow(imagem):    
    if(len(imagem.shape) == 2):
        #Para questao 7
        #im = plt.imshow(imagem, cmap='gray', interpolation='nearest')
        #Para questao 10 letra a
        im = plt.imshow(imagem, cmap=None, interpolation='nearest')
    else:
        im = plt.imshow(imagem, cmap=None, interpolation='nearest')
    plt.axis('off')
    plt.show()

def thresh(imagem, limiar):
    if(len(imagem.shape) > 2):
        imgTh = np.zeros([len(imagem), len(imagem[0]), 3], dtype=np.uint8)
        for i in range(len(imagem)):
            for j in range(len(imagem[i])):
                if(imagem[i][j][0] >= limiar):
                    imgTh[i][j][0] = 255
                else:
                    imgTh[i][j][0] = 0
                    
                if(imagem[i][j][1] >= limiar):
                    imgTh[i][j][1] = 255
                else:
                    imgTh[i][j][1] = 0
                    
                if(imagem[i][j][2] >= limiar):
                    imgTh[i][j][2] = 255
                else:
                    imgTh[i][j][2] = 0    
    else:
        imgTh = np.zeros([len(imagem), len(imagem[0])], dtype=np.uint8)
        for i in range(len(imagem)):
            for j in range(len(imagem[i])):
                if(imagem[i][j] >= limiar):
                    imgTh[i][j] = 255
                else:
                    imgTh[i][j] = 0
    return imgTh       

def negative(imagem):
    if(len(imagem.shape) > 2):        
        imgNeg = np.zeros([len(imagem), len(imagem[0]), 3], dtype=np.uint8)
        for i in range(len(imagem)):
            for j in range(len(imagem[i])):
                imgNeg[i][j][0] = 255 - imagem[i][j][0]
                imgNeg[i][j][1] = 255 - imagem[i][j][1]
                imgNeg[i][j][2] = 255 - imagem[i][j][2]    
    else:
        imgNeg = np.zeros([len(imagem), len(imagem[0])], dtype=np.uint8)
        for i in range(len(imagem)):
            for j in range(len(imagem[i])):
                imgNeg = 255 - imagem[i][j]        
    return imgNeg 

def contrast(imagem, r, m):
    if(len(imagem.shape) > 2):
        imgContr = np.zeros([len(imagem), len(imagem[0]), 3], dtype=np.uint8)
        for i in range(len(imagem)):
            for j in range(len(imagem[i])):
                imgContr[i][j][0] = round(r * (imagem[i][j][0] - m) + m)
                imgContr[i][j][1] = round(r * (imagem[i][j][1] - m) + m)
                imgContr[i][j][2] = round(r * (imagem[i][j][2] - m) + m)
    else:
        imgContr = np.zeros([len(imagem), len(imagem[0])], dtype=np.uint8)
        for i in range(len(imagem)):
            for j in range(len(imagem[i])):
                imgContr[i][j] = round(r * (imagem[i][j] - m) + m)
    return imgContr                

def hist(imagem):
    if(len(imagem.shape) > 2):
        qtdPixelsComIntensidade = np.zeros([256, 3], dtype=int)
        for i in range(len(imagem)):
            for j in range(len(imagem[i])):
                for w in range(3):
                    for k in range(256):
                        if(imagem[i][j][w] == k):
                            qtdPixelsComIntensidade[k][w] += 1
                            break                           
    return qtdPixelsComIntensidade                    

def showhist(vetHist, bin=1):
    pass

def histeq(imagemEscalaCinza):
    pass

def convolve(imagem, mascara):
    pass

def maskBlur():
    #return (1/16)*[[1, 2, 1], [2, 4, 2], [1, 2, 1]]
    pass	

def blur(imagem, mascara):
    pass

def seSquare3():
    return [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

def seCross3():
    return [[0, 1, 0], [1, 1, 1], [0, 1, 0]]

def erode(imagem, elementoEstruturante):
    pass

def dilate(imagem, elementoEstruturante):
    pass
    
    

