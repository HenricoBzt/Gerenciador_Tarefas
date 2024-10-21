

class Gerenciador:
    def __init__(self):
        self.tarefas = []

    def adicoinar_tarefa(self,tarefa):
        self.tarefas.append(tarefa)
        print("Nova tarefa adicionada na lista!")

    def remover_tarefa(self,titulo):
        for tarefa in self.tarefas:
            if tarefa.titulo == titulo:
                self.tarefas.remove(tarefa)
                print(f"Tarefa {titulo} removida com sucesso!")
        print("Tarefa não encontrada!")

    def listar_tarefas(self):
        lista_tarefa = self.tarefas
        if not lista_tarefa:
            print("Nenhuma tarefa encontrada!")
        for indice,tarefa in enumerate(lista_tarefa,1):
            print(f'{indice} - {tarefa}')
            