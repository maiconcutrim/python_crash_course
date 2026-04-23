# reprodução do jogo que o autor do livro desenvolveu quando era criança.
from random import randint
while True:
  n = randint(1,50)
  p = int(input("Eu estou pensando em um número! Tente advinhar o número que eu estou pensando: "))
  while True:
    if p < n:
      p = int(input("Muito baixo! Tente de novo: "))
    elif p > n:
      p = int(input("Muito alto! Tente de novo: "))
    else:
      break
  j = str(input("É isso! Você gostaria de jogar novamente? (yes/no) "))
  if j == "no":
    print("Obrigado por jogar!")
    break