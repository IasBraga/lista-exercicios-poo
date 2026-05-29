from abc import ABC, abstractmethod

class Midia(ABC):
    def __init__(self, titulo: str, duracao: int):
        self.titulo = titulo
        self.duracao = duracao  # em minutos

    def mostrar_info(self):
        print(f"Mídia: {self.titulo} | Duração: {self.duracao} min")

    @abstractmethod
    def reproduzir(self):
        pass

class Video(Midia):
    def __init__(self, titulo: str, duracao: int, resolucao: str):
        super().__init__(titulo, duracao)
        self.resolucao = resolucao

    def reproduzir(self):
        print(f"🎬 Reproduzindo o vídeo '{self.titulo}' em {self.resolucao}...")

class Podcast(Midia):
    def __init__(self, titulo: str, duracao: int, apresentador: str):
        super().__init__(titulo, duracao)
        self.apresentador = apresentador

    def reproduzir(self):
        print(f"🎙️ Reproduzindo o podcast '{self.titulo}' comandado por {self.apresentador}...")

class TextoNarrado(Midia):
    def __init__(self, titulo: str, duracao: int, idioma: str):
        super().__init__(titulo, duracao)
        self.idioma = idioma

    def reproduzir(self):
        print(f"📖 Lendo o texto narrado '{self.titulo}' no idioma: {self.idioma}...")

class Plataforma:
    def __init__(self, nome: str):
        self.nome = nome
        self.midias = []

    def adicionar_midia(self, midia: Midia):
        self.midias.append(midia)

    def listar_midias(self):
        print(f"\n--- Mídias Disponíveis na {self.nome} ---")
        for m in self.midias:
            m.mostrar_info()

    def reproduzir_todas(self):
        print(f"\n--- Iniciando Reprodução na {self.nome} ---")
        for m in self.midias:
            m.reproduzir()