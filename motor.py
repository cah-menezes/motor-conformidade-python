from controles import criar_controle
from notificadores import LogNotificador, TerminalNotificador

class Motor:
    def __init__(self):
        self.observadores = []

    def inscrever(self, observador):
        self.observadores.append(observador)

    def notificar(self, controle):
        for observador in self.observadores:
            observador.atualizar(controle)

if __name__ == "__main__":
    motor = Motor()
    motor.inscrever(LogNotificador())
    motor.inscrever(TerminalNotificador())
    controle = criar_controle("ISO27001")
    controle.verificar()
    motor.notificar(controle)
    controle = criar_controle("NIST")
    controle.verificar()
    motor.notificar(controle)
    controle = criar_controle("CIS")
    controle.verificar()
    motor.notificar(controle)

