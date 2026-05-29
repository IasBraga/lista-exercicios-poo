from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome: str, cpf: str):
        self.nome = nome
        self.cpf = cpf

    def mostrar_dados(self):
        print(f"Funcionário: {self.nome} | CPF: {self.cpf}")

    @abstractmethod
    def calcular_pagamento(self) -> float:
        pass

class FuncionarioAssalariado(Funcionario):
    def __init__(self, nome: str, cpf: str, salario_mensal: float):
        super().__init__(nome, cpf)
        self.salario_mensal = salario_mensal

    def calcular_pagamento(self) -> float:
        return self.salario_mensal

class FuncionarioHorista(Funcionario):
    def __init__(self, nome: str, cpf: str, horas_trabalhadas: float, valor_hora: float):
        super().__init__(nome, cpf)
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    def calcular_pagamento(self) -> float:
        return self.horas_trabalhadas * self.valor_hora

class FuncionarioComissionado(Funcionario):
    def __init__(self, nome: str, cpf: str, total_vendas: float, percentual_comissao: float):
        super().__init__(nome, cpf)
        self.total_vendas = total_vendas
        self.percentual_comissao = percentual_comissao

    def calcular_pagamento(self) -> float:
        return self.total_vendas * self.percentual_comissao

class Empresa:
    def __init__(self, nome: str):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario: Funcionario):
        self.funcionarios.append(funcionario)

    def listar_funcionarios(self):
        print(f"\n--- Quadro de Funcionários: {self.nome} ---")
        for f in self.funcionarios:
            f.mostrar_dados()

    def mostrar_folha_pagamento(self):
        print(f"\n--- Folha de Pagamento: {self.nome} ---")
        total_folha = 0.0
        for f in self.funcionarios:
            pagamento = f.calcular_pagamento()
            total_folha += pagamento
            print(f"Nome: {f.nome} | Salário a receber: R$ {pagamento:.2f}")
        print(f"** Total Geral da Folha: R$ {total_folha:.2f} **")