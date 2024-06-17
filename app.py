import json
import random

# Carregando o arquivo JSON
with open('frases.json') as arquivo:
    frases = json.load(arquivo)

# Selecionando frase aleatória
frase_aleatoria = random.choice(frases)

# Mostrando a frase na linha de comando
print(f"Frase do dia: \"{frase_aleatoria['frase']}\" - {frase_aleatoria['autor']}")
