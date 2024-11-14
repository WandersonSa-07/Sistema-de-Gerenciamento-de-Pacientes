from datetime import date, time
from usuario import Usuario  # Importa a classe base Usuario
from paciente import Paciente
from consulta import Consulta
from receita_medica import ReceitaMedica
from ficha_medica import FichaMedica

class Medico(Usuario):
    def __init__(self, nome, email, crm, telefone=None, especialidade=None):
        super().__init__(nome, email, crm, telefone)
        self.especialidade = especialidade  # Especialidade do médico, como "Cardiologia", "Pediatria", etc.

    def registrar_detalhes_consulta(self, consulta, detalhes):
        consulta.detalhes = detalhes
        print(f"Detalhes da consulta registrados: {detalhes}")

    def acessar_ficha_medica(self, ficha_medica):
        """Acessa a ficha médica e exibe as informações resumidas."""
        resumo = ficha_medica.resumo_ficha_medica()  # Chama o método que retorna o resumo da ficha
        if resumo:  # Verifica se o resumo não é None
            for chave, valor in resumo.items():
                print(f"{chave}: {valor}")
        else:
            print("Erro: Não foi possível acessar os dados da ficha médica.")


    def receita_medica(self, receita_medica):
        print(f"Receita emitida:\nRemédio: {receita_medica.remedio}\nDosagem: {receita_medica.dosagem} "
              f"\nQuantidade por dia: {receita_medica.qtd_por_dia} por {receita_medica.qtd_de_dias} dias")

    def atualizar_medicamentos(self, ficha_medica, novos_medicamentos):
        ficha_medica.atualizar_medicamentos(novos_medicamentos)
        print(f"Medicamentos atualizados: {novos_medicamentos}")

if __name__ == "__main__":
    # Criando o objeto Medico
    medico = Medico(nome="Dr. João", email="joao@hospital.com", crm="CRM12345", telefone="11987654321", especialidade="Cardiologia")

    # Criando o objeto Paciente
    paciente = Paciente(
        nome="Gabriel Pinheiro",
        email="gabrielpinheiro@gmail.com",
        codigo="123456789101",
        telefone="22999777888",
        idade=30,
        profissao="Estudante",
        sexo="Masculino"
    )

    # Definindo os dados da consulta
    data_consulta = date(2024, 11, 11)
    hora_consulta = time(14, 30)
    sintomas = "Dor de cabeça intensa e tontura"
    medico_nome = "Dr. João Silva"
    especialidade = "Neurologia"

    # Criando a instância da consulta
    consulta = Consulta(data=data_consulta, hora=hora_consulta, sintomas_apresentados=sintomas, medico=medico_nome, especialidade=especialidade)

    # Cadastrando a consulta
    consulta.cadastrar()

    # Teste 1: Registrar detalhes da consulta
    medico.registrar_detalhes_consulta(consulta, "Paciente com sintomas de dor de cabeça.")
    print("Detalhes da Consulta:", consulta.detalhes)  

    # Teste 2: Acessar ficha médica do paciente
    # Criando a ficha médica
    ficha_medica = FichaMedica(
    formacao_medico="Neurologia",
    alergias="Penicilina",
    medicamentos_em_uso="Paracetamol",
    observacoes="Paciente diabético"
    )


    # Adicionando uma consulta à ficha médica
    ficha_medica.adicionar_consulta(consulta)

    # Exibindo o resumo da ficha médica
    print("\nResumo da Ficha Médica:")
    medico.acessar_ficha_medica(ficha_medica)

    # Teste 3: Emitir uma receita médica
    receita = ReceitaMedica(remedio="Naproxeno", dosagem="50mg", qtd_por_dia=2, qtd_de_dias=30)
    medico.receita_medica(receita)

    # Teste 4: Atualizar medicamentos na ficha médica
    novos_medicamentos = ["Naproxeno 50mg", "Triptanos 100mg"]
    medico.atualizar_medicamentos(ficha_medica, novos_medicamentos)
    print("Medicamentos na Ficha Médica:", ficha_medica.medicamentos_em_uso)  
