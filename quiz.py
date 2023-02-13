# Exercício de perguntas e respostas
import os

# Função que exibe a questão escolhida pelo usuário, suas opções e verifica se a resposta é correta
def questionario(questao, lista_perguntas):
    # Verifica se a questão escolhida é a primeira
    if questao == 1:
        os.system('cls')  # Limpa a tela
        
        # Exibe a pergunta e as opções
        print(lista_perguntas[0]['Pergunta'])
        print(lista_perguntas[0]['Opções'])

        # Função que verifica se a resposta do usuário é correta
        def respostas(resposta_usuario):
            # Verifica se a resposta está na lista de respostas corretas
            if str(resposta_usuario) in lista_perguntas[0]['Resposta']:
                print('Acertou')
            else:
                print('Errou')
    
    # Verifica se a questão escolhida é a segunda
    if questao == 2:
        os.system('cls')  # Limpa a tela
        
        # Exibe a pergunta e as opções
        print(lista_perguntas[1]['Pergunta'])
        print(lista_perguntas[1]['Opções'])

        # Função que verifica se a resposta do usuário é correta
        def respostas(resposta_usuario):
            # Verifica se a resposta está na lista de respostas corretas
            if str(resposta_usuario) in lista_perguntas[1]['Resposta']:
                print('Acertou')
            else:
                print('Errou')
    
    # Verifica se a questão escolhida é a terceira
    if questao == 3:
        os.system('cls')  # Limpa a tela
        
        # Exibe a pergunta e as opções
        print(lista_perguntas[2]['Pergunta'])
        print(lista_perguntas[2]['Opções'])

        # Função que verifica se a resposta do usuário é correta
        def respostas(resposta_usuario):
            # Verifica se a resposta está na lista de respostas corretas
            if str(resposta_usuario) in lista_perguntas[2]['Resposta']:
                print('Acertou')
            else:
                print('Errou')
    
    # Retorna a função respostas
    return respostas