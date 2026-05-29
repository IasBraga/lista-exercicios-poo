from armazenamento import (
    ArmazenadorArquivo, ArmazenadorBanco, ArmazenadorNuvem,
    ejecutar_salvamento_formal, ejecutar_salvamento_flexivel
)

if __name__ == "__main__":
    print("\n--- Testando Armazenamento ---")
    arq = ArmazenadorArquivo()
    banco = ArmazenadorBanco()
    nuvem = ArmazenadorNuvem()

    print("\n>> Execução Formal (Exige Herança da ABC):")
    ejecutar_salvamento_formal(arq, "Backup_1")
    ejecutar_salvamento_formal(banco, "Backup_2")

    print("\n>> Execução Flexível (Exige apenas compatibilidade estrutural):")
    ejecutar_salvamento_flexivel(arq, "Dados_A")
    ejecutar_salvamento_flexivel(banco, "Dados_B")
    ejecutar_salvamento_flexivel(nuvem, "Dados_C")