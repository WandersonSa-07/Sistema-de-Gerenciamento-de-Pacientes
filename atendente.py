# Classe Atendente herda de Usuario
from usuario import Usuario

from fila_de_espera import FilaDeEspera

class Atendente(Usuario):
    def __init__(self, nome, email, id_funcional, fila_espera):
        super().__init__(nome, email, id_funcional)
        self.fila_espera = fila_espera  # Fila de espera que a atendente controla

    def login(self, email, id_funcional):
        """Realiza o login da atendente usando o email e o ID Funcional."""
        if self._email == email and self._codigo == id_funcional:
            print(f"{self._nome} logado com sucesso como Atendente.")
        else:
            print("Credenciais de Atendente inválidas.")

    def visualizar_fila(self):
        """Permite ao atendente manipular a fila de espera."""
        # Exemplo de uso dos métodos de FilaDeEspera
        print("Fila de Espera Atual:")
        for i, paciente in enumerate(self.fila_espera._fila, start=1):
            print(f"{i}: {paciente}")

    def inserir_paciente_na_fila(self, paciente):
        """Insere um paciente no final da fila de espera."""
        self.fila_espera.inserir_paciente(paciente)

    def remover_paciente_da_fila(self):
        """Remove o paciente no início da fila de espera."""
        self.fila_espera.remover_paciente()

    def posicao_paciente_na_fila(self, paciente):
        """Retorna a posição de um paciente na fila de espera."""
        return self.fila_espera.posicao(paciente)

    def _acompanhar_Relatorio(self, relatorio):
        """Método protegido para acompanhar o relatório de pacientes."""
        print(f"Acompanhando o relatório: {relatorio.obter_detalhes()}")


# Importar a classe FilaDeEspera (assumindo que ela já foi implementada)
fila_espera = FilaDeEspera()

# Criar uma instância da Atendente com a fila de espera
atendente = Atendente("Mariana", "mariana@hospital.com", "ID456", fila_espera)

# Login da Atendente
atendente.login("mariana@hospital.com", "ID456")

# Interações da Atendente com a fila de espera
atendente.inserir_paciente_na_fila("Paciente A")
atendente.inserir_paciente_na_fila("Paciente B")
atendente.inserir_paciente_na_fila("Paciente C")

# Verificar posição de um paciente específico
atendente.verificar_posicao_paciente("Paciente B")

# Remover o primeiro paciente da fila
atendente.remover_paciente_da_fila()

# Verificar novamente a posição dos pacientes após a remoção
atendente.verificar_posicao_paciente("Paciente B")
