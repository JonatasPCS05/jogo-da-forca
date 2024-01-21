import random
import os

def tela(palavra, verificador_acerto_letras):
    for i in range(0, len(palavra)):
        if i == len(palavra)-1:
            if verificador_acerto_letras[i] == False:
                print("_")
            else:
                print(palavra[i])
        else:
            if verificador_acerto_letras[i] == False:
                print("_", end=" ")
            else:
                print(palavra[i], end=" ")
def sistema(palavra,verificador_acerto_letras):
    tela(palavra, verificador_acerto_letras)
    letra = input("Digite uma letra: ")
    if letra in ["a", "e", "i", "o", "u", "c"]:
        letra = ajustar_letras(letra)
    for i in range(0, len(palavra)):
        if palavra[i] in letra:
            verificador_acerto_letras[i] = True
        else:
            continue

def ajustar_letras(letra):
    if letra == "a":
        letra = ["a", "á", "à", "ã", "â"]
    if letra == "e":
        letra = ["e", "é", "è", "ê"]
    if letra == "i":
        letra = ["i", "í", "ì", "î"]
    if letra == "o":
        letra = ["o", "ó", "ò", "õ", "ô"]
    if letra == "u":
        letra = ["u", "ú", "ù", "û"]
    if letra == "c":
        letra = ["c", "ç"]
    return letra

palavras = [["abacate", "abacaxi", "açaí", "acerola", "amora"], ["administração", "administração publica", "agronegócios e agropecuária"]]
dica = ["Fruta", "Profissões"]

n1 = random.randint(0, len(dica)-1)
n2 = random.randint(0, len(palavras[n1])-1)
palavra = palavras[n1][n2]
verificador_acerto_letras = []

for i in range(0, len(palavra)):
    if palavra[i] == " ":
        verificador_acerto_letras.append(True)
    else:
        verificador_acerto_letras.append(False)

while False in verificador_acerto_letras:
    sistema(palavra,verificador_acerto_letras)