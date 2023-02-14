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

perguntas = [
    {
        'Pergunta' : 'Quanto é 2+2?',
        'Opções' : ['1','3','4','5','6'],
        'Resposta' : '4'
    },
    {
        'Pergunta' : 'Quanto é 5 * 5?',
        'Opções' : ['5','255','55','25','45'],
        'Resposta' : '25'
    },
    {
        'Pergunta' : 'Quanto é 10/2?',
        'Opções' : ['4','3','5','1','2'],
        'Resposta' : '5'
    },
]

numero_questao = 1
i=0
for pergunta in perguntas:
    
    print(f'{numero_questao}.Pergunta',perguntas[i]['Pergunta'])
    print('Opções:', perguntas[i]['Opções'])
    numero_questao += 1
    i += 1
    
questao = int(input('Digite qual das questões você quer responder: '))
seleciona_questao = questionario(questao, perguntas)
resposta_usuario = int(input('Resposta: '))

seleciona_questao(resposta_usuario)