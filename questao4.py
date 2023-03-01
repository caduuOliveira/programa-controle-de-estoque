listaDePecas = [] #lista que vai armazenar um dicionario com as informacoes da peca

def cadastrarPecas(codigo):# funcao que cadastra pecas
    print('Você selecionou a opção de cadastrar peça')
    print(f'Código da peça 00{codigo}')
    nome = input('Digite o nome da peça! ')
    fabricante = input('Digite o nome do fabricante! ')
    try:
        valor = int(input('Digite o valor da peça!'))
    except ValueError:
        print('Por favor digite um valor valido')
# dicionario criado para armazenar informacoes das pecas
    dicionarioDePecas = {'codigo': codigo,
                           'nome': nome,
                           'fabricante': fabricante,
                           'valor': valor}
    listaDePecas.append(dicionarioDePecas.copy())# copia do dicionario de pecas passada para a lista de pecas


def consultarPecas():# funcao que consulta pecas
    while True:
        try:#menu de consulta de pecas
            print('Você selecionou a opção de Consultar peças')
            opConsultar = int(input('digite a opcao desejada: '
                                    '\n1 - Consultar Todas as peças'
                                    '\n2 - Consultar peças por código '
                                    '\n3 - consultar peças por Fabricante'
                                    '\n4 - retorna'
                                    '\n>>'))
            if (opConsultar == 1):
                print('-' * 15 )
                for pecas in listaDePecas:  # seleciono cada dicionario da minha lista
                    for key, value in pecas.items():  # selecionando cada chave / valor do dicionario
                        print(f'{key} : {value}')
            elif (opConsultar == 2):
                print('-' * 15)
                entrada = int(input('digite o Código da peça'))
                for pecas in listaDePecas:
                    if (pecas['codigo'] == entrada):
                        for key, value in pecas.items():
                            print(f'{key} : {value}')
            elif (opConsultar == 3):
                print('-' * 15)
                entrada = input('digite o Nome do fabricante')
                for pecas in listaDePecas:
                    if (pecas['fabricante'] == entrada):
                        for key, value in pecas.items():
                            print(f'{key} : {value}')
            elif (opConsultar == 4):
                break
            else:
                print('digite uma opcao valida')
                continue
        except ValueError:
            print('pare de digitar valores nao inteiros')
            continue




def removerPecas():# funcao de remover pecas vai capturar o codigo da peca que sera removida
    print('Você selecionou a opcao de remover pecas ')
    entrada = int(input('digite o codigo da peça'))
    for pecas in listaDePecas:# laco de repeticao para buscar o codigo correspondente ao que o usuario digitou
        if (pecas['codigo'] == entrada):
            listaDePecas.remove(pecas)
    for pecas in listaDePecas:# laco de repeticao para mostrar as informacoes das pecas que sobraram
        for key, value in pecas.items():
            print(f'{key} : {value}')






print('Bem vindo ao programa de controle de estoque da Bicicletaria do Carlos Eduardo Silva De Oliveira')
registroDePecas = 0
while True:
  try:
    opcao = int(input('digite a opcao desejada: '
                      '\n1 - Cadastrar peças'
                      '\n2 - Consultar peças '
                      '\n3 - Remover peças'
                      '\n4 - Sair'
                      '\n>>'))
    if(opcao == 1):
        registroDePecas += 1
        cadastrarPecas(registroDePecas)
    elif(opcao == 2):
        consultarPecas()
    elif(opcao == 3):
        removerPecas()
    elif(opcao == 4):
        print('programa finalizado')
        break
    else:
        print('pare de digitar numeros que nao existem')
        continue
  except ValueError:
      print('Digite uma das opcoes! ')
      continue
