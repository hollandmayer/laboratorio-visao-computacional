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

#Questao 12
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

#Questao 14        
def histeq(imagemEscalaCinza):

    #Verificando se a imagem esta em escala de cinza
    if(nchannels(imagemEscalaCinza) != 1):
        return "Apenas para imagens em escala de cinza"
    else:

        #Gerando histograma da função massa de probabilidade
        h = hist(imagemEscalaCinza)
        r = np.arange(256, dtype=float)
        dimImg = size(imagemEscalaCinza)
        totalPixels = dimImg[0]*dimImg[1]
        for i in range(len(h)):
            r[i] = h[i]/totalPixels
        
        #Calculando o histograma acumulado da funcao massa de probabilidade
        #Esse histograma acumulado normalizado será nossa função de transformação    
        T = np.arange(256, dtype=float)
        T[0] = r[0]
        for i in range(1, len(T)):
            T[i] = T[i-1] + r[i]

        #Normalizando o histograma acumulado...
        for i in range(0, len(T)):
            T[i] = T[i]*255
        
        #Gerando a imagem de histograma normalizado...
        s = np.zeros([len(imagemEscalaCinza), len(imagemEscalaCinza[0])], dtype=np.uint8)
        for i in range(len(s)):
            for j in range(len(s[0])):
                #Função de Transformação!
                #s = T[r]
                s[i][j] = T[imagemEscalaCinza[i][j]]
        
        return s
        
#Questao 15
def convolve(imagem, mascara):
    
    #Primeiro passo: Gerar a imagem com a borda
    #ampliada para que o filtro não diminua a imagem

    #Se a imagem estiver em escala de cinza...
    if(len(imagem.shape) == 2):
        imgParaConv = np.zeros([len(imagem)+2, len(imagem[0])+2], dtype=np.uint8)
    else:    
        imgParaConv = np.zeros([len(imagem)+2, len(imagem[0])+2, 3], dtype=np.uint8)

    #Segundo passo: Preencher a nova imagem com a
    #imagem passada como argumento
    for i in range(len(imagem)):
        for j in range(len(imagem[0])):
            imgParaConv[i+1][j+1] = imagem[i][j]

    #Terceiro passo: Preencher as bordas da imagem nova
    #(repetir pixels mais próximos das bordas)

    #Cantos da nova imagem
    imgParaConv[0][0] = imagem[0][0]
    imgParaConv[len(imgParaConv)-1][0] = imagem[len(imagem)-1][0]
    imgParaConv[0][len(imgParaConv[0])-1] = imagem[0][len(imagem[0])-1]
    imgParaConv[len(imgParaConv)-1][len(imgParaConv[0])-1] = imagem[len(imagem)-1][len(imagem[0])-1]

    #Demais margens da nova imagem		
    #Linhas
    for i in range(len(imagem)):        
        imgParaConv[i+1][0] = imagem[i][0]
        imgParaConv[i+1][len(imgParaConv[0])-1] = imagem[i][len(imagem[0])-1]
    #Colunas
    for i in range(len(imagem[0])):
        imgParaConv[0][i+1] = imagem[0][i]
        imgParaConv[len(imgParaConv)-1][i+1] = imagem[len(imagem)-1][i]    

    #Hora da magia acontecer!
    #Aqui efetuaremos a convolução da imagem pela máscara dada

    #Se a imagem estiver em escala de cinza...
    if(len(imagem.shape) == 2):    
        imgConv = np.zeros([len(imagem), len(imagem[0])], dtype=np.uint8)
        for i in range(1, len(imgParaConv)-1):
            for j in range(1, len(imgParaConv[0])-1):
                li = -int(len(mascara)/2)
                ls = int(len(mascara)/2)+1
                for k in range(li, ls):
                    for l in range(li, ls):
                        imgConv[i-1][j-1] += mascara[k+1][l+1]*imgParaConv[k+i][l+j]
    else:
        imgConv = np.zeros([len(imagem), len(imagem[0]), 3], dtype=np.uint8)
        for i in range(1, len(imgParaConv)-1):
            for j in range(1, len(imgParaConv[0])-1):
                li = -int(len(mascara)/2)
                ls = int(len(mascara)/2)+1
                for k in range(li, ls):
                    for l in range(li, ls):
                        for c in range(3):
                            imgConv[i-1][j-1][c] += mascara[k+1][l+1]*imgParaConv[k+i][l+j][c]
                            
    #Retorna a imagem convolucionada
    return imgConv
    
    
#Questao 16
def maskBlur():
    return (1/16)*np.asarray([[1, 2, 1], [2, 4, 2], [1, 2, 1]])

#Questao 17    
def blur(imagem):
    return convolve(imagem, maskBlur())

#Questao 18
def seSquare3():
    return np.asarray([[1, 1, 1], [1, 1, 1], [1, 1, 1]])

#Questao 19
def seCross3():
    return np.asarray([[0, 1, 0], [1, 1, 1], [0, 1, 0]])

#Questao 20
def erode(imagem, elementoEstruturante):
    pass

#Questao 21
def dilate(imagem, elementoEstruturante):
    pass
    
    

