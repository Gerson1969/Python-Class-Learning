# criar uma criptografia simples, somente deve ser substituido letras do alfabeto comum, respaitar maiuscula e minuscula e nao deve ser substituido caracteres especiais, numeros e espacos, e acentuações, deve ser solicitado um número que será a quandidede de caracteres deslocados da letra dentro do alfabeto
# e deve ser solicitado uma frase para ser criptografada, a saida deve ser a frase criptografada
def criptografar(frase, deslocamento):
    resultado = ""
    for char in frase:
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):  # Verifica se é uma letra do alfabeto comum
            deslocamento_mod = deslocamento % 26  # Garante que o deslocamento seja dentro do alfabeto
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')
            # Aplica o deslocamento e mantém a letra dentro do alfabeto respeitando maiúsculas e minúsculas
            resultado += chr((ord(char) - base + deslocamento_mod) % 26 + base)
        else:
            resultado += char  # Caracteres especiais, números, espaços e acentuações permanecem inalterados
    return resultado

# Solicita o número de deslocamento e a frase a ser criptografada
print("Bem-vindo à criptografia simples!")
deslocamento = int(input("Digite o número de deslocamento: "))
frase = input("Digite a frase a ser criptografada: ")
# Chama a função de criptografia e exibe o resultado
frase_criptografada = criptografar(frase, deslocamento)
print("Frase criptografada:", frase_criptografada)

#fim do código
