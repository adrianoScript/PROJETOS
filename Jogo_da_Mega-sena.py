import random 

sorteio = random.sample(range(1, 61), k = 6)
meujogo = random.sample(range(1, 61), k = 6)

sorteio = set(sorteio)
meujogo = set(meujogo)  

numeros = sorteio.intersection(meujogo)
acertos = len(numeros)
print(' Sorteio:', sorteio)
print('Meu Jogo:', meujogo) 
print('#Acertos:', acertos)
