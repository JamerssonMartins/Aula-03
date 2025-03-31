print("Vamos jogar")
print("Tente advinhar o número escolhido entre 1 e 100")
import random
NumAleatorio = random.randint (1,100)
while True:
    number = int(input("Digite um número entre 1 e 100: "))
    if number < NumAleatorio:
        print("Dica: É um número maior")
    elif number > NumAleatorio:
        print("Dica: É um número menor")
    else:
        print("Congratulations! Você acertou")
        break