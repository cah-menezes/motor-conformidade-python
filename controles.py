"""Define a classe base Controle, as classes filhas ISO27001, NIST e CIS,
e a Factory que cria o controle certo a partir do nome do framework."""

class Controle: # Classe principal
    def __init__(self, nome):
        self.nome = nome
        self.status = "pendente"

    def verificar(self):
        pass

class ControleISO(Controle): #Classe derivada | ISO herdando de Controle
    def __init__ (self, nome):
        super().__init__(nome)

    def verificar(self):
        self.status = "aprovado"
        print(f"Verificando controle: {self.nome} | Status: {self.status}")

class ControleNIST(Controle): #Classe derivada | NIST herdando de Controle
    def __init__ (self, nome):
        super().__init__(nome)

    def verificar(self):
        self.status = "aprovado"
        print(f"Verificando controle: {self.nome} | Status: {self.status}")

class ControleCIS(Controle): #Classe derivada | CIS herdando de Controle
    def __init__ (self, nome):
        super().__init__(nome)

    def verificar(self):
        self.status = "aprovado"
        print(f"Verificando controle: {self.nome} | Status: {self.status}")

def criar_controle(tipo):
    if tipo == "ISO27001":
        return ControleISO("ISO27001")
    elif tipo == "NIST":
        return ControleNIST("NIST")
    elif tipo == "CIS":
        return ControleCIS("CIS")
