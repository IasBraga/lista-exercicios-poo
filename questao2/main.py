from funcionario import FuncionarioAssalariado, FuncionarioHorista, FuncionarioComissionado, Empresa

if __name__ == "__main__":
    empresa = Empresa("Tech Solutions ICET")

    f1 = FuncionarioAssalariado("Ana Silva", "123.456.789-00", 5000.0)
    f2 = FuncionarioHorista("Carlos Souza", "987.654.321-11", 160, 25.0)
    f3 = FuncionarioComissionado("Beatriz Costa", "456.789.123-22", 50000.0, 0.05)

    empresa.adicionar_funcionario(f1)
    empresa.adicionar_funcionario(f2)
    empresa.adicionar_funcionario(f3)

    empresa.listar_funcionarios()
    empresa.mostrar_folha_pagamento()