class FilaDeEspera:
    def __init__(self):
        # Inicializa uma lista vazia para representar a fila
        self._fila = []

    def inserir_paciente(self, paciente):
        """Insere um paciente no final da fila."""
        self._fila.append(paciente)
        print(f"Paciente {paciente} inserido no final da fila.")

    def remover_paciente(self):
        """Remove o paciente no início da fila, se houver algum."""
        if self._fila:
            paciente_removido = self._fila.pop(0)
            print(f"Paciente {paciente_removido} removido do início da fila.")
        else:
            print("A fila está vazia. Nenhum paciente para remover.")

    def posicao(self, paciente):
        """Retorna a posição do paciente na fila (1 para o primeiro da fila, 2 para o segundo, etc.)."""
        if paciente in self._fila:
            # Retorna a posição do paciente na fila, somando 1 pois as listas começam no índice 0
            posicao = self._fila.index(paciente) + 1
            print(f"O paciente {paciente} está na posição {posicao}.")
            return posicao
        else:
            print(f"Paciente {paciente} não está na fila.")
            return -1



# Criando a fila de espera
fila = FilaDeEspera()

# Inserindo pacientes na fila
fila.inserir_paciente("Wanderson")
fila.inserir_paciente("Gabriela")
fila.inserir_paciente("João")

# Verificando a posição de um paciente
fila.posicao("Wanderson")
fila.posicao("Gabriela") 
fila.posicao("João") 

# Removendo um paciente do início da fila
fila.remover_paciente()

# Verificando a posição novamente após a remoção
fila.posicao("Gabriela")  # Deve retornar 1 agora
fila.posicao("Wanderson")  # Deve retornar -1, pois foi removido
fila.posicao("João") 