
import random
print(  '\033[32m' '=' * 15,'Jogo do milhão', '=' * 15, '\033[0m')
# Lista de perguntas, organizadas por níveis de dificuldade
perguntas = {
    'fácil': [
        { 'pergunta': 'Quem pintou o quadro da Monalisa?',
          'alternativas': ['Vicente Van Gogh', 'Pablo Picasso', 'Leonardo da Vinci', 'Claude Monet'],
          'correta': 2,
        },
        { 'pergunta': 'Qual a capital da França?',
          'alternativas': ['Lisboa', 'Paris', 'Berlim', 'Londres'],
          'correta': 1,
        },
        { 'pergunta': 'Qual o continente onde fica o Egito?',
          'alternativas': ['América', 'África', 'Ásia', 'Europa'],
          'correta': 1,
        },
        { 'pergunta': 'Quantos meses tem um ano?',
          'alternativas': ['10', '12', '11', '13'],
          'correta': 1,
        },
        { 'pergunta': 'Qual o símbolo químico do oxigênio?',
          'alternativas': ['O', 'O2', 'Ox', 'O3'],
          'correta': 0,
        },
        { 'pergunta': 'Qual o maior mamífero do mundo?',
          'alternativas' : ['Elefante', 'Baleia Azul', 'Hipopótamo', 'Girafa'],
          'correta' : 1
        },
        { 'pergunta': 'Quantos dias tem um ano bissexto?',
          'alternativas' : ['365', '366', '364', '360'],
          'correta' : 1
        },
        { 'pergunta': 'Qual o menor país do mundo?',
          'alternativas' : ['Mônaco', 'San Marino', 'Vaticano', 'Malta'],
          'correta' : 2
        },
        { 'pergunta': 'Qual desses é um fruto?',
          'alternativas' : ['Batata', 'Cenoura', 'Tomate', 'Cebola'],
          'correta' : 2
        },
        { 'pergunta': 'Qual desses animais é um réptil',
          'alternativas' : ['Tubarão', 'Jacaré', 'Golfinho', 'Pinguim'],
          'correta' : 1
        }
    ],
    'médio': [
        {'pergunta': 'Quantos estados tem o Brasil?',
         'alternativas': ['25', '27', '26', '28'],
         'correta': 2},
        {'pergunta': 'Qual o maior país do mundo?',
         'alternativas': ['Estados Unidos', 'Canadá', 'China', 'Rússia'],
         'correta': 3},
        {'pergunta': 'Quem é o autor de "O Pequeno Príncipe"?',
         'alternativas': ['Antoine de Saint-Exupéry', 'Jules Verne', 'Victor Hugo', 'Marcel Proust'],
         'correta': 0},
        {'pergunta': 'Qual o idioma mais falado do mundo?',
         'alternativas': ['Inglês', 'Mandarim', 'Espanhol', 'Árabe'], 
         'correta': 1},
        {'pergunta': 'Qual a capital do Japão?',
         'alternativas': ['Pequim', 'Seul', 'Tóquio', 'Bangkok'],
         'correta': 2},
         {'pergunta': 'Em qual país fica a torre de Pisa?',
         'alternativas': ['França', 'Itália', 'Espanha', 'Grécia'],
         'correta': 1},
         {'pergunta': 'Quem esvreveu "Hamlet"?',
         'alternativas': ['William Shakespeare', 'Charles Dickens', 'J.K. Rowling', 'George Orwell'],
         'correta': 0},
         {'pergunta': 'Quantos ossos tem o corpo humano adulto?',
         'alternativas': ['206', '208', '210', '212'],
         'correta': 0},
         {'pergunta': 'Qual desses continentes é maior de área?',
         'alternativas': ['África', 'América do Norte', 'Ásia', 'Europa'],
         'correta': 2},
         {'pergunta': 'Em que ano ocorreu a Revolução Francesa?',
         'alternativas': ['1789', '1799', '1776', '1815'],
         'correta': 0}
    ],
    'difícil': [
        {'pergunta': 'Quem descobriu a América?',
         'alternativas': ['Pedro Álvares Cabral', 'Cristóvão Colombo', 'Zumbi dos Palmares', 'Simón Bolivar'],
         'correta': 1},
        {'pergunta': 'Qual o maior planeta do sistema solar?',
         'alternativas': ['Júpiter', 'Saturno', 'Vênus', 'Marte'],
         'correta': 0},
        {'pergunta': 'Quem escreveu "Cem Anos de Solidão"?',
         'alternativas': ['Gabriel García Márquez', 'Mario Vargas Llosa', 'Jorge Luis Borges', 'Julio Cortázar'],
         'correta': 0},
        {'pergunta': 'Qual a capital da Nova Zelândia?',
         'alternativas': ['Auckland', 'Wellington', 'Christchurch', 'Hamilton'],
         'correta': 1},
        {'pergunta': 'Em que ano o homem pisou na Lua pela primeira vez?',
         'alternativas': ['1965', '1969', '1971', '1975'],
         'correta': 1},
         {'pergunta': 'Qual foi o primeiro presidente dos Estados Unidos?',
         'alternativas': ['George Washington', 'Abraham Lincoln', 'Thomas Jefferson', 'John Adams'],
         'correta': 0},
         {'pergunta': 'Qual a camada externa da Terra?',
         'alternativas': ['Núcleo', 'Manto', 'Crosta', 'Astenosfera'],
         'correta': 2},
        {'pergunta': 'Em que ano começou a Segunda Guerra Mundial?',
         'alternativas': ['1935', '1939', '1941', '1945'],
         'correta': 1},
        {'pergunta': 'Quem é o autor da teoria da relatividade?',
         'alternativas': ['Isaac Newton', 'Nikola Tesla', 'Albert Einstein', 'Stephen Hawking'],
         'correta': 2},
        {'pergunta': 'Qual a cidade mais populosa do mundo? ',
         'alternativas': ['Tóquio', 'Nova York', 'São Paulo', 'Xangai'],
         'correta': 0},
    ]
}

# Função para exibir uma pergunta
def exibir_pergunta(perguntas):
    '''Função para exibir a pergunta
    

    Faz uma busca no dicionário maior de perguntas
    procura pela chave 'pergunta' e a exibe, após exibir
    a pergunta é feito um for com enumerate para assim 
    pegar o índice e logo após as respectivas alternativas,
    feito isso, as alternativas serão exibidas

    Parâmetro :
        - perguntas(dict) : É o dicionário listas de perguntas organizadas por dificuldades.
 
    '''


    print(f"\nPergunta: {perguntas['pergunta']}")
    for i, alternativa in enumerate(perguntas["alternativas"]):
        print(f'{i + 1}. {alternativa}')

# Função para responder a uma pergunta
def responder_pergunta(perguntas, resposta, jogador_atual, premios, indice_pergunta, jogadores):
    '''Verifica a resposta do jogador e ajeita o prêmio acumulado

    A função compara a resposta fornecida pelo jogador com a resposta correta. Se a resposta estiver correta,
    o jogador ganha o valor correspondente ao prêmio da pergunta atual e esse valor é registrado no dicionário
    de jogadores. Se a resposta estiver errada, o jogador perde 90% do valor acumulado, ficando com 10% do total.

    Parâmetros:
    - perguntas (dict): O dicionário que contém as perguntas e a resposta correta.
    - resposta (int): O número da alternativa escolhida pelo jogador.
    - jogador_atual (str): O nome do jogador atual que está respondendo à pergunta.
    - premios (list): Uma lista contendo os valores dos prêmios para cada pergunta.
    - indice_pergunta (int): O índice da pergunta atual, utilizado para buscar o prêmio correto na lista.
    - jogadores (dict): Um dicionário que armazena os prêmios acumulados de cada jogador.

    Retorna:
    - bool: Retorna True se a resposta estiver correta, ou False se estiver incorreta.
    '''
    
    correta = perguntas['correta']
    premio_acumulado = 0

    if resposta == correta + 1:
        premio_acumulado = premios[indice_pergunta]
        jogadores[jogador_atual] = premio_acumulado
        print(f"Resposta correta!! Você ganhou  \033[32mR${premio_acumulado:.2f}\033[0m ")
        return True
    else:
        premio_perdido = jogadores[jogador_atual] * 0.1
        jogadores[jogador_atual] = premio_perdido
        print('Resposta errada!')
        print(f"Você perdeu, mas leva 10% do prêmio:   \033[32mR${premio_perdido:.2f}\033[0m")
        return False

def escolher_nivel(perguntas):
    '''Solicita ao usuário que escolha um nível de dificuldade e valida a entrada.

    A função apresenta ao usuário três opções de nível de dificuldade: 
    fácil, médio ou difícil. Ela verifica se a escolha do usuário é válida,
    ou seja, se o nível escolhido corresponde a uma das chaves disponíveis no dicionário de perguntas.
    Se o usuário digitar uma entrada inválida, ele será solicitado a tentar novamente.

    Parâmetros:
    - perguntas (dict): Um dicionário contendo listas de perguntas organizadas por nível de dificuldade ('fácil', 'médio', 'difícil').

    Retorna:
    - str: O nível de dificuldade escolhido ('fácil', 'médio' ou 'difícil').
    '''
    niveis = list(perguntas.keys())
    while True:
        nivel = input("Escolha o nível de dificuldade (fácil, médio, difícil): ").lower()
        if nivel in niveis:
            return nivel
        else:
            print("Nível inválido. Tente novamente.")

def realizar_rodada(turno, pergunta_atual, jogadores, ajuda, premios, indice_pergunta):
    '''Controla uma rodada do jogo de perguntas, oferecendo ao jogador diferentes opções de ação.

    O jogador atual tem a opção de responder à pergunta, pedir ajuda para eliminar alternativas,
    passar a vez ou sair do jogo com o prêmio acumulado. A função também exibe a pergunta e
    as alternativas de resposta.

    Parâmetros:
    - turno (str): Nome do jogador que está jogando no momento.
    - pergunta_atual (dict): Dicionário contendo a pergunta atual, alternativas e a resposta correta.
    - jogadores (dict): Dicionário que armazena os prêmios acumulados por cada jogador.
    - ajuda (dict): Dicionário que indica se o jogador já utilizou a ajuda para eliminar alternativas.
    - premios (list): Lista de prêmios disponíveis para cada pergunta respondida corretamente.
    - indice_pergunta (int): Índice da pergunta atual, usado para associar ao prêmio correspondente.

    Funcionalidade:
    - A função exibe a pergunta e as alternativas.
    - O jogador escolhe uma das opções:
        1. Responder à pergunta.
        2. Pedir ajuda para eliminar 2 alternativas.
        3. Passar a vez, o que alterna o turno para o próximo jogador.
        4. Sair do jogo e levar o prêmio acumulado.
    - Dependendo da escolha do jogador, a função chama outras funções para processar a resposta, aplicar a ajuda, 
      ou encerrar a rodada.

    Retorna:
    - bool: Retorna True se o jogador respondeu ou pediu ajuda, mantendo o turno. 
      Retorna False se o jogador passou a vez, indicando a necessidade de troca de turno.
    - None: Se o jogador optar por sair, retorna None para encerrar o jogo.
    '''
    exibir_pergunta(pergunta_atual)

    print(f"\n{turno}, escolha uma opção")
    print("1. Responder")
    print("2. Pedir ajuda (eliminar 2 alternativas)")
    print("3. Passar a vez")
    print("4. Sair e levar o prêmio acumulado")

    escolha = input('Escolha: ')
    
    if escolha == '1':
        return responder_opcao(turno, pergunta_atual, jogadores, premios, indice_pergunta)
    
    elif escolha == '2':
        if not ajuda[turno]:
            return usar_ajuda(turno, pergunta_atual, jogadores, ajuda, premios, indice_pergunta)
        else:
            print("Você já usou sua ajuda!")
            return True  # Continua o jogo sem mudar o turno
        
    elif escolha == '3':
        print(f"{turno} passou a vez.")
        return False  # Passa o turno, portanto retorna False para indicar mudança de turno
    
    elif escolha == '4':
        print(f'O jogador {turno} decidiu sair e acumulou R${jogadores[turno]:.2f}')
        return None  # Encerra o jogo

def responder_opcao(turno, pergunta_atual, jogadores, premios, indice_pergunta):
    '''Solicita ao jogador a resposta para a pergunta e verifica se está correta.

    A função exibe as alternativas para que o jogador atual forneça uma resposta. Em seguida, chama a função 
    `responder_pergunta` para validar a resposta e determinar se o jogador acertou ou errou. 

    Parâmetros:
    - turno (str): O nome do jogador que está respondendo à pergunta no momento.
    - pergunta_atual (dict): O dicionário que contém a pergunta e suas alternativas.
    - jogadores (dict): Um dicionário que armazena o prêmio acumulado de cada jogador.
    - premios (list): Uma lista contendo os valores dos prêmios para cada pergunta.
    - indice_pergunta (int): O índice da pergunta atual, utilizado para acessar o prêmio correto na lista de prêmios.

    Retorna:
    - bool: Retorna True se a resposta estiver correta, ou False se estiver incorreta.
    '''

    resposta = int(input('Digite o número da sua resposta: '))
    correta = responder_pergunta(pergunta_atual, resposta, turno, premios, indice_pergunta, jogadores)
    return correta

def usar_ajuda(turno, pergunta_atual, jogadores, ajuda, premios, indice_pergunta):
    '''Aplica a ajuda ao jogador, eliminando duas alternativas incorretas da pergunta atual.

    Esta função permite que o jogador utilize sua ajuda, que elimina duas das alternativas
    incorretas disponíveis na pergunta, facilitando a escolha da resposta correta. Após a eliminação,
    a pergunta é exibida novamente com as alternativas restantes, e o jogador tem a oportunidade
    de responder.

    Parâmetros:
    - turno (str): Nome do jogador que está utilizando a ajuda.
    - pergunta_atual (dict): Dicionário contendo a pergunta atual, alternativas e a resposta correta.
    - jogadores (dict): Dicionário que armazena os prêmios acumulados por cada jogador.
    - ajuda (dict): Dicionário que armazena se o jogador já utilizou a ajuda. Atualiza para True após o uso.
    - premios (list): Lista de prêmios disponíveis para cada pergunta respondida corretamente.
    - indice_pergunta (int): Índice da pergunta atual, usado para associar ao prêmio correspondente.

    Funcionalidade:
    - Elimina duas alternativas incorretas da pergunta.
    - Exibe a pergunta novamente com as alternativas restantes.
    - O jogador escolhe uma nova resposta após a eliminação.
    - Marca a ajuda como utilizada para o jogador atual, impedindo novo uso.

    Retorna:
    - bool: Retorna True se a resposta estiver correta e o jogador ganha o prêmio correspondente.
            Retorna False se a resposta estiver errada e o jogador perde uma parte do prêmio.
    '''
    print("Duas alternativas serão eliminadas.")
    alternativas_possiveis = [i for i in range(4) if i != pergunta_atual['correta']]
    eliminadas = random.sample(alternativas_possiveis, 2)
    for i in eliminadas:
        pergunta_atual['alternativas'][i] = "-----"
    
    exibir_pergunta(pergunta_atual)
    resposta = int(input("Digite o número da sua resposta: "))
    correta = responder_pergunta(pergunta_atual, resposta, turno, premios, indice_pergunta, jogadores)
    
    ajuda[turno] = True
    return correta

def alternar_turno(turno, jogador1, jogador2):
    '''Alterna o turno entre dois jogadores.

    A função recebe o jogador que está atualmente jogando e alterna para o outro jogador.

    Parâmetros:
    - turno (str): O nome do jogador que está no turno atual.
    - jogador1 (str): O nome do primeiro jogador.
    - jogador2 (str): O nome do segundo jogador.

    Retorna:
    - str: O nome do jogador que terá o próximo turno.
    '''
    return jogador1 if turno == jogador2 else jogador2

def exibir_resultado_final(jogador1, jogador2, jogadores):
    '''Exibe o resultado final do jogo, determinando o vencedor e mostrando os prêmios acumulados.

    Esta função compara os prêmios acumulados pelos dois jogadores e determina qual deles é o vencedor
    com base no valor total acumulado. Em seguida, exibe o vencedor e os valores finais acumulados
    por ambos os jogadores.

    Parâmetros:
    - jogador1 (str): Nome do primeiro jogador.
    - jogador2 (str): Nome do segundo jogador.
    - jogadores (dict): Dicionário contendo o total de prêmios acumulados por cada jogador.

    Funcionalidade:
    - Determina o jogador vencedor com base no maior valor acumulado.
    - Exibe o nome do vencedor e o valor acumulado.
    - Exibe os resultados finais de ambos os jogadores, com os valores formatados em reais (R$).'''
    vencedor = jogador1 if jogadores[jogador1] > jogadores[jogador2] else jogador2
    print(f'O vencedor é: {vencedor} com R$\033[32m{jogadores[vencedor]:.2f}\033[0m')

    print("Resultados finais:")
    print(f"{jogador1}: \033[32mR${jogadores[jogador1]:.2f}\033[0m")
    print(f"{jogador2}: \033R${jogadores[jogador2]:.2f}\033[0m")

def jogo_do_milhao(jogador1, jogador2, perguntas, premios):
    '''Controla o fluxo do jogo de perguntas e respostas, onde dois jogadores competem por prêmios em dinheiro.

    O jogo funciona em rodadas alternadas entre dois jogadores, que respondem perguntas de múltipla escolha. 
    Cada jogador acumula prêmios ao acertar as respostas. O jogador pode passar a vez, continuar jogando, ou 
    decidir sair e levar o prêmio acumulado. O turno só alterna quando o jogador decide passar a vez.

    Parâmetros:
    - jogador1 (str): Nome do primeiro jogador.
    - jogador2 (str): Nome do segundo jogador.
    - perguntas (dict): Dicionário contendo as perguntas, alternativas e respostas corretas, organizadas por nível de dificuldade.
    - premios (list): Lista de prêmios acumulativos para cada pergunta acertada.

    Funcionalidade:
    - A função primeiro solicita que o jogador escolha o nível de dificuldade.
    - Perguntas são selecionadas de acordo com o nível escolhido.
    - Cada rodada, o jogador atual responde à pergunta ou escolhe uma das opções (responder, pedir ajuda, passar ou sair).
    - Se o jogador passar a vez, o turno é alternado.
    - Se o jogador sair, o jogo termina.
    - Ao final, a função exibe os resultados com o jogador vencedor e os prêmios acumulados por cada jogador.

    Retorna:
    - None: A função não retorna nenhum valor, apenas exibe os resultados do jogo.
    '''
    
    jogadores = {jogador1: 0, jogador2: 0}
    ajuda = {jogador1: False, jogador2: False}
    turno = jogador1
    
    nivel = escolher_nivel(perguntas)
    perguntas_selecionadas = perguntas[nivel]
    
    for indice_pergunta, pergunta_atual in enumerate(perguntas_selecionadas):
        resultado_rodada = realizar_rodada(turno, pergunta_atual, jogadores, ajuda, premios, indice_pergunta)
        
        if resultado_rodada is None:
            break  # Encerra o jogo se o jogador sair
        elif not resultado_rodada:
            turno = alternar_turno(turno, jogador1, jogador2)  # Só altera o turno se passar a vez

    exibir_resultado_final(jogador1, jogador2, jogadores)

# Lista de prêmios
premios = [1000, 5000, 50000, 100000,150000, 350000, 450000, 500000, 750000, 1000000]

if __name__ == '__main__':
    jogador1 = input('Digite o nome do participante 1: ')
    jogador2 = input('Digite o nome do participante 2: ')
    jogo_do_milhao(jogador1, jogador2, perguntas, premios)


