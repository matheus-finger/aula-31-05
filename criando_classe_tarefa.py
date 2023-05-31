class Tarefa:
    """
    Classe principal do programa
    """
    def __init__(self, prioridade, texto):
        self.prioridade = prioridade
        self.texto = texto

    def __str__(self):
        prioridade = self.prioridade
        texto = self.texto
        return f"Prioridade: {prioridade}\nTexto: {texto}"

    def __eq__(self, outra) -> bool:
        if self.texto == outra.texto:
            return True
        return False
    
    def maior(self, outra) -> bool:
        if self.prioridade > outra.prioridade:
            return True
        elif self.prioridade < outra.prioridade:
            return False
        else:
            if self.texto > self.prioridade:
                return True
            else:
                return False
    
class GerenciadorDeTarefas:
    def __init__(self):
        self.lista = []

    def adiciona_tarefa(self, tarefa: Tarefa):
        self.lista.append(tarefa)

    def remove_tarefas(self, indices: tuple[int]):
        for indice in reversed(indices):
            self.lista.pop(indice)
    
    def ordena_tarefas(self):
        pass



# x é um objeto da classe tarefa
x = Tarefa(True, "Nada")
x.prioridade = False

# se eu tentar imprimir sem definir o método __str__, ele vai só imprimir que a variável é um objeto de Tarefa.
print(x)

gerenciador = GerenciadorDeTarefas()
gerenciador.adiciona_tarefa(gerenciador)

y = Tarefa(True, "Nada")

if x == y:
    print('As tarefas são iguais')