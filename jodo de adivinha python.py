import random

numero = random.randint(1, 100)
tentativas = 0

print("Bem-Vindo ao jogo da adivinhação!")
print("Eu escolhi um numero entre 1 e 100. Você tem 10 tentativas para adivinhar.")

while tentativas < 10:
  palpite = int(input("Digite o seu palpite: "))
  tentativas += 1

  if palpite == numero:
    print(f"Parabens! Você acertou o numero em {tentativas} tentaticas.")
    break
  elif palpite < numero: 
      print("O numero e maior. tente novamente.")

  else: print("O numero e menor. tente novamente.")
else: print(f"Você perdeu! o numero era {numero}.")