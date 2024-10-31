class ReceitaMedica:
    def __init__(self, remedio: str, dosagem: float, qtd_de_dias: int, qtd_por_dia: int):
        self._remedio = remedio             # Nome do remédio que o paciente deve tomar
        self._dosagem = dosagem             # Quantidade em ml/g
        self._qtd_de_dias = qtd_de_dias      # Duração do tratamento em dias
        self._qtd_por_dia = qtd_por_dia      # Quantidade de doses por dia

    def get_receita(self) -> str:
        """
        Retorna uma descrição detalhada da receita.
        """
        return (
            f"Remédio: {self._remedio}\n"
            f"Dosagem: {self._dosagem} ml/g\n"
            f"Quantidade de dias: {self._qtd_de_dias}\n"
            f"Quantidade por dia: {self._qtd_por_dia}"
        )

    # Métodos de acesso e modificação (getter e setter) para cada atributo

    @property
    def remedio(self) -> str:
        return self._remedio

    @remedio.setter
    def remedio(self, valor: str):
        if valor:  # Verifica se o nome do remédio não é vazio
            self._remedio = valor

    @property
    def dosagem(self) -> float:
        return self._dosagem

    @dosagem.setter
    def dosagem(self, valor: float):
        if valor > 0:  # Verifica se a dosagem é positiva
            self._dosagem = valor

    @property
    def qtd_de_dias(self) -> int:
        return self._qtd_de_dias

    @qtd_de_dias.setter
    def qtd_de_dias(self, valor: int):
        if valor > 0:  # Verifica se a quantidade de dias é positiva
            self._qtd_de_dias = valor

    @property
    def qtd_por_dia(self) -> int:
        return self._qtd_por_dia

    @qtd_por_dia.setter
    def qtd_por_dia(self, valor: int):
        if valor > 0:  # Verifica se a quantidade por dia é positiva
            self._qtd_por_dia = valor



# Instanciando a classe ReceitaMedica
receita = ReceitaMedica(remedio="Paracetamol", dosagem=500.0, qtd_de_dias=7, qtd_por_dia=3)

# Exibindo a receita completa usando o método get_receita
print("Informações da Receita Médica:")
print(receita.get_receita())

# Testando os getters (acesso aos atributos protegidos via @property)
print("\nAcessando os atributos individualmente:")
print("Remédio:", receita.remedio)
print("Dosagem:", receita.dosagem)
print("Quantidade de dias:", receita.qtd_de_dias)
print("Quantidade por dia:", receita.qtd_por_dia)

# Testando os setters (modificação dos atributos com validação)
print("\nModificando os atributos com validação:")

# Modificando o nome do remédio
receita.remedio = "Ibuprofeno"
print("Novo Remédio:", receita.remedio)

# Modificando a dosagem
receita.dosagem = 200.0
print("Nova Dosagem:", receita.dosagem)

# Modificando a quantidade de dias
receita.qtd_de_dias = 10
print("Nova Quantidade de Dias:", receita.qtd_de_dias)

# Modificando a quantidade por dia
receita.qtd_por_dia = 2
print("Nova Quantidade por Dia:", receita.qtd_por_dia)

# Exibindo a receita atualizada
print("\nInformações da Receita Médica Atualizada:")
print(receita.get_receita())

