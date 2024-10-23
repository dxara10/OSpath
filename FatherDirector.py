import os

class ObterDiretorioPai:
    def __init__(self, caminho):
        self.caminho = caminho

    def obter_diretorio_pai(self):
        return os.path.dirname(self.caminho)

caminho = "/path/to/file.txt"
obter_diretorio = ObterDiretorioPai(caminho)
print("Diretório pai:", obter_diretorio.obter_diretorio_pai())
