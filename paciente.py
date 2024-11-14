from usuario import Usuario  # Importa a classe base Usuario

class Paciente(Usuario):
    def __init__(self, nome, email, codigo, telefone, idade, profissao, sexo):
        # Inicializa a classe pai Usuario
        super().__init__(nome, email, codigo, telefone)
        
        # Verifica se o telefone foi fornecido e é válido
        if telefone is None:
            raise ValueError("O número de telefone é obrigatório para pacientes.")
        
        # Validação para o atributo sexo
        if sexo not in ["Masculino", "Feminino"]:
            raise ValueError("O sexo deve ser 'Masculino' ou 'Feminino'.")
        
        # Atributos específicos de Paciente
        self.idade = idade
        self.profissao = profissao
        self.sexo = sexo
    
    def marcar_consulta(self):
        """Método para marcar uma consulta. Implementação futura."""
        pass  # Será implementado posteriormente
    
    def visualizar_receita(self, receita):
        """Visualiza uma receita médica existente.
        
        Parâmetros:
        receita (ReceitaMedica): Instância da classe ReceitaMedica.
        """
        print(f"Receita para {self._nome}:")
        print(receita.obter_detalhes())  # Exibe detalhes da receita


if __name__ == "__main__":
    try:
        # Criando um paciente com sexo válido
        paciente = Paciente(
            nome="João Luiz",
            email="joaoluiz@gmail.com",
            codigo="123456789101",
            telefone="22999777888",
            idade=30,
            profissao="Professor",
            sexo="Masculino"  # Valor válido
        )
    except ValueError as e:
        print(e)  # Output: O sexo deve ser 'Masculino' ou 'Feminino'.

    # Tentando criar um paciente com um valor de sexo inválido
    # try:
    #     paciente_invalido = Paciente(
    #         nome="Maria Souza",
    #         email="maria@exemplo.com",
    #         codigo="CPF987654321",
    #         telefone="10987654321",
    #         idade=28,
    #         profissao="Médica",
    #         sexo="Outro"  # Valor inválido
    #     )
    # except ValueError as e:
    #     print(e)  # Output: O sexo deve ser 'Masculino' ou 'Feminino'.
