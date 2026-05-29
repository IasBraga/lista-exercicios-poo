from midia import Video, Podcast, TextoNarrado, Plataforma

if __name__ == "__main__":
    plataforma = Plataforma("UFAM Play")

    v = Video("Aula de Programação Orientada a Objetos", 45, "1080p")
    p = Podcast("DevCast Especial Engenharia de Software", 60, "Prof. Alternei")
    t = TextoNarrado("Artigo sobre Encapsulamento", 15, "Português-BR")

    plataforma.adicionar_midia(v)
    plataforma.adicionar_midia(p)
    plataforma.adicionar_midia(t)

    plataforma.listar_midias()
    plataforma.reproduzir_todas()