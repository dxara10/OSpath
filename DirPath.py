import os

class VerificadorDiretorio:
    def __init__(self, caminho):
        self.caminho = caminho

    def verificar_diretorio(self):
        return os.path.isdir(self.caminho)

caminho = "/path/to/directory"
verificador = VerificadorDiretorio(caminho)
print("O caminho", caminho, "é um diretório?", verificador.verificar_diretorio())
