class Usuario:
    def __init__(self, nome, email, codigo, telefone=None):
        self._nome = nome
        self._email = email
        self._codigo = codigo  # Pode ser CPF, CRM ou ID funcional, dependendo do tipo de usuário
        self._telefone = telefone  # Telefone opcional
        self._autenticado = False  # Estado inicial de autenticação

        # Verifica se o telefone é válido (11 dígitos) se fornecido
        if telefone is not None:
            if isinstance(telefone, str) and len(telefone) == 11 and telefone.isdigit():
                self._telefone = telefone
            else:
                raise ValueError("O número de telefone deve conter exatamente 11 dígitos.")
        else:
            self._telefone = None


    def logar(self):
        senha = input(f"Digite a senha: ")
        if senha == self._codigo:  # Usando o atributo privado
            self._autenticado = True
            print(f"{self._nome} logado com sucesso.")
        else:
            print("Senha incorreta. Tente novamente.")

    def deslogar(self):
        if self._autenticado:  # Verifica o estado protegido
            self._autenticado = False
            print(f"{self._nome} deslogado com sucesso.")
        else:
            print(f"{self._nome} não está logado.")



# if __name__ == "__main__":
#     # Criando um usuário
#     usuario1 = Usuario("Wanderson", "wanderson@gmail.com", "12345", "2999650274")

#     # Tentando logar
#     usuario1.logar()

#     # Tentando deslogar
#     usuario1.deslogar()
