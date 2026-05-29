from notificador import NotificadorEmail, NotificadorSMS, NotificadorApp, CentralNotificacoes

if __name__ == "__main__":
    central = CentralNotificacoes()

    central.adicionar_notificador(NotificadorEmail())
    central.adicionar_notificador(NotificadorSMS())
    central.adicionar_notificador(NotificadorApp())

    central.enviar_para_todos("Atenção alunos: O prazo final da Lista II é 25 de maio de 2026!")