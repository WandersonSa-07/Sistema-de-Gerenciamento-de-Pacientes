class FichaMedica:
    def __init__(self, formacao_medico, alergias, medicamentos_em_uso, observacoes):
        self.formacao_medico = formacao_medico            # Formação do médico responsável pela ficha
        self.alergias = alergias                          # Alergias do paciente
        self.medicamentos_em_uso = medicamentos_em_uso    # Medicamentos em uso pelo paciente
        self.consultas = []                               # Lista de consultas (inicia vazia)
        self.observacoes = observacoes                    # Observações gerais sobre o paciente
        self.exames = []                                  # Lista de exames/histórico (inicia vazia)

    def resumo_ficha_medica(self):
        """Exibe um resumo da ficha médica do paciente e retorna como um dicionário."""
        resumo = {
            'Formação do Médico': self.formacao_medico,
            'Alergias': self.alergias,
            'Medicamentos em Uso': self.medicamentos_em_uso,
            'Observações': self.observacoes,
            'Consultas': self.consultas if self.consultas else "Nenhuma consulta registrada.",
            'Exames': self.exames if self.exames else "Nenhum exame registrado."
        }
        return resumo
    

    def adicionar_consulta(self, consulta):
        self.consultas.append(consulta)
        print("Consulta adicionada com sucesso à ficha médica.")
    
    def adicionar_exame(self, exame):
        self.exames.append(exame)
        print("Exame adicionado com sucesso ao histórico.")

    def atualizar_medicamentos(self, novos_medicamentos):
        """Atualiza a lista de medicamentos em uso do paciente."""
        self.medicamentos_em_uso = novos_medicamentos
        print("Medicamentos atualizados com sucesso.")
