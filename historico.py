from receita_medica import ReceitaMedica
from consulta import Consulta
from datetime import date, time

class Historico:
    def __init__(self, paciente_nome: str, consulta: Consulta):
        """Histórico do paciente, que só é criado se houver uma consulta."""
        self.paciente_nome = paciente_nome
        self.consultas = [consulta]  # Relaciona a consulta com o histórico do paciente

    def exibir_historico(self):
        """Exibe o histórico do paciente."""
        print(f"Histórico do Paciente: {self.paciente_nome}")
        for consulta in self.consultas:
            print(f"\nConsulta:")
            consulta.cadastrar()  # Exibe os detalhes da consulta associada ao histórico



if __name__ == "__main__":
    # Criando uma consulta
    consulta1 = Consulta(date(2024, 11, 14), time(10, 30), "Dor de cabeça", "Dr. João", "Neurologista")
    consulta1.cadastrar()

    # Criando o histórico do paciente, que inclui a consulta
    historico_paciente = Historico("Carlos Souza", consulta1)

    # Exibindo o histórico do paciente
    historico_paciente.exibir_historico()

