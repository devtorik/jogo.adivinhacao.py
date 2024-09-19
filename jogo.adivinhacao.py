import random

def jogo_adivinhacao():
    print("Bem-vindo ao Jogo de Adivinhação!")
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    max_tentativas = 10

    print("O bot pensou em um número de 1 a 100.")
    print(f"Você tem {max_tentativas} tentativas para adivinhar.")

    while tentativas < max_tentativas:
        palpite = int(input("Qual é o seu palpite? "))
        tentativas += 1

        if palpite < numero_secreto:
            print("Muito baixo! Tente novamente.")
        elif palpite > numero_secreto:
            print("Muito alto! Tente novamente.")
        else:
            print(f"Parabéns,Você adivinhou o número {numero_secreto} em {tentativas} tentativas.")
            break
    else:
        print(f"Você não adivinhou! O número era {numero_secreto}.")

if __name__ == "__main__":
    jogo_adivinhacao()