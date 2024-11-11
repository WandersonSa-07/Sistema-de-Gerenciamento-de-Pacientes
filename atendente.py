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

    def inserir_paciente_na_fila(self, paciente):
        """Insere um paciente no final da fila de espera e atualiza o contador."""
        self.fila_espera._fila.append(paciente)
        self.fila_espera._num_pacientes += 1
        print(f"Paciente {paciente} inserido na fila.")

    def remover_paciente_da_fila(self):
        """Remove o paciente no início da fila de espera e atualiza o contador."""
        if self.fila_espera._fila:
            paciente_removido = self.fila_espera._fila.pop(0)
            self.fila_espera._num_pacientes -= 1
            print(f"Paciente {paciente_removido} removido da fila.")
        else:
            print("A fila está vazia. Nenhum paciente para remover.")

    def visualizar_fila(self):
        """Exibe todos os pacientes na fila de espera."""
        if self.fila_espera._fila:
            print("Fila de Espera Atual:")
            for i, paciente in enumerate(self.fila_espera._fila, start=1):
                print(f"{i}: {paciente}")
        else:
            print("A fila está vazia.")

    def acompanhar_relatorio(self):
        # Método para acompanhar o relatório (implementação pode variar)
        pass

# Exemplo de teste
if __name__ == "__main__":
    # Cria a fila de espera e a atendente
    fila_espera = FilaDeEspera()
    atendente = Atendente("Mariana", "mariana@hospital.com", "ID456", fila_espera)

    # Login da Atendente
    atendente.login("mariana@hospital.com", "ID456")

    # Inserir pacientes na fila
    atendente.inserir_paciente_na_fila("Wanderson")
    atendente.inserir_paciente_na_fila("Gabriela")
    atendente.inserir_paciente_na_fila("João")

    # Visualizar fila após inserções
    atendente.visualizar_fila()

    # Remover paciente da fila e visualizar novamente
    atendente.remover_paciente_da_fila()
    atendente.visualizar_fila()

    # Remover mais um paciente e visualizar a fila final
    atendente.remover_paciente_da_fila()
    atendente.visualizar_fila()
