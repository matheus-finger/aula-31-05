import time
import timeit
import random

def marca_tempo(funcao):
    def embrulho(*args, **kargs):
        antes = time.process_time()
        # o asterisco aqui serve para desempacotar as tuplas que vem do *args
        funcao(*args, **kargs)
        depois = time.process_time()
        print('Demorou', depois - antes, 'segundos')
    return embrulho

def chamadas(funcao):
    def embrulho(*args, **kargs):
        print('Chamando a função', funcao)
        funcao(*args, **kargs)
    return embrulho

@marca_tempo
@chamadas
def calcula_algo(menor):
    [random.randint(menor, 1000) for x in range(5*10**6)].sort()

@marca_tempo
@chamadas
def calcula_algo_mais_rapido():
    [random.randint(0, 1000) for x in range(5*10**3)].sort()
    time.sleep(0.1)


def quantidade_generica(primeiro=10, *args, **kargs):
    for arg in args:
        print(arg)
    for key, value in kargs.items():
        print('Outros argumentos', key, value)

# mesma coisa do @
# calcula_algo = chamadas(calcula_algo)

if __name__ == '__main__':
    # Quero chamar as duas funções mas quero guardar cada chamada em um bloco
    # Quero também calcular o tempo que elas demoram
    calcula_algo(100)
    # calcula_algo_mais_rapido()
    # quantidade_generica(1)
    # quantidade_generica(1, 2, delta=10, alpha = 5)
    # quantidade_generica()