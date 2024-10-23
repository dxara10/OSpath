import os

class ObterNomeArquivo:
    def __init__(self, caminho):
        self.caminho = caminho

    def obter_nome_arquivo(self):
        return os.path.basename(self.caminho)

caminho = "/path/to/file.txt"
obter_nome = ObterNomeArquivo(caminho)
print("Nome do arquivo:", obter_nome.obter_nome_arquivo())
