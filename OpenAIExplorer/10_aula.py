import json
import yfinance as yf
import os
import pandas as pd
import time

OPENAI_API_KEY = os.getenv("MYOPENAI_API_KEY")

import openai
client = openai.Client(api_key=OPENAI_API_KEY)

def montar_simbolo_yahoo(ticker: str, mercado: str = "BR") -> str:
    t = ticker.strip().upper()

    # Se já veio completo (ex: PETR4.SA, TSLA, TSLA34.SA), respeita
    if "." in t:
        return t

    # Mercado brasileiro: adiciona .SA
    if mercado.upper() == "BR":
        return f"{t}.SA"

    # Mercado americano: usa sem sufixo
    return t


def retorna_cotacao_acao_historica(
    ticker: str,
    periodo: str = "1mo",
    mercado: str = "BR",
    max_pontos: int = 30,
    tentativas: int = 3
):
    simbolo = montar_simbolo_yahoo(ticker, mercado)
    ultimo_erro = None

    for tentativa in range(1, tentativas + 1):
        try:
            ticker_obj = yf.Ticker(simbolo)

            # Busca apenas histórico; evita depender de info para esse caso
            hist = ticker_obj.history(period=periodo)

            if hist.empty or "Close" not in hist.columns:
                return "{}"

            hist = hist["Close"].dropna()

            if hist.empty:
                return "{}"

            hist.index = pd.to_datetime(hist.index, errors="coerce")
            hist = hist[hist.index.notna()]

            if hist.empty:
                return "{}"

            hist = hist.round(2)

            # Mantém no máximo os últimos 30 pontos
            if len(hist) > max_pontos:
                hist = hist.tail(max_pontos)

            hist.index = hist.index.strftime("%Y-%m-%d")
            return hist.to_json()

        except Exception as e:
            ultimo_erro = e

            msg = str(e).lower()
            if "too many requests" in msg or "429" in msg:
                if tentativa < tentativas:
                    time.sleep(2 ** tentativa)   # 2s, 4s, 8s...
                    continue

            break

    raise Exception(
        f"Erro ao consultar {simbolo}. "
        f"Possível rate limit do Yahoo ou ticker inválido. Detalhe: {ultimo_erro}"
    )

tools = [
    {
        'type': 'function',
        'function': {
            'name': 'retorna_cotacao_acao_historica',
            'description': 'Retorna a cotação diária histórica para uma ação da bovespa',
            'parameters': {
                'type': 'object',
                'properties': {
                    'ticker': {
                        'type': 'string',
                        'description': 'O ticker da ação. Exemplo: "ABEV3" para ambev, "PETR4" para petrobras, etc'
                    },
                    'periodo': {
                        'type': 'string',
                        'description': 'O período que será retornado de dados históriocos \
                                        sendo "1mo" equivalente a um mês de dados, "1d" a \
                                        1 dia e "1y" a 1 ano',
                        'enum': ["1d","5d","1mo","6mo","1y","5y","10y","ytd","max"]
                    },
                    'mercado': {
                        'type': 'string',
                        'description': 'O mercado onde a ação está listada. Exemplo: "BR" para Brasil, "US" para Estados Unidos',
                        'enum': ["BR", "US"]
                    }
                }
            }
        }
    }
]

funcoes_disponiveis = {'retorna_cotacao_acao_historica': retorna_cotacao_acao_historica}


def gera_texto(mensagens):
    resposta = client.chat.completions.create(
        messages=mensagens,
        model='gpt-4o-mini',
        tools=tools,
        tool_choice='auto'
    )


    tool_calls = resposta.choices[0].message.tool_calls

    if tool_calls:
        mensagens.append(resposta.choices[0].message)
        for tool_call in tool_calls:
            func_name = tool_call.function.name
            function_to_call = funcoes_disponiveis[func_name]
            func_args = json.loads(tool_call.function.arguments)
            func_return = function_to_call(**func_args)
            mensagens.append({
                'tool_call_id': tool_call.id,
                'role': 'tool',
                'name': func_name,
                'content': func_return
            })
        segunda_resposta = client.chat.completions.create(
            messages=mensagens,
            model='gpt-4o-mini',
        )
        mensagens.append(segunda_resposta.choices[0].message)
    
    print(f'Assistant: {mensagens[-1].content}')

    return mensagens


if __name__ == '__main__':

    print('Bem-vindo ao ChatBot Financeiro da Asimov.')

    while True:
        input_usuario = input('User: ')
        mensagens = [{'role': 'user', 'content': input_usuario}]
        if input_usuario.lower() == 'sair':
            print('Encerrando a conversa. Até mais!')
            break
        mensagens = gera_texto(mensagens)

