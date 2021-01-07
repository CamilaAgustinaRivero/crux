from chatterbot.logic import LogicAdapter

class MyLogicAdapter(LogicAdapter):
    def __init__(self, chatbot, **kwargs):
        ().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        """
        PRE: Determina si es posible encontrar una respuesta para el statement entregado.
        POST: Si retorna True, se ejecuta process. Si retorna False, no se ejecuta nada.
        """
        words = ['mostrar', 'posteos', 'facebook']
        if all(word in statement.text.split() for word in words):
            return True
        else:
            return False

    def process(self, input_statement, additional_response_selection_parameters):
        """
        PRE: Crea la respuesta segun el statement entregado.
        POST: Retorna el statement de respuesta.
        """
        from chatterbot.conversation import Statement
        response_statement = Statement(text="Mostrar posteos de facebook")
        print("Ejecuto una funcioncita")
        return response_statement