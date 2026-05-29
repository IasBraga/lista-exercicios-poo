from abc import ABC, abstractmethod

class Notificador(ABC):
    @abstractmethod
    def notificar(self, mensagem: str):
        pass

class NotificadorEmail(Notificador):
    def notificar(self, mensagem: str):
        print(f"📧 [E-mail Enviado]: {mensagem}")

class NotificadorSMS(Notificador):
    def notificar(self, mensagem: str):
        print(f"💬 [SMS Enviado]: {mensagem}")

class NotificadorApp(Notificador):
    def notificar(self, mensagem: str):
        print(f"📱 [Push Notification App]: {mensagem}")

class CentralNotificacoes:
    def __init__(self):
        self.notificadores = []

    def adicionar_notificador(self, notificador: Notificador):
        self.notificadores.append(notificador)

    def enviar_para_todos(self, mensagem: str):
        print(f"\n--- Disparando Notificações em Massa ---")
        for n in self.notificadores:
            n.notificar(mensagem)