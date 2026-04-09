import config

from langchain_openai import ChatOpenAI

chat = ChatOpenAI(model='gpt-3.5-turbo-0125')

from langchain_core.messages import HumanMessage, SystemMessage

mensagens = [
    SystemMessage(content='Você é um assistente que conta piadas.'),
    HumanMessage(content='Quanto é 1 + 1?')
]

#no formato tradicional, a resposta é gerada completamente antes de ser exibida
#resposta = chat.invoke(mensagens)
#print(resposta)

#no formato stream, a resposta é gerada em partes, e cada parte é exibida à medida que é recebida
for trecho in chat.stream(mensagens):
    print(trecho.content, end='')