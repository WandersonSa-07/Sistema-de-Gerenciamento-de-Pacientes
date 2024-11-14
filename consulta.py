from datetime import date, time

class Consulta:
    def __init__(self, data: date, hora: time, sintomas_apresentados: str, medico: str, especialidade: str):
        self.data = data
        self.hora = hora
        self.sintomas_apresentados = sintomas_apresentados
        self.medico = medico
        self.especialidade = especialidade

    def cadastrar(self):
        """Cadastra a consulta exibindo as informações de forma organizada."""
        print(f"Consulta cadastrada com sucesso!")
        print(f"Data: {self.data}")
        print(f"Hora: {self.hora}")
        print(f"Sintomas Apresentados: {self.sintomas_apresentados}")
        print(f"Médico: {self.medico}")
        print(f"Especialidade: {self.especialidade}")
    
    def visualizar(self, medico, especialidade_medico):
        """Permite que o médico visualize a consulta se ele for da mesma especialidade."""
        if especialidade_medico == self.especialidade:
            print(f"Consulta encontrada para o médico {medico}:")
            print(f"Data: {self.data}")
            print(f"Hora: {self.hora}")
            print(f"Sintomas Apresentados: {self.sintomas_apresentados}")
            print(f"Especialidade: {self.especialidade}")
        else:
            print(f"O médico {medico} não pode visualizar esta consulta, pois a especialidade não corresponde.")

# Exemplo de uso
consulta1 = Consulta(date(2024, 11, 14), time(10, 30), "Dor de cabeça", "Dr. João", "Neurologista")
consulta1.cadastrar()

# Médico com especialidade correspondente
consulta1.visualizar("Dr. João", "Neurologista")

# Médico com especialidade diferente
consulta1.visualizar("Dr. Carlos", "Cardiologista")