import os

class VerificadorArquivo:
    def __init__(self, caminho):
        self.caminho = caminho

    def verificar_arquivo(self):
        return os.path.isfile(self.caminho)

caminho = "/path/to/file.txt"
verificador = VerificadorArquivo(caminho)
print("O caminho", caminho, "é um arquivo?", verificador.verificar_arquivo())
