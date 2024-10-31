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
        # Método para visualizar a fila de espera
        return self.fila_espera

    def acompanhar_relatorio(self):
        # Método para acompanhar o relatório (implementação pode variar)
        pass


# Importar a classe FilaDeEspera (assumindo que ela já foi implementada)
fila = FilaDeEspera()

# Criar uma instância da Atendente com a fila de espera
atendente = Atendente("Mariana", "mariana@hospital.com", "ID456", fila)

# Login da Atendente
atendente.login("mariana@hospital.com", "ID456")

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
