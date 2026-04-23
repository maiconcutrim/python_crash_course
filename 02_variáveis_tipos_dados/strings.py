# strings
print("Esta é uma sequência de caracteres")
print('Isso também é uma sequência de caracteres')

print('Eu disse ao meu amigo: "Python é minha linguagem favorita!"')
print("A linguagem 'Python' recebeu esse nome em homenagem ao grupo Monty Python, e não à cobra.")
print("Um dos pontos fortes do 'Python' é sua comunidade diversificada e solidária.")

# tabulações e quebra de linha
print("Python")
print("\tPython") # tabulação
print("Languages:\nPython\nC\nJavaScript") # quebra de linha
print("Languages:\n\tPython\n\tC\n\tJavaScript") # tabulação e quebra de linha

# remoção de espaços em brano
favorite_language="Python "
print("'"+favorite_language+"'")
print("'"+favorite_language.rstrip()+"'") # remoção de espços em branco à direita

print("'"+favorite_language+"'")
favorite_language=favorite_language.rstrip() # limpeza do dado e rearmazenamento na variavel
print("'"+favorite_language+"'")

favorite_language=" JavaScript "
print("'"+favorite_language+"'")
print("'"+favorite_language.rstrip()+"'") # remoção de espaços em branco à direita
print("'"+favorite_language.lstrip()+"'") # remoção de espaços em branco à esquerda
print("'"+favorite_language.strip()+"'") # remoção de espaços em branco dos dois lados
