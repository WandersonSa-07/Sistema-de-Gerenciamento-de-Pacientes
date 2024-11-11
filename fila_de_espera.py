class FilaDeEspera:
    def __init__(self):
        # Inicializa uma lista vazia para representar a fila e um contador de pacientes
        self._fila = []
        self._num_pacientes = 0  # Número de pacientes na fila

    @property
    def fila(self):
        """Retorna a lista de pacientes na fila."""
        return self._fila

    @property
    def num_pacientes(self):
        """Retorna o número de pacientes na fila."""
        return self._num_pacientes


if __name__ == "__main__":
    # Criando a fila de espera
    fila = FilaDeEspera()

