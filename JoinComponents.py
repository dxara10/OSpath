import os

class JuntarCaminhos:
    def __init__(self, *componentes):
        self.componentes = componentes

    def juntar(self):
        return os.path.join(*self.componentes)

caminho1 = "/path/to"
caminho2 = "file.txt"
juntador = JuntarCaminhos(caminho1, caminho2)
print("Caminho completo:", juntador.juntar())
