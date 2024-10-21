from gerenciador_tarefas.tarefa import Tarefa
from gerenciador_tarefas.gerenciado import Gerenciador

def main():
    gerenciar_tarefa = Gerenciador()

    while True:
        print("""\n Escolha uma opção:
                    
                [1] Adcionar tarefa
                [2] Remover tarefa
                [3] Listar suas tarefas
                [Q] Sair
              """)
        opcao = input("Digite o numero da opção: ")
        if opcao == "1":
            titulo = input("Dê um titulo para sua tarefa: ")
            descricao = input("Agora dê uma descrição: ")
            tarefa = Tarefa(titulo,descricao)
            gerenciar_tarefa.adicoinar_tarefa(tarefa)

        elif opcao == "2":
            titulo_remover = input("Digite o titulo da tarefa que voce deseja remover: ")
            gerenciar_tarefa.remover_tarefa(titulo_remover)

        elif opcao == "3":
            gerenciar_tarefa.listar_tarefas()

        elif opcao == "Q":
            break

        else:
            print("Opção invalida digite um valor valido")

main()
