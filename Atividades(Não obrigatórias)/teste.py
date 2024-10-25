class Funcionarios:

    dados_de_cada_funcionario = {}

    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.adicionar_funcionario()

    def adicionar_funcionario(self):
        if self.cargo not in Funcionarios.dados_de_cada_funcionario:
            Funcionarios.dados_de_cada_funcionario[self.cargo] = []
        Funcionarios.dados_de_cada_funcionario[self.cargo].append(self)

    @classmethod
    def criar_por_cargo(cls, nome, cargo):
        salario_padrao = 3000  # Salário padrão para o cargo
        return cls(nome, cargo, salario_padrao)

    @classmethod
    def listar_funcionarios(cls):
        for cargo, funcionarios in cls.dados_de_cada_funcionario.items():
            print(f'\nCargo: {cargo}')
            for funcionario in funcionarios:
                print(
                    f"Funcionario: {funcionario.nome}\n"
                    f"Salario: {funcionario.salario}\n"
                    f"Salario anual: {funcionario.calculo_salario_anual}\n"
                )

    @property
    def calculo_salario_anual(self):
        """Calcula o salário anual do funcionário."""
        return self.salario * 12

# Criação de funcionários
Funcionarios.criar_por_cargo('Adamos', 'Porteiro')
Funcionarios.criar_por_cargo('Antonio', 'Vigilante')
Funcionarios.criar_por_cargo('Vilma', 'Porteiro')

# Listar funcionários
Funcionarios.listar_funcionarios()
