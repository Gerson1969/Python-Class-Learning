import config

from langchain_openai import OpenAI

llm  = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0.9)

#pergunta = 'Conte uma história breve sobre a jornada de aprender a programar'

#no formato tradicional, a resposta é gerada completamente antes de ser exibida
#resposta = llm.invoke(pergunta)
#print(resposta)

#no formato stream, a resposta é gerada em partes, e cada parte é exibida à medida que é recebida
#for trecho in llm.stream(pergunta):
#    print(trecho, end='', flush=True)

#agora com varias perguntas
perguntas = [
    'Conte uma história breve sobre a jornada de aprender a programar',
    'Quais são as melhores práticas para aprender a programar?',
    'Quais são os erros comuns que os iniciantes cometem ao aprender a programar?'
]

respostas = llm.batch(perguntas)
for resposta in respostas:
    print(resposta) 


