import random

def escolher_palavra():
    palavras = ['casa', 'mouse', 'telhado', 'programar', 'corda', 'jogo']
    return random.choice(palavras)

def mostrar_palavra(palavra, letras_corretas):
    resultado = ''
    for letra in palavra:
        if letra in letras_corretas:
            resultado += letra + ' '
        else:
            resultado += '_ '
    return resultado

def jogar():
    palavra = escolher_palavra()
    letras_corretas = []
    tentativas = 6
    
    print("Bem-vindo ao Jogo da Forca!")
    print("A palavra tem", len(palavra), "letras.")
    
    while tentativas > 0:
        print("\nPalavra:", mostrar_palavra(palavra, letras_corretas))
        letra = input("Digite uma letra: ").lower()
        
        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, digite apenas uma letra.")
            continue
        
        if letra in letras_corretas:
            print("Você já tentou esta letra.")
            continue
        
        if letra in palavra:
            print("Ótimo! A letra", letra, "está na palavra.")
            letras_corretas.append(letra)
            
            if len(set(palavra)) == len(letras_corretas):
                print("\nParabéns! Você venceu! A palavra era", palavra)
                break
        else:
            print("Ops! A letra", letra, "não está na palavra.")
            tentativas -= 1
            print("Você tem", tentativas, "tentativas restantes.")
    
    if tentativas == 0:
        print("\nVocê perdeu! A palavra era", palavra)

if __name__ == "__main__":
    jogar()