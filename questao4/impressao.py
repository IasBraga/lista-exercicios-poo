from typing import Protocol

class Imprimivel(Protocol):
    def imprimir(self) -> None:
        ...

class Boleto:
    def __init__(self, codigo: str, valor: float):
        self.codigo = codigo
        self.valor = valor

    def imprimir(self) -> None:
        print(f"📄 [IMPRIMINDO BOLETO] Cód: {self.codigo} | Valor: R$ {self.valor:.2f}")

class Etiqueta:
    def __init__(self, destinatario: str, endereco: str):
        self.destinatario = destinatario
        self.endereco = endereco

    def imprimir(self) -> None:
        print(f"🏷️ [IMPRIMINDO ETIQUETA] Destino: {self.destinatario} | End: {self.endereco}")

class RelatorioSimples:
    def __init__(self, titulo: str):
        self.titulo = titulo

    def imprimir(self) -> None:
        print(f"📊 [IMPRIMINDO RELATÓRIO] Título: {self.titulo}")

def processar_impressao(item: Imprimivel):
    item.imprimir()