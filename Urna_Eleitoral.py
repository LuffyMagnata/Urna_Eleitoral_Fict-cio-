"""
Projeto Urna Eletrônica
Versão 2024.11 Sistema Eleitoral
Data de Criação: 12/02/24
Data de atualização: 27/03/24
Candidatos fictícios
Testado: Sim (08/03/24)
"""
# Cadastro Antes de Votar
import os
prefeito = ''
presidente = ''

try:
    nome = str(input('Nome Completo: OBS: Escreva seu nome todo abaixo:\n'))
except ValueError:
    print('Erro na digitação, tente novamente!!')
    nome = str(input('Nome Completo: OBS: Escreva seu nome todo abaixo:\n'))
except TypeError:
    print('Erro na digitação, tente novamente!!')
    nome = str(input('Nome Completo: OBS: Escreva seu nome todo abaixo:\n'))
except NameError:
    print('Erro na digitação, tente novamente!!')
    nome = str(input('Nome Completo: OBS: Escreva seu nome todo abaixo:\n'))
except KeyError:
    print('Erro na digitação, tente novamente!!')
    nome = str(input('Nome Completo: OBS: Escreva seu nome todo abaixo:\n'))

os.system('cls')

try:
    cpf = int(input('Digite seu CPF:\n'))
except ValueError:
    print('Erro na digitação, tente novamente!!')
    cpf = int(input('Digite seu CPF:\n'))
except TypeError:
    print('Erro na digitação, tente novamente!!')
    cpf = int(input('Digite seu CPF:\n'))
except NameError:
    print('Erro na digitação, tente novamente!!')
    cpf = int(input('Digite seu CPF:\n'))
except KeyError:
    print('Erro na digitação, tente novamente!!')
    cpf = int(input('Digite seu CPF:\n'))

os.system('cls')

try:
    titulo = int(input('Digite código do título de eleitor: \n'))
except TypeError:
    print('Erro na digitação, tente novamente!!')
    titulo = int(input('Digite código do título de eleitor: \n'))
except ValueError:
    print('Erro na digitação, tente novamente!!')
    titulo = int(input('Digite código do título de eleitor: \n'))
except NameError:
    print('Erro na digitação, tente novamente!!')
    titulo = int(input('Digite código do título de eleitor: \n'))
except KeyError:
    print('Erro na digitação, tente novamente!!')
    titulo = int(input('Digite código do título de eleitor: \n'))

os.system('cls')

try:
    idade = int(input('Digite sua idade:\n'))
except TypeError:
    print('Erro na digitação, tente novamente!!')
    idade = int(input('Digite sua idade:\n'))
except ValueError:
    print('Erro na digitação, tente novamente!!')
    idade = int(input('Digite sua idade:\n'))
except NameError:
    print('Erro na digitação, tente novamente!!')
    idade = int(input('Digite sua idade:\n'))
except KeyError:
    print('Erro na digitação, tente novamente!!')
    idade = int(input('Digite sua idade:\n'))

os.system('cls')

if idade < 16:
    print('Menor de idade!!!\n')
    print('Não permitido, cadastro cancelado!!')
    exit()
elif idade == 16 or idade == 17:
    print('Olá Jovem, hoje será seu primeiro dia de voto ou segundo.\n')
    print('Começaremos seu voto, siga o passo a passo, aperte o enter para começar')
    os.system('cls')
elif idade == 18:
    print('Maior de idade!!, permitido\n')
    print('Começaremos seu voto, siga o passo a passo, aperte o enter para começar')
    os.system('cls')
else:
    print('Maior de idade!!!, Permitido\n')

print(f'Nome: {nome.title()}\nCPF: {cpf}\nTítulo de Eleitor: {titulo}\nIdade: {idade}')

# Confirmação de Dados pessoais
conf = input('Está correto seus dados?   Digite Sim ou Não abaixo:\n')
os.system('cls')
def canditado1():
    print('==================================================================================')
    print('Sugestão de Prefeitos abaixo:\n1111 = LULA MOLUSCO\n2222 = LOBÃO\n3333 = GANJA COLETIVA\n4444 = PANCADINHA')
    print('5555 = MARIO BROSS\n6666 = NARUTINHO\n7777 = MACARRÃO\n8888 = FERNANDA XERETA')
    print('==================================================================================')
    print('/////////PARA PREFEITO//////////\nDigite número do prefeito: ou Nulo = 1\n')

if conf == 'Não':
     print('VOTO REALOCADO, REINICIANDO VOTO, CHAME O RESPONSÁVEL DA URNA')
     exit()
elif conf == 'Sim':

    # Sistema de votação Prefeito
    print('Votação iniciada')
    os.system('cls')
    canditado1()
else:
    print('ERRO NA DIGITAÇÃO!!!\nREINICIANDO VOTO, CHAME O RESPONSÁVEL DA URNA')
    exit()
try:
    d1 = int(input(''))
except TypeError:
    print('Erro na digitação, tente novamente!!')
    canditado1()
    d1 = int(input(''))
except ValueError:
    print('Erro na digitação, tente novamente!!')
    canditado1()
    d1 = int(input(''))
except NameError:
    print('Erro na digitação, tente novamente!!')
    canditado1()
    d1 = int(input(''))
except KeyError:
    print('Erro na digitação, tente novamente!!')
    canditado1()
    d1 = int(input(''))

os.system('cls')

# Candidatos Prefeito
if d1 == 1111:
    print('///////LULA MOLUSCO///////\nPartido: Trabalhador Pobre\nIdade: 53 anos\nGênero: MOLUSCO')
    print('Sobre: luta pela causa dos pobres desempregados, dando dinheiro do povo para o povo.\n')
    prefeito = 'LULA MOLUSCO'
    print('É esse o candidato que deseja votar? Sim ou Não')

elif d1 == 2222:
    print('//////LOBÃO//////\nPartido: Movimento Democrático Brasileiro\nIdade: 45 anos\nGênero: MASCULINO')
    print('Sobre: Gosta de animais e selva, luta pela vida dos animais e gosta da chapeuzinho vermelho.\n')
    prefeito = 'LOBÃO'
    print('É esse o candidato que deseja votar? Sim ou Não')
elif d1 == 3333:
    print('//////GANJA COLETIVA//////\nPartido: Movimento Calvão de cria\nIdade: 38 anos\nGênero: MASCULINO')
    print('Sobre: Amador de Calvos,adora gente que ama a beleza masculina, tendo em vista ser macho alfa.\n')
    prefeito = 'GANJA COLETIVA'
    print('É esse o candidato que deseja votar? Sim ou Não')
elif d1 == 4444:
    print('//////PANCADINHA//////\nPartido: Solidariedade\nIdade: 34 anos\nGênero: MASCULINO')
    print('Sobre: Destinado pela burrice, mas ama o povo brasileiro, segue as leis da vida, sendo honesto(confia).\n')
    prefeito = 'PANCADINHA'
    print('É esse o candidato que deseja votar? Sim ou Não')
elif d1 == 5555:
    print('//////MARIO BROSS//////\nPartido: Games\nIdade 50 anos\nGênero: MASCULINO')
    print('Sobre: Amador de jogos, criador do lendário jogo do Mario,defendendo o investimentos em criadores de jogos.\n')
    prefeito = 'MARIO BROSS'
    print('\nÉ esse o candidato que deseja votar? Sim ou Não')
elif d1 == 6666:
    print('//////NARUTINHO//////\nPartido: KONOHA\nIdade 23 anos\nGênero: MASCULINO')
    print('Sobre: Candidato focado na determinação em proteger a população do mal, sendo o mais forte de todo estado.\n')
    prefeito = 'NARUTINHO'
    print('É esse o candidato que deseja votar? Sim ou Não')
elif d1 == 7777:
    print('//////MACARRÃO//////\nPartido: Comida\nIdade 42 anos\nGênero: OUTRO')
    print('Sobre: Senti amor por comida, sendo gordinho(a) delicia, quer que a população produza comidas diferentes\n')
    print('para atrair turistas para o Estado.\n')
    prefeito = 'MACARRÃO'
    print('É esse o candidato que deseja votar? Sim ou Não')
elif d1 == 8888:
    print('//////FERNANDA XERETA//////\nPartido: Fofoqueiras\nIdade 20 anos\nGênero: FEMININO')
    print('Sobre: Luta pelas mulheres contra homens machistas e defende total liberdade das mulheres brasileiras.')
    prefeito = 'FERNANDA XERETA'
    print('É essa a candidata que deseja votar? Sim ou Não')
elif d1 == 1:
    print('//////VOTO NULO//////\n')
    print('Sobre: esse voto será anulado, indo o voto pro vencedor da eleição\n')
    prefeito = 'VOTO NULO'
    print('Quer mesmo votar nulo? Sim ou Não')
else:
    print('ERRO NA DIGITAÇÃO!!!\nREINICIANDO VOTO, CHAME O RESPONSÁVEL DA URNA')
    exit()
conf2 = input('')
os.system('cls')
if conf2 == 'Sim':
    print('Voto Computado!!!')
    os.system('cls')
elif conf2 == 'Não':
    print('VOTO REALOCADO, REINICIANDO VOTO, CHAME O RESPONSÁVEL DA URNA')
    exit()
else:
    print('ERRO NA DIGITAÇÃO!!!\nREINICIANDO VOTO, CHAME O RESPONSÁVEL DA URNA')
    exit()
    # Fim votação Prefeito
    # Início votação Presidente
def candidato2():
    print('==================================================================================')
    print('Sugestões de Canditados a Presidente do Brasil abaixo:\n13 = BOLOLSONARO DA SILVA\n30 = DILMA ROUBOSSEFF')
    print('24 = AÉCIO NEVESCOVA\n17 = LULALÁBIO FALSANTE\n45 = MICHEL MOLEFF\n19 = CABO DARCIOLO\n26 = ITAMAR FRANQUINHO\n')
    print('==================================================================================')
candidato2()
try:
    p1 = int(input('/////////PARA PRESIDENTE//////////\nDigite número do presidente: ou Nulo = 1\n'))
except TypeError:
    print('Erro na digitação, tente novamente!!')
    candidato2()
    p1 = int(input('/////////PARA PRESIDENTE//////////\nDigite número do presidente: ou Nulo = 1\n'))
except ValueError:
    print('Erro na digitação, tente novamente!!')
    candidato2()
    p1 = int(input('/////////PARA PRESIDENTE//////////\nDigite número do presidente: ou Nulo = 1\n'))
except NameError:
    print('Erro na digitação, tente novamente!!')
    candidato2()
    p1 = int(input('/////////PARA PRESIDENTE//////////\nDigite número do presidente: ou Nulo = 1\n'))
except KeyError:
    print('Erro na digitação, tente novamente!!')
    candidato2()
    p1 = int(input('/////////PARA PRESIDENTE//////////\nDigite número do presidente: ou Nulo = 1\n'))

os.system('cls')
if p1 == 1:
    print('//////VOTO NULO//////\n')
    print('Sobre: esse voto será anulado, indo o voto pro vencedor da eleição\n')
    presidente = 'VOTO NULO'
    print('Quer mesmo votar nulo? Sim ou Não')
elif p1 == 13:
    print('//////BOLOLSONARO DA SILVA//////\nPartido: Rachadinha\nIdade 80 anos\nGênero: AFEMINADO')
    print('Sobre: o maior honesto do Brasil, tendo mansões compradas com dinheiro vivo,festejando com dinheiro vivo.\n')
    presidente = 'BOLOLSONARO DA SILVA'
    print('É esse o candidato que deseja votar? Sim ou Não')
elif p1 == 30:
    print('//////DILMA ROUBOSSEFF//////\nPartido: Plebiscito\nIdade 53 anos\nGênero: FEMININO')
    print('Sobre: Quer votações sem fraudes, a mulher mais honesta do mundo, e xamã vendo o futuro, medo\n')
    presidente = 'DILMA ROUBOSSEFF'
    print('É essa a candidata que deseja votar? Sim ou Não')
elif p1 == 24:
    print('//////AÉCIO NEVESCOVA//////\nPartido: Nevasca\nIdade 78 anos\nGênero: MASCULINO')
    print('Sobre: Amador de neves, querendo produzir neve no Brasil,roubando o máximo possível, a favor de bolinho.\n')
    presidente = 'AÉCIO NEVESCOVA'
    print('É esse o candidato que deseja votar? Sim ou Não')
elif p1 == 17:
    print('//////LULALÁBIO FALSANTE//////\nPartido: Comunista\nIdade 19 anos\nGênero: MASCULINO')
    print('Sobre: Quer implementar o comunismo no Brasil, "O que é meu é seu", um ser divino, honesto.\n')
    presidente = 'LULALÁBIO FALSANTE'
    print('É esse o candidato que deseja votar? Sim ou Não')
elif p1 == 2:
    print('EASTER EGG!!!!')
    print('//////LUCAS PROGRAMADOR//////\nPartido: Programadores\nIdade 21 anos\nGênero: MASCULINO')
    print('Sobre: Um sonhador que busca conhecimento na programação, com âmbito de crescer na área que ama.\n')
    presidente = 'LUCAS PROGRAMADOR'
    print('É esse o candidato que deseja votar? Sim ou Não')
elif p1 == 45:
    print('//////MICHEL MOLEFF//////\nPartido: Capitalistas\nIdade 39 anos\nGênero: MASCULINO')
    print('Sobre: Quer o fim da existencia do bolsão familiar do Brasil, "todos devem trabalhar", não honesto.\n')
    presidente = 'MICHEL MOLEFF'
    print('É esse o candidato que deseja votar? Sim ou Não')
elif p1 == 19:
    print('//////CABO DARCIOLO//////\nPartido: Gloria a Deus\nIdade 33 anos\nGênero: MASCULINO')
    print('Sobre: Ama Deus por votos, quer implementar igrejas no Brasil inteiro, Igreja Gloria a Deus.\n')
    presidente = 'CABO DARCIOLO'
    print('É esse o candidato que deseja votar? Sim ou Não')
elif p1 == 26:
    print('//////ITAMAR FRANQUINHO//////\nPartido: Real\nIdade 33 anos\nGênero: MASCULINO')
    print('Sobre: quer implementar o plano realidade, mundando a vida dos Brasileiros completamente, povo')
    print('deve ser ricos')
    presidente = 'ITAMAR FRANQUINHO'
    print('É esse o candidato que deseja votar? Sim ou Não')
else:
    print('ERRO NA DIGITAÇÃO!!!\nREINICIANDO VOTO, CHAME O RESPONSÁVEL DA URNA')
    exit()
conf3 = input('')
os.system('cls')
if conf3 == 'Sim':
    print('Voto Computado!!!')
    os.system('cls')
elif conf3 == 'Não':
     print('VOTO REALOCADO, REINICIANDO VOTO, CHAME O RESPONSÁVEL DA URNA')
     exit()
else:
    print('ERRO NA DIGITAÇÃO!!!\nREINICIANDO VOTO, CHAME O RESPONSÁVEL DA URNA')
    exit()
def acesso_restrito():
    print('VOTAÇÃO CONCLUÍDA !!')
    print('================================================================')
    print(f'Nome: {nome.title()}')
    print('CPF: restrito')
    print('T.Eleitor: restrito')
    print(f'Idade: {idade}')
    print('Prefeito: Secreto')
    print('Presidente: Secreto')
    print('================================================================')
acesso_restrito()
mesario = input('Deseja imprimir o voto? Sim ou Não, Acesso somente Mesario!!!\n')

if mesario == 'Não':
    print('VOTO CONCLUIDO COM SUCESSO!!')
    exit()
elif mesario == 'Sim':
    print('Digite a senha abaixo:')
else:
    print('ERRO 404!!! REINICIANDO')
    exit()
# Senha Obrigatoria!!!
password = "Sonho"
usuario = input()
while usuario != password:
    print('Senha incorreta, tente novamente!!')
    print('Digite a senha abaixo:')
    usuario = input()
def acesso_liberado():
    print('Acesso liberado!!!')
    print('VOTO CONCLUIDO, imprimindo resultado...\n')
    print('================================================================')
    print(f'Nome: {nome.title()}')
    print(f'CPF: {cpf}')
    print(f'Título de Eleitor: {titulo}')
    print(f'Idade: {idade}')
    print(f'Prefeito: {prefeito}')
    print(f'Presidente: {presidente}')
    print('================================================================')
acesso_liberado()

print('ESSA FOI URNA ELETRÔNICA PROJETADA, SOMENTE PARA DIVERSÃO, OBRIGADO POR TER TESTADO ELA')
print('by Lucas <3')
