from impressao import Boleto, Etiqueta, RelatorioSimples, processar_impressao

if __name__ == "__main__":
    print("\n--- Sistema de Impressão (Protocol) ---")
    boleto = Boleto("34191.79001", 150.00)
    etiqueta = Etiqueta("Instituto ICET", "Estrada Odovaldo Novo, Parintins")
    relatorio = RelatorioSimples("Desempenho Acadêmico 2026.1")

    processar_impressao(boleto)
    processar_impressao(etiqueta)
    processar_impressao(relatorio)