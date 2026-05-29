from abc import ABC, abstractmethod
from typing import Protocol

class Armazenador(ABC):
    @abstractmethod
    def salvar(self, dado: str) -> None:
        pass

class ArmazenadorArquivo(Armazenador):
    def salvar(self, dado: str) -> None:
        print(f"💾 Salvando '{dado}' em Arquivo Local TXT.")

class ArmazenadorBanco(Armazenador):
    def salvar(self, dado: str) -> None:
        print(f"🗄️ Inserindo '{dado}' no Banco de Dados SQL.")

class Salvavel(Protocol):
    def salvar(self, dado: str) -> None:
        ...

class ArmazenadorNuvem:
    def salvar(self, dado: str) -> None:
        print(f"☁️ Sincronizando '{dado}' com a Nuvem AWS.")

def ejecutar_salvamento_formal(armazenador: Armazenador, dado: str):
    armazenador.salvar(dado)

def ejecutar_salvamento_flexivel(objeto: Salvavel, dado: str):
    objeto.salvar(dado)