import os

OPENAI_API_KEY = os.getenv("MYOPENAI_API_KEY")

import openai
client = openai.Client(api_key=OPENAI_API_KEY)

def geracao_texto(mensagens):
    resposta = client.chat.completions.create(
        messages=mensagens,
        model='gpt-3.5-turbo-0125',
        temperature=0,
        max_tokens=1000,
        stream=True,
    )

    print('Assistant: ', end='')
    texto_completo = ''
    for resposta_stream in resposta:
        texto = resposta_stream.choices[0].delta.content
        if texto:
            print(texto, end='')
            texto_completo += texto
    print()
    
    mensagens.append({'role': 'assistant', 'content': texto_completo})
    return mensagens

# Exemplo de uso - o uso do main indica onde comeca rodar. O código dentro do main é o que vai ser executado quando rodar o script.
if __name__ == '__main__':

    print('Bem-vindo ao chatBot com Python da Asimov :) (Digite "sair" para encerrar a conversa.)')
    mensagens = []
    while True:
        input_usuario = input('User: ')
        mensagens.append({'role': 'user', 'content': input_usuario})
        if input_usuario.lower() == 'sair':
            print('Encerrando a conversa. Até mais!')
            break
        mensagens = geracao_texto(mensagens)
        #para entendimento do código, o que acontece é o seguinte: 
        # o usuário digita uma mensagem, essa mensagem é adicionada à lista de mensagens, 
        # e então a função geracao_texto é chamada para gerar a resposta do assistente. 
        # A resposta é impressa em tempo real, e depois a resposta completa é adicionada à lista de mensagens 
        # para que o contexto da conversa seja mantido. O loop continua até que o usuário digite "sair". 
        # exemplo para entendimento --> print ('\n',mensagens,'\n')
