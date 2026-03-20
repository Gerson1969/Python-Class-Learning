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

#como configuro para fazer o push no github usando o terminal do vscode, e quais comandos devo usar para isso, considerando que já tenho um repositório criado no github e o projeto já está inicializado como um repositório git localmente?
Para fazer o push do seu projeto para o GitHub usando o terminal do VSCode, siga os passos abaixo:
1. Abra o terminal no VSCode (você pode usar o atalho Ctrl + `).
2. Navegue até o diretório do seu projeto usando o comando `cd` (exemplo: `cd caminho/para/seu/projeto`).
3. Configure o repositório remoto do GitHub usando o comando:   `git remote add origin https://github.com/seu_usuario/seu_repositorio.git`
4. Faça o commit das suas alterações:   `git commit -m "Mensagem do commit"`
5. Envie as alterações para o GitHub:   `git push -u origin main`   
    (Substitua "main" pelo nome da sua branch, se for diferente).   
6. Se solicitado, insira suas credenciais do GitHub para autenticação.
Após seguir esses passos, suas alterações serão enviadas para o repositório do GitHub.  

#como faco a autenticacao usando o token de acesso pessoal do github para fazer o push usando o terminal do vscode?Para autenticar usando um token de acesso pessoal do GitHub ao fazer push usando o terminal do VSCode, siga os passos abaixo:
1. Gere um token de acesso pessoal no GitHub:
    - Vá para as configurações da sua conta no GitHub.
    - Clique em "Developer settings" (Configurações de desenvolvedor).
    - Selecione "Personal access tokens" (Tokens de acesso pessoal).
    - Clique em "Generate new token" (Gerar novo token).
    - Dê um nome ao token, selecione as permissões necessárias (geralmente "repo" para acesso a repositórios) e clique em "Generate token".
    - Copie o token gerado, pois você não poderá vê-lo novamente.