from datetime import time

class Relatorio:
    def __init__(self, medico: str, formacao_medico: str, horario_consulta: time, horario_consulta_marcada: time):
        self.medico = medico
        self.formacao_medico = formacao_medico
        self.horario_consulta = horario_consulta
        self.horario_consulta_marcada = horario_consulta_marcada

    def horario_atraso(self):
        """Verifica se o médico está atrasado e calcula o atraso em minutos."""
        # Se o horário da consulta for maior que o horário marcado, calcula o atraso
        if self.horario_consulta > self.horario_consulta_marcada:
            atraso_minutos = (self.horario_consulta.hour - self.horario_consulta_marcada.hour) * 60 + (self.horario_consulta.minute - self.horario_consulta_marcada.minute)
            return atraso_minutos
        else:
            return 0  # Sem atraso

    def exibir_relatorio(self):
        """Exibe o relatório de consulta do médico."""
        atraso = self.horario_atraso()
        if atraso > 0:
            print(f"O médico {self.medico} está {atraso} minutos atrasado para a consulta.")
        else:
            print(f"O médico {self.medico} está no horário para a consulta.")

# Exemplo de uso
relatorio1 = Relatorio("Dr. João", "Neurologista", time(14, 45), time(14, 30))  # Médico atrasado
relatorio2 = Relatorio("Dr. Ana", "Cardiologista", time(10, 30), time(10, 30))  # Médico no horário

relatorio1.exibir_relatorio()
relatorio2.exibir_relatorio()
