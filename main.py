from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


def get_conversation(chatbot):
    talk = True
    while talk:
        request = input('Usuario: ').lower()
        response = chatbot.get_response(request)
        print('Crux: ', response)
        if 'chau' in request:
            talk = False

def main():
    botname = 'Crux'
    chatbot = ChatBot(
        botname,
        logic_adapters = [
        {
            'import_path': 'adapters.MyLogicAdapter'},
        {
            'import_path':'chatterbot.logic.BestMatch',
            'default_response': 'No entiendo. ¿Podrías utilizar otras palabras?'
        }
        ])
    # Borra cualquier entrenamiento anterior
    chatbot.storage.drop()
    trainer = ListTrainer(chatbot)
    conversation = []
    file = None
    try:
        file = open('trainer.txt', encoding='utf-8')
        for line in file:
            conversation.append(line.strip('\n'))
    except IOError:
        print("Error de entrada/salida.")
    finally:
        if file and not file.closed:
            file.close()

    if conversation:
        trainer.train(conversation)
        get_conversation(chatbot)
    else:
        print("El asistente no esta entrenado.")

main()