class Usuario:
    def __init__(self, nome, email, codigo):
        self._nome = nome
        self._email = email
        self._codigo = codigo  # Pode ser CPF, CRM ou ID funcional, dependendo do tipo de usuário

    def logar(self):
        senha = input(f"Digite a senha: ")
        if senha == self._codigo:  # Usando o atributo privado
            self._autenticado = True
            print(f"{self.nome} logado com sucesso.")
        else:
            print("Senha incorreta. Tente novamente.")

    def deslogar(self):
        if self._autenticado:  # Verifica o estado protegido
            self._autenticado = False
            print(f"{self.nome} deslogado com sucesso.")
        else:
            print(f"{self.nome} não está logado.")



# # Criando um usuário
# usuario1 = Usuario("Wanderson", "12345")

# # Tentando logar
# usuario1.logar()

# # Tentando deslogar
# usuario1.deslogar()
