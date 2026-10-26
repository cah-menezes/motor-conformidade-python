class Notificador: # Classe principal
    def atualizar(self, controle):
        pass

class LogNotificador(Notificador): # Classe derivada | LogNotificador herdando de Notificador

    def atualizar(self, controle):
        print(f"[LOG] Controle {controle.nome} registrado com status: {controle.status}")

class TerminalNotificador(Notificador): # Classe derivada | TerminalNotificador herdando de Notificador

    def atualizar(self, controle):
        print(f"[TERMINAL] Atenção: {controle.nome} — status: {controle.status}")