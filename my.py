# -*- coding: utf-8 -*-
"""
    Biblioteca que armazena
    funcoes para manipulacao
    de imagens no Python
"""

import os
import numpy as np
import matplotlib.pyplot as plt

#Questao 2 
def imread(path_imagem):
    return plt.imread(path_imagem, np.uint8)

#Questao 3    
def nchannels(imagem):
    if(len(imagem.shape) == 2):
        return 1
    else:
        return len(imagem[0][0])

#Questao 4
def size(imagem):
    return [len(imagem[0]), len(imagem)]

#Questao 5
def rgb2gray(imagem):
    imgGS = np.zeros([len(imagem), len(imagem[0])], dtype=np.uint8)
    if(len(imagem.shape) > 2):        
        for i in range(len(imagem)):
            for j in range(len(imagem[i])):
                imgGS[i][j] = (imagem[i][j][0]*0.299)+(imagem[i][j][1]*0.587)+(imagem[i][j][2]*0.114)    
    else:
        imgGs = imagem        
    return imgGS    
        
#Questao 6                        
def imreadgray(path_imagem):
    imagem = imread(path_imagem)
    imagemGS = rgb2grey(imagem)
    return imagemGS

#Questao 7
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

#Questao 8
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

#Questao 9
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

#Questao 10
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

#Questao 11
def hist(imagem):    
    if(len(imagem.shape) > 2):
        qtdPixelsComIntensidade = np.zeros([256, 3], dtype=int)
        for i in range(len(imagem)):
            for j in range(len(imagem[i])):
                for k in range(3):
                    qtdPixelsComIntensidade[imagem[i][j][k]][k] += 1
    else:
        qtdPixelsComIntensidade = np.zeros([256], dtype=int)
        for i in range(len(imagem)):
            for j in range(len(imagem[i])):
                qtdPixelsComIntensidade[imagem[i][j]] += 1
        
                    
    return qtdPixelsComIntensidade                    

def showhist(vetHist, bin=1):

    intensidade = np.arange(256)

    if(len(vetHist.shape) == 2):

        barWidth = 0.25
        r = np.arange(256)
        g = [x + barWidth for x in r]
        b = [x + barWidth for x in g]

        vetHistR = [x[0] for x in vetHist]
        vetHistG = [x[1] for x in vetHist]
        vetHistB = [x[2] for x in vetHist]
        
        plt.bar(r, vetHistR, color="red", width=barWidth, label="R")
        plt.bar(g, vetHistG, color="green", width=barWidth, label="G")
        plt.bar(b, vetHistB, color="blue", width=barWidth, label="B")
        plt.xlabel("Intensidades da cor")
        plt.ylabel("Quantidade das intensidades da cor")
        plt.title("Quantidade x Intensidades da cor")
        plt.legend()
            
    else:        

        plt.bar(intensidade, vetHist, color="black")
        plt.xlabel("Niveis de cinza")
        plt.ylabel("Quantidade do nivel de cinza")
        plt.title("Quantidade x Niveis de Cinza")
        
    plt.show()
        
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
    
    

