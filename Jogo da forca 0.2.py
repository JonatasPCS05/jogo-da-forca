import random
import os

def tela(palavra, verificador_acerto_letras, dica, chances, letras_usadas):
    print(f"\033[44mDica: {dica}\033[m"," "*10,f"\033[41mChances: {chances}\033[m")
    print(f"Letras usadas: {letras_usadas}")
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

def sistema(palavra,verificador_acerto_letras, chances):
    tela(palavra, verificador_acerto_letras, dica, chances, letras_usadas)
    letra = input("Digite uma letra: ")
    letras_usadas.append(letra)
    if letra in ["a", "e", "i", "o", "u", "c"]:
        letra = ajustar_letras(letra)
    perdeu = 0
    for i in range(0, len(palavra)):
        if palavra[i] in letra:
            verificador_acerto_letras[i] = True
            perdeu += 1
        else:
            continue
    return perdeu

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
dica = dica[n1]
verificador_acerto_letras = []
letras_usadas = []
chances = 10

for i in range(0, len(palavra)):
    if palavra[i] == " ":
        verificador_acerto_letras.append(True)
    else:
        verificador_acerto_letras.append(False)

while False in verificador_acerto_letras:
    perdeu = sistema(palavra,verificador_acerto_letras, chances)
    if perdeu == 0:
        chances -= 1
    else:
        continue
    if chances == 0:
        exit()
    else:
        continue