################################################################################################################
################################################################################################################
#                                      Classes                                               
################################################################################################################
################################################################################################################

    # Classes
class Sala:
    codigo = -1
    nome = ""
    capacidade = -1
    tipo_de_exibição = ""
    acessivel = ""

class Filme:
    codigo = -1
    nome = ""
    ano_de_lancamento = -1
    diretor = ""
    atores = ""

class Sessao:
    codigo_do_filme = -1
    codigo_da_sala = -1
    data = ""
    horario = []
    preco_do_ingresso = -1

################################################################################################################
################################################################################################################
#                       Menu principal e menu de filme, de salas, de sessoes e de relatórios                                              
################################################################################################################
################################################################################################################


def menu():
    print("##########       ****    Cine  System   ****      #########")
    print("##########     ****     Menu Principal    ****    #########")
    print("escolha um dos sub-menus por meio dos números de cada opção")
    print("Informações sobre salas.................................. 1")
    print("Informações sobre filmes................................. 2")
    print("Informações sobre sessões................................ 3")
    print("Relatórios gerais........................................ 4")
    print("Sair..................................................... 0")
    opção = input("Qual sua opção?    ")
    return opção


# SUBMENU DE FILMES
    # Menu principal do submenu de filmes
def menu_filmes():
    print("##########   Cine  System  ##########")
    print("##########  Menu de Filmes ##########")
    print("Adicionar filme......................1")
    print("Listar filmes........................2")
    print("Listar um filme......................3")
    print("alterar ou Excluir...................4")
    print("Voltar ao menu principal.............0")
    opcao = input("-> ")
    return opcao

def menu_salas():
    print("##########   Cine  System  ##########")
    print("##########  Menu de Salas  ##########")
    print("Adicionar sala......................1")
    print("Listar todas as salas...............2")
    print("Listar uma sala.....................3")
    print("alterar ou Excluir..................4")
    print("Voltar ao menu principal............0")
    opcao = input("-> ")
    return opcao

def menu_sessoes():
    print("##########    Cine  System     ##########")
    print("##########   Menu de Sessoes   ##########")
    print("Adicionar sessão........................1")
    print("Listar todas as sessões.................2")
    print("Listar uma sessão.......................3")
    print("alterar ou Excluir......................4")
    print("Voltar ao menu principal................0")
    opcao = input("-> ")
    return opcao

def menu_relatorios():
    print("##########      Cine  System      ##########")
    print("##########   Menu de Realtórios   ##########")
    print("Relatório 1................................1")
    print("Relatório 2................................2")
    print("Relatório 3................................3")
    print("Voltar ao menu principal...................0")
    opcao = input("-> ")
    return opcao
################################################################################################################
################################################################################################################
#                                      Funções Salas                                         
################################################################################################################
################################################################################################################

    # Menu de escolha de opções de alteração e exclusão de salas
def verificar_posicao(lista,code):
    i = 0
    saida = -1
    while i < len(lista):
        if lista[i].codigo == code:
            saida = i
        i = i + 1
    return saida

def alterar_excluir_salas():
    print("##########          Cine  System         ##########")
    print("####    Menu alteração e exclusão de Salas    #####")
    print("Alterar...........................................1")
    print("Excluir...........................................2")
    print("Voltar ao menu principal..........................0")
    opcao2 = input("-> ")
    return opcao2

    # Menu com opções para alteração de características de salas
def menu_alterar_salas():
    print("##########          Cine  System         ##########")
    print("##########    Menu alteração de Salas    ##########")
    print("Alterar código....................................1")
    print("Alterar nome......................................2")
    print("Alterar capacidade................................3")
    print("Alterar tipo de exibição..........................4")
    print("Alterar acessibilidade............................5")
    print("Voltar ao menu principal..........................0")
    opcao3 = input("-> ")
    return opcao3

    # Função de alterações para salas listadas
def alterar_salas(lista_salas):
    code=input("Digite o código da sala:")
    i = verificar_posicao(lista_salas,code)
    if i != -1:
        op3= ''
        res = input("Deseja mesmo alterar esse cadastro? 1-(SIM) 0-(NÃO)")
        if res=="1":
            while op3 != '0':
                op3 = menu_alterar_salas()
                if op3 == '1':
                    continuar=True
                    while continuar==True:
                        code2=input("Digite o novo código: ")
                        v = verificar_posicao(lista_salas,code2)
                        if v!=-1:
                            print("O código digitado já está em uso! Tente novamente: ")
                        else:
                            lista_salas[i].codigo = code2
                            continuar=False
                            print("informação alterada com sucesso!")
                elif op3 == '2':
                    lista_salas[i].nome = input("Digite o novo nome: ")
                elif op3 == '3':
                    lista_salas[i].capacidade = int(input("Digite a capacidade da sala: "))
                elif op3 == '4':
                    lista_salas[i].tipo_de_exibição = input("Digite o tipo de exibição: ")
                elif op3 == '5':
                    lista_salas[i].acessivel = input("Digite a acessibilidade da sala: ")
                elif op3 == '0':
                    print("Retornando...")
                else:
                    print("Opção inválida!")
                print("Escolha outra opção para alterar ou digite 0 para sair")
        elif res=="0":
            print("Os dados continuam inalterados!")
        else:
            print("Opção inválida!")
    else:
        print("A sala não encontra-se no banco de dados!")

    # Função de exclusão:
def excluir_salas(lista):
    code=input("Digite o código da sala:")
    i = verificar_posicao(lista,code)
    if i != -1:
        res = input("Deseja mesmo excluir esse cadastro? 1-(SIM) 0-(NÃO): ")
        if res=="1":
            lista.pop(i)
            print("O cadastro foi excluido!")
        elif res=="0":
            print("O cadastro continua no banco de dados!")
        else:
            print("Opcão invalida.")
    else:
        print("O cadastro não encontra-se no banco de dados!")

    # Função para inserir novas salas a lista
def inserir_salas(lista):
    s = Sala()
    code=input("Digite o código da sala:")
    i=verificar_posicao(lista,code)
    if i!=-1:
        print("O código digitado já está em uso!")
        i=i+1
    else:
        s.codigo=code
        s.nome = input("Informe o nome da sala: ")
        s.capacidade = int(input("Informe a capacidade: "))
        s.tipo_de_exibição = input("Informe o tipo de exibição ('normal' ou '3D'): ")
        s.acessivel = input("Informe a acessibilidade ('sim' ou 'não'): ")
        lista.append(s)
        print("Informações da sala inseridas com sucesso!!!")

    # Função de impressão de salas
def imprimir_salas(lista):
    print(f"Sala codigo {str(lista.codigo)}")
    print(f"    nome: {lista.nome}")
    print(f"    capacidade: {str(lista.capacidade)}")
    print(f"    tipo_de_exibição: {lista.tipo_de_exibição}")
    print(f"    acessivel: {lista.acessivel}")
    print("#####################################################")

    # Função para listar todas as salas da lista
def apresentar_todas_salas(lista):
    if len(lista) > 0:
        i = 0
        while i < len(lista):
            imprimir_salas(lista[i])
            i = i + 1
    else:
        print("Não há informações cadastradas! Você precisa incluir um novo cadastro.")

    # Função para listar uma unica sala
def listar_uma_sala(lista):
    if len(lista) == 0:
        print("Não há cadastros! Você precisa incluir um novo cadastro no sistema para utilizar essa função.")
    else:
        continuar = True
        while continuar == True:
            code = input("Digite o código da sala: ")
            i=verificar_posicao(lista,code)
            continuar_2 = True
            while continuar_2 == True:
                if i!=-1:
                    imprimir_salas(lista[i])
                else:
                    print("Não há salas cadastradas com esse código!")
                continuar_3 = True
                while continuar_3 == True:
                    opção = input("Você ainda deseja listar uma sala? 1(sim) ou 0(não)")
                    if opção == '0':
                        continuar_3 = False
                        continuar_2 = False
                        continuar = False
                    elif opção == '1':
                        continuar_3 = False
                        continuar_2 = False
                    else:
                        print("Comando inválido! Escolha uma opção válida. ")

################################################################################################################
################################################################################################################
#                                      Funções Filmes                                                
################################################################################################################
################################################################################################################

    # Menu de escolha de opções de alteração e exclusão de filmes
def alterar_excluir_filmes():
    print("##########          Cine  System         ##########")
    print("##########    Menu exclusão de Filmes    ##########")
    print("Alterar...........................................1")
    print("Excluir...........................................2")
    print("Voltar ao menu principal..........................0")
    opcao2 = input("-> ")
    return opcao2

    # Menu com opções para alteração de características de filmes
def menu_alterar_filme():
    print("##########          Cine  System         ##########")
    print("##########    Menu alteração de Filmes   ##########")
    print("Alterar código....................................1")
    print("Alterar nome......................................2")
    print("Alterar ano de lançamento.........................3")
    print("Alterar diretor...................................4")
    print("Alterar Atores....................................5")
    print("Voltar ao menu principal..........................0")
    opcao3 = input("-> ")
    return opcao3

    # Função de alterações para filmes listados
def alterar_filmes(lista_filmes):
    code=input("Digite o código do filme:")
    i = verificar_posicao(lista_filmes,code)
    if i != -1:
        op3= ''
        res = input("Deseja mesmo alterar esse cadastro? 1-(SIM) 0-(NÃO)")
        if res=="1":
            while op3 != '0':
                op3 = menu_alterar_filme()
                if op3 == '1':
                    continuar=True
                    while continuar==True:
                        code2=input("Digite o novo código: ")
                        v = verificar_posicao(lista_filmes,code2)
                        if v!=-1:
                            print("O código digitado já está em uso! Tente novamente: ")
                        else:
                            lista_filmes[i].codigo = code2
                            continuar=False
                            print("informação alterada com sucesso!")
                elif op3 == '2':
                    lista_filmes[i].nome = input("Digite o novo nome: ")
                elif op3 == '3':
                    lista_filmes[i].ano_de_lancamento = int(input("Digite o novo ano de lançamento: "))
                elif op3 == '4':
                    lista_filmes[i].diretor = input("Digite o novo diretor: ")
                elif op3 == '5':
                    lista_atores = []
                    lista_filmes[i].atores = ""
                    ator=str(input("informe o nome de um ator/atriz: "))
                    lista_atores.append(ator)
                    sistema = True
                    while sistema == True:
                        ator=str(input("informe o nome de um novo ator/atriz ou precione (0 e enter) para finalizar: "))
                        if ator == "0":
                            sistema = False
                        else:
                            lista_atores.append(ator)
                            lista_filmes[i].atores = lista_atores
                elif op3 == '0':
                    print("Retornando...")
                else:
                    print("Opção inválida!")
                print("Escolha outra opção para alterar ou digite 0 para sair")
        elif res=="0":
            print("Os dados continuam inalterados!")
        else:
            print("Opção inválida!")
    else:
        print("O filme não encontra-se no banco de dados!")

    # Função de exclusão de filmes listados
def excluir_filmes(lista_filmes):
    code=input("Digite o código do filme:")
    i = verificar_posicao(lista_filmes,code)
    if i != -1:
        res = input("Deseja mesmo excluir esse cadastro? 1-(SIM) 0-(NÃO): ")
        if res=="1":
            lista_filmes.pop(i)
            print("O filme foi excluido!")
        elif res=="0":
            print("O filme continua cadastrado!")
        else:
            print("Opcão invalida.")
    else:
        print("O filme não encontra-se no banco de dados!")

    # Função para inserir novos filmes a lista
def inserir_filme(lista_filmes):
    f = Filme()
    lista_atores = []
    code=input("Digite o código do filme:")
    i=verificar_posicao(lista_filmes,code)
    if i!=-1:
        print("O código digitado já está em uso!")
        i=i+1
    else:
        f.codigo=code
        f.nome = input("Informe o nome do filme: ")
        f.ano_de_lancamento = int(input("Informe o ano de lançamento  : "))
        f.diretor = input("Informe o diretor: ")
        ator=input("informe o nome de um ator/atriz: ")
        lista_atores.append(ator)
        inserir_novos_atores = True
        while inserir_novos_atores:
            ator=input("informe o nome de um novo ator/atriz ou precione (0 e enter) para finalizar: ")
            if ator == "0":
                inserir_novos_atores = False
            else:
                lista_atores.append(ator)
        f.atores = lista_atores
        lista_filmes.append(f)
        print("Informações do filme inseridas com sucesso!!!")

    # Função de impressão de filmes 
def imprime_filme(f):
    print(f"Código:{f.codigo}")
    print(f"Nome do filme:{f.nome}")
    print(f"Ano de lançamento:{f.ano_de_lancamento}")
    print(f"Nome do diretor:{f.diretor}")
    print("Atores:  ", end = ' ')
    i = 0 
    while i < len(f.atores) - 1:
        print(f.atores[i], end = " | ")
        i = i + 1
    print(f.atores[i])
    print("-" * 30)

    # Função para listar todos os filmes da lista
def listar_filmes(lista_filmes):
    if len(lista_filmes) > 0:
        i = 0
        while i < len(lista_filmes):
            imprime_filme(lista_filmes[i])
            i = i + 1
    else:
        print("Não há filmes cadastrados! Você precisa incluir filmes no sistema.")

    # Função para listar um unico filme da lista
def listar_um_filme(lista_filmes):
    if len(lista_filmes) == 0:
        print("Não há filme cadastrados! Você precisa incluir filmes no sistema.")
    else:
        continuar = True
        while continuar == True:
            code = input("Digite o código do filme: ")
            i=verificar_posicao(lista_filmes,code)
            continuar_2 = True
            while continuar_2 == True:
                if i!=-1:
                    imprime_filme(lista_filmes[i])
                else:
                    print("Não há filmes cadastrados com esse código!")
                continuar_3 = True
                while continuar_3 == True:
                    opção = input("Você ainda deseja listar uma sala? 1(sim) ou 0(não)")
                    if opção == '0':
                        continuar_3 = False
                        continuar_2 = False
                        continuar = False
                    elif opção == '1':
                        continuar_3 = False
                        continuar_2 = False
                    else:
                        print("Comando inválido! Escolha uma opção válida. ")



################################################################################################################
################################################################################################################
#                                      Funções Sessões                                                
################################################################################################################
################################################################################################################

def verificar_posicao_sessao(lista,code_sala,data,horario):
    posicao =  -1
    horario_inicio = int(horario[:2]+horario[3:5])
    horario_fim = int(horario[6:8]+horario[9:])
    if len(lista) > 0:
        i=0
        while i < len(lista) and posicao == - 1:
            if lista[i].data == data and int(lista[i].horario[:2]+lista[i].horario[3:5]) == horario_inicio  and int(lista[i].horario[6:8]+lista[i].horario[9:]) == horario_fim and lista[i].codigo_da_sala == code_sala:
                posicao = i
            i=i+1
    return posicao

def verificar_interposicao_sessao(lista,data,horario,code_sala):
    achou =  False
    horario_inicio = int(horario[:2]+horario[3:5])
    horario_fim = int(horario[6:8]+horario[9:])
    
    if len(lista) > 0:
        i=0
        while i < len(lista) and not achou:
            if lista[i].data == data and lista[i].codigo_da_sala == code_sala and horario_inicio < int(lista[i].horario[6:8]+lista[i].horario[9:]) and horario_fim > int(lista[i].horario[6:8]+lista[i].horario[9:]):
                achou = True
            if lista[i].data == data and lista[i].codigo_da_sala == code_sala and horario_inicio < int(lista[i].horario[:2]+lista[i].horario[3:5]) and horario_fim > int(lista[i].horario[:2]+lista[i].horario[3:5]):
                achou = True
            i=i+1
    return achou

def apresentar_todas_sessoes(lista_sessoes):
    if len(lista_sessoes) > 0:
        i = 0
        while i < len(lista_sessoes):
            imprimir_sessao(lista_sessoes,i)
            i = i + 1
        print("Apressentação de sessões encerrada.")
    else:
        print("Não há sessões cadastradas. Você precisa cadastrar uma sessão.")


def listar_uma_sessao(lista_sessoes):
    if lista_sessoes == []:
        print("Não há sessões cadastradas. Cadastre uma sessão.")
    else:
        code_sala=input("Digite o código do sala da sessão:")
        data = input("Digite a data da sessão - nesse formato dd/mm/aaaa:  ")
        horario = input("Digite o horario de início e fim da sessão - nesse formato e sem parênteses (hh:mm/hh:mm):   ")
        posicao = verificar_posicao_sessao(lista_sessoes,code_sala,data,horario)
        if posicao != - 1:
            imprimir_sessao(lista_sessoes,posicao)
        print("Apressentação de sessão encerrada.")

def imprimir_sessao(lista_sessoes,posicao):
    l = lista_sessoes
    print("*******************************************************************************************************************")
    print(f"Sessão {posicao+1} - codigo do filme: {l[posicao].codigo_do_filme} | codigo da sala: {l[posicao].codigo_da_sala} | data: {l[posicao].data} | horário: {l[posicao].horario} | preço do ingresso: {l[posicao].preco_do_ingresso}")


    # Menu de escolha de opções de alteração e exclusão de sessões
def alterar_excluir_sessao():
    print("##########          Cine  System         ##########")
    print("##########   Menu exclusão de Sessões    ##########")
    print("Alterar...........................................1")
    print("Excluir...........................................2")
    print("Voltar ao menu de sessões..........................0")
    opcao2 = input("-> ")
    return opcao2


    # Menu com opções para alteração de características de salas
def menu_alterar_sessao():
    print("##########          Cine  System          ##########")
    print("##########    Menu alteração de sessão    ##########")
    print("Alterar data e horário.............................1")
    print("Alterar filme......................................2")
    print("Alterar sala.......................................3")
    print("Alterar preço do ingresso..........................4")
    print("Voltar ao menu de sessões...........................0")
    opcao3 = input("-> ")
    return opcao3


    # Função de alterações para salas listadas
def alterar_sessao(lista_sessoes,lista_filmes,lista_salas):
    if lista_sessoes == []:
        print("Não há sessões cadastradas. Você precisa cadastrar uma sessão.")
    else:
        code_sala=input("Digite o código do sala da sessão:")
        data = input("Digite a data da sessão - nesse formato dd/mm/aaaa:  ")
        horario = input("Digite o horario de início e fim da sessão - nesse formato (hh:mm/hh:mm):   ")
        posicao = verificar_posicao_sessao(lista_sessoes,code_sala,data,horario)
        if posicao != -1:
            op3= ''
            res = input("Deseja alterar essa sessão? 1-(SIM) 0-(NÃO): ")
            print("Lembre-se, nessa opção você não pode mudar código de filmes ou de salas específicas, mas apenas trocar qual filme ou sala de cada sessão. Para isso vá em seus respectivos menus.")
            if res=="1":
                while op3 != '0':
                    op3 = menu_alterar_sessao()
                    continuar=True
                    while continuar==True:
                        if op3 == '1':
                            data = input("Digite a nova data - nesse formato (dd/mm/aaaa): ")
                            horario = input("Digite o novo horario de início e de termino da sessão - nesse formato (hh:mm/hh:mm):   ")

                            interposicao = verificar_interposicao_sessao(lista_sessoes,data,horario,code_sala)
                            if interposicao == True:
                                print("Um ou os dois horário digitados estão dando problema com outras sessões!")
                                res = input("Você deseja tentar novamente? sim(1) ou não(0) -->")
                                if res == 1:
                                    print("Digite um código diferente.")
                                elif res ==0:
                                    continuar=False
                                else:
                                    print("Resposta invalida, você será direcionado para o menu.") 
                            else:
                                lista_sessoes[posicao].data = data
                                lista_sessoes[posicao].horario = horario
                                continuar=False
                                print("informação alterada com sucesso!")
                        elif op3 == '2':
                            code_filme = input("Digite o código do filme: ")
                            i = verificar_posicao(lista_filmes,code_filme)
                            if i == -1:
                                print("Não existe esse código de filme.")
                                res = input("Você deseja tentar novamente? sim(1) ou não(0) -->")
                                if res == 1:
                                    print("Digite um código diferente.")
                                elif res ==0:
                                    continuar=False
                                else:
                                    print("Resposta invalida, você será direcionado para o menu.") 
                            else:
                                lista_sessoes[posicao].codigo_do_filme = code_filme
                                continuar=False
                        elif op3 == '3':
                            code_sala = input("Digite o código da sala: ")
                            i = verificar_posicao(lista_salas,code_sala)
                            if i == -1:
                                print("Não existe esse código de filme.")
                                res = input("Você deseja tentar novamente? sim(1) ou não(0) -->")
                                if res == 1:
                                    print("Digite um código diferente.")
                                elif res ==0:
                                    continuar=False
                                else:
                                    print("Resposta invalida, você será direcionado para o menu.")
                            else:
                                lista_sessoes[posicao].codigo_da_sala = code_sala
                                continuar=False
                        elif op3 == '4':
                            preco = int(input("Digite o preço da sessão: "))
                            if preco < 0:
                                print("Preço inválido. Tente outro valor.")
                            else:
                                lista_sessoes[posicao].preco_do_ingresso = preco
                                continuar=False
                        elif op3 == '0':
                            print("Retornando...")
                            continuar=False
                        else:
                            print("Opção inválida!")
                            print("Escolha outra opção para alterar ou digite 0 para sair")
            elif res=="0":
                print("Os dados continuam inalterados!")
            else:
                print("Opção inválida!")
        else:
            print("A sala não encontra-se no banco de dados!")

    # Função de exclusão:
def excluir_sessao(lista_sessoes):
    if lista_sessoes == []:
        print("Não há sessões cadastradas. Você precisa cadastrar uma sessão.")
    else:
        code_sala=input("Digite o código do sala da sessão:")
        data = input("Digite a data da sessão - nesse formato dd/mm/aaaa:  ")
        horario = input("Digite o horario de início e fim da sessão - nesse formato (hh:mm/hh:mm):   ")
        posicao = verificar_posicao_sessao(lista_sessoes,code_sala,data,horario)
        if posicao != -1:
            res = input("Deseja mesmo excluir esse cadastro? 1-(SIM) 0-(NÃO): ")
            if res=="1":
                lista_sessoes.pop(posicao)
                print("O cadastro foi excluido!")
            elif res=="0":
                print("O cadastro continua no banco de dados!")
            else:
                print("Opcão invalida.")
        else:
            print("O cadastro não encontra-se no banco de dados!")

        # Função para inserir novas salas a lista
def inserir_sessoes(lista_sessoes,lista_salas,lista_filmes):
    s = Sessao()
    if lista_filmes != [] and lista_salas != []:
        continuar = True
        while continuar:
            code_sala=input("Digite o código do sala da sessão:")
            i = verificar_posicao(lista_salas,code_sala)
            if i == -1:
                print("O código digitado não está cadastrado!")
                print("Não existe esse código de filme.")
                res = input("Você deseja tentar novamente? sim(1) ou não(0) -->")
                if res == 1:
                    print("Digite um código diferente.")
                elif res ==0:
                    continuar=False
                else:
                    print("Resposta invalida, você será direcionado para o menu.") 
            else:
                data = input("Digite a data da sessão - nesse formato dd/mm/aaaa:  ")
                horario = input("Digite o horario de início e de termino da sessão - nesse formato e sem parenteses (hh:mm/hh:mm)   ")                
                interposicao = verificar_interposicao_sessao(lista_sessoes,data,horario,code_sala)
                if interposicao == True:
                    print("Alguma sessão existete está entrando em conflito com a sessão nova, troquei os horarios, a data ou a sala.")
                else:
                    continuar = False
        while continuar:
            code_filme=input("Digite o código do filme da sessão:")
            i = verificar_posicao(lista_filmes,code_filme)
            if i == -1:
                print("O esse filme não está cadastrado! Utilize um codigo existem")
                print("Não existe esse código de filme.")
                res = input("Você deseja tentar novamente? sim(1) ou não(0) -->")
                if res == 1:
                    print("Digite um código diferente.")
                elif res ==0:
                    continuar=False
                else:
                    print("Resposta invalida, você será direcionado para o menu.") 
            else:
                continuar = False
            
        s.codigo_da_sala = code_sala
        s.codigo_do_filme = code_filme
        s.data = data
        s.horario = horario
        s.preco_do_ingresso = int(input("Informe o preço do ingresso: "))
        lista_sessoes.append(s)
        

        print("Sessão cadastrada com sucesso!")
    elif lista_filmes != [] and lista_salas == []:
        print("Não há salas cadastradas no sistema. Cadastre um sala.")
    elif lista_filmes == [] and lista_salas != []:
        print("Não há filmes cadastrados no sistema. Cadastre um filme.")
    else:
        print("Não há filmes ou salas cadastrado no sistema. Cadastre um filme e uma sala.")


################################################################################################################
################################################################################################################
#                                      Funções Relátorios                                                
################################################################################################################
################################################################################################################
#Relatórios:
#a) Mostrar todos os dados de todas as salas cujo tipo de exibição seja X e
# capacidade para mais de Y pessoas, onde X e Y são fornecidos pelo usuário;


# b) Mostrar todos os dados de todos os filmes que foram lançados a partir do
# ano X, onde X é fornecido pelo usuário;


# c) Mostrar o código do filme, nome do filme, atores, código da sala, nome da
# sala e os demais atributos de todas as sessões exibidas a partir de uma
#data inicial X até uma data final Y, onde ambas as datas são fornecidas pelo usuário.

def relatorio_1(lista_salas):
    print("************************************************")
    print("#######            Relatório 1            ######")
    print("************************************************")
    print("  ")
    print("Veja o relatório das salas que tenham certo tipo de exibição")
    print("e capacidade igual ou acima da selecionada.")
    tipo_exibicao = input("Qual o tipo de exibição ('normal' ou '3D'):   ")
    capacidade = int(input("Qual a capacidade da sala: "))
    l = lista_salas
    
    achou = False
    i = 0
    while i < len(lista_salas):
        if tipo_exibicao == l[i].tipo_de_exibição and capacidade <= l[i].capacidade:
            print("************************************************")
            imprimir_salas(l[i])
            achou = True
        i = i + 1
    if not achou:
        print("Não foi encontrada salas com esses paramentros.")
    print("Fim do relatório 1.")

def relatorio_2(lista_filmes):
    print("************************************************")
    print("#######            Relatório 2            ######")
    print("************************************************")
    print("  ")
    print("Veja o relatório dos filmes que tenham si lançados a partir")
    print("de uma certo ano.")
    ano = int(input("Qual o ano de lançamento :   "))
    l = lista_filmes
    i = 0
    achou = False
    while i < len(lista_filmes):
        if ano <= l[i].ano_de_lancamento:
            print("************************************************")
            imprime_filme(l[i])
            achou = True
        i = i + 1
    if not achou:
        print(f"Não foi achado filmes lançados a partir de {ano}")
    print("Fim do relatório 2.")

def relatorio_3(lista_salas,lista_filmes,lista_sessoes):
    print("************************************************")
    print("#######            Relatório 3            ######")
    print("************************************************")
    print("  ")
    print("Veja o relatório completo dos filmes e salas vinculados a todas ")
    print("sessões que estão dentro de um período de tempo.")
    data_inicial = input("Qual a data de inicio do período (dd/mm/aaaa):   ")
    data_final = input("Qual a data final do período (dd/mm/aaaa):   ")
    data_inicial_int = int(data_inicial[:2]+data_inicial[3:5]+data_inicial[6:])
    data_final_int = int(data_final[:2]+data_final[3:5]+data_final[6:])
    
    # imprimindo posições das sessões que se enquadram no período
    l = lista_sessoes
    i = 0
    achou = False
    while i < len(lista_sessoes):
        if data_inicial_int <= int(l[i].data[:2]+l[i].data[3:5]+l[i].data[6:]) and data_final_int >= int(l[i].data[:2]+l[i].data[3:5]+l[i].data[6:]):
            achou = True
            print("                      *******************                     ")
            imprimir_sessao(lista_sessoes,i)
            code_filme = l[i].codigo_do_filme
            code_sala = l[i].codigo_da_sala
            posicao = 0
            while posicao < len(lista_filmes):
                if code_filme == lista_filmes[posicao].codigo:
                    imprime_filme(lista_filmes[posicao])
                if code_sala == lista_salas[posicao].codigo:
                    imprimir_salas(lista_salas[posicao])
                posicao = posicao + 1
        i = i + 1    
    if not achou:
        print(f"Não foi encontrado sessões entre {data_inicial} e {data_final}")
    print("Fim do relatório 3.")
    



################################################################################################################
################################################################################################################
#                                      Função Arquivo                                                
################################################################################################################
################################################################################################################

def verificar_existencia_arquivo(nome_arquivo):
    import os
    if os.path.exists(nome_arquivo):
        return True
    else:
        return False

def ler_arquivo_filme(nome_arquivo,lista_filmes):
    
    arq = open(nome_arquivo,"r")
    arquivo = arq.read()
    arquivo = arquivo.split("\n")
    i = 0
    while i < len(arquivo)-1:
        f = Filme()
        dados_filme = arquivo[i].split(";")
        f.codigo = dados_filme[0]
        f.nome = dados_filme[1]
        f.ano_de_lancamento = int(dados_filme[2])
        f.diretor = dados_filme[3]
        f.atores = dados_filme[4]
        lista_filmes.append(f)
        i = i + 1
    arq.close()
    return lista_filmes

def ler_arquivo_sala(nome_arquivo,lista_salas):
    
    arq = open(nome_arquivo,"r")
    arquivo = arq.read()
    arquivo = arquivo.split("\n")

    i = 0
    while i < len(arquivo)-1:
        s = Sala()
        dados_sala = arquivo[i].split(";")
        s.codigo = dados_sala[0]
        s.nome = dados_sala[1]
        s.capacidade = int(dados_sala[2])
        s.tipo_de_exibição = dados_sala[3]
        s.acessivel = dados_sala[4]
        lista_salas.append(s)
        i = i + 1
    arq.close()
    return lista_salas

def ler_arquivo_sessao(nome_arquivo,lista_sessoes):
    
    arq = open(nome_arquivo,"r")
    arquivo = arq.read()
    arquivo = arquivo.split("\n")
    
    i = 0
    while i < len(arquivo)-1:
        s = Sessao()
        dados_sessao = arquivo[i].split(";")
        s.codigo_do_filme = dados_sessao[0]
        s.codigo_da_sala = dados_sessao[1]
        s.data = dados_sessao[2]
        s.horario = dados_sessao[3]
        s.preco_do_ingresso = int(dados_sessao[4])
        lista_sessoes.append(s)
        i = i + 1
    arq.close()
    return lista_sessoes

def criar_arquivo(nome_arquivo):
    arq = open(nome_arquivo,"w")
    arq.close()

def escrever_arquivo_salas(nome_arquivo,lista_salas):
    l = lista_salas
    arq = open(nome_arquivo,"w")
    i = 0
    while i < len(lista_salas):
        linha = str(str(l[i].codigo) + ";" + str(l[i].nome) + ";" + str(l[i].capacidade) + ";" + str(l[i].tipo_de_exibição) + ";" + str(l[i].acessivel))
        arq.write(linha)
        arq.write("\n")
        i = i + 1
    arq.close()

def escrever_arquivo_filmes(nome_arquivo,lista_filmes):
    l = lista_filmes
    arq = open(nome_arquivo,"w")
    i = 0
    while i <len(lista_filmes):
        linha = str(str(l[i].codigo) + ";" + str(l[i].nome) + ";" + str(l[i].ano_de_lancamento) + ";" + str(l[i].diretor) + ";" + str(l[i].atores))
        arq.write(linha)
        arq.write("\n")
        i = i + 1
    arq.close()

def escrever_arquivo_sessoes(nome_arquivo,lista_sessoes):
    l = lista_sessoes
    arq = open(nome_arquivo, "w")
    i = 0
    while i < len(lista_sessoes):
        linha = str(str(l[i].codigo_do_filme) + ";" + str(l[i].codigo_da_sala) + ";" + str(l[i].data) + ";" + str(l[i].horario) + ";" + str(l[i].preco_do_ingresso))
        arq.write(linha)
        arq.write("\n")
        i = i + 1
    arq.close()







################################################################################################################
################################################################################################################
#                                      Função Main                                                
################################################################################################################
################################################################################################################

    # Função main(principal)
def main():

        #criando listas
    lista_salas = []
    lista_filmes = []
    lista_sessoes = []

        #garantindo existencia de arquivos para salvar dados de cada lista
    existe = verificar_existencia_arquivo("salas.txt")
    if existe:
        lista_salas = ler_arquivo_sala("salas.txt",lista_salas)
    else:
        criar_arquivo("salas.txt")
    
    existe = verificar_existencia_arquivo("filmes.txt")
    if existe:
        lista_filmes = ler_arquivo_filme("filmes.txt",lista_filmes)
    else:
        criar_arquivo("filmes.txt")

    existe = verificar_existencia_arquivo("sessoes.txt")
    if existe:
        lista_sessoes = ler_arquivo_sessao("sessoes.txt",lista_sessoes)

    else:
        criar_arquivo("sessoes.txt")

        # o menu principal
    opção = -1
    while opção != "0":
        opção = menu()
        if opção == "1":
            salas(lista_salas)
        elif opção == "2":
            filmes(lista_filmes)
        elif opção == "3":
            sessoes(lista_sessoes,lista_filmes,lista_salas)
        elif opção == "4":
            relatorios(lista_salas,lista_filmes,lista_sessoes)
        elif opção != "0":
            print("Opção inválida! Escolhar outra opção.")

    print("###      Sistema desligado.     ####")
    print("Obrigado por usado Films System!!!")

    escrever_arquivo_filmes("filmes.txt",lista_filmes)
    escrever_arquivo_salas("salas.txt",lista_salas)
    escrever_arquivo_sessoes("sessoes.txt",lista_sessoes)
    
    
def filmes(lista_filmes):
    op = ''
    while op != '0':
        op = menu_filmes()
        if op == '1':
            inserir_filme(lista_filmes)
        elif op == '2':
            listar_filmes(lista_filmes)
        elif op == '3':
            listar_um_filme(lista_filmes)
        elif op == '4':
            op2= ''
            while op2 != '0' :
                op2 = alterar_excluir_filmes()
                if op2 == '1':
                    alterar_filmes(lista_filmes)
                elif op2 == '2':
                    excluir_filmes(lista_filmes)
                elif op2 == '0':
                    print("Retornando...")
                else:
                    print("Opcao invalida.")
        elif op == '0':
            print("Voltando ao menu principal.")
        else:
            print("Opção invalida.")

def salas(lista_salas):
    op = ''
    while op != '0':
        op = menu_salas()
        if op == '1':
            inserir_salas(lista_salas)
        elif op == '2':
            apresentar_todas_salas(lista_salas)
        elif op == '3':
            listar_uma_sala(lista_salas)
        elif op == '4':
            op2= ''
            while op2 != '0' :
                op2 = alterar_excluir_salas()
                if op2 == '1':
                    alterar_salas(lista_salas)
                elif op2 == '2':
                    excluir_salas(lista_salas)
                elif op2 == '0':
                    print("Retornando...")
                else:
                    print("Opcao invalida.")
        elif op == '0':
            print("Voltando ao menu principal.")
        else:
            print("Opção invalida.")


def sessoes(lista_sessoes,lista_filmes,lista_salas):
    op = ''
    while op != '0':
        op = menu_sessoes()
        if op == '1':
            inserir_sessoes(lista_sessoes,lista_salas,lista_filmes)
        elif op == '2':
            apresentar_todas_sessoes(lista_sessoes)
        elif op == '3':
            listar_uma_sessao(lista_sessoes)
        elif op == '4':
            op2= ''
            while op2 != '0' :
                op2 = alterar_excluir_sessao()
                if op2 == '1':
                    alterar_sessao(lista_sessoes,lista_filmes,lista_salas)
                elif op2 == '2':
                    excluir_sessao(lista_sessoes)
                elif op2 == '0':
                    print("Retornando...")
                else:
                    print("Opcao invalida.")
        elif op == '0':
            print("Voltando ao menu principal.")
        else:
            print("Opção invalida.")

def relatorios(lista_salas,lista_filmes,lista_sessoes):
    op = ""
    while op != "0":
        op = menu_relatorios()
        if op == "1":
            relatorio_1(lista_salas)
        elif op == "2":
            relatorio_2(lista_filmes)
        elif op == "3":
            relatorio_3(lista_salas,lista_filmes,lista_sessoes)
        elif op == "0":
            print("Voltando ao menu principal!")
        else:
            print("Opção inválida. Escolha uma opção válida.")

##############

#execussão programa
main()