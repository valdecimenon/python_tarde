#frutas.py

import time


#tipos de arquivos: texto ou binário
#modo de acesso ao arquivo:
#  1. Somente leitura (read) = 'r'
#  2. Escrita (write) = 'w'
#  3. Anexar (append) = 'a'

lista = []

def entrar_fruta():
    fruta = input('Digite o nome de uma fruta: ')
    lista.append(fruta)


def salvar_frutas():
    arquivo = open('frutas.txt', 'w')

    for fruta in lista:
        arquivo.write(fruta + '\n')
        
    arquivo.close()
    print('Lista de frutas salva')


#recupera as frutas salvas no arquivo
def recuperar_frutas():
    arquivo = open('frutas.txt', 'r')

    lista.clear()
    for linha in arquivo:
        vetor = linha.split('\n')  #remove '\n' do final da linha
        lista.append(vetor[0])

    arquivo.close()
    print('Lista de frutas recuperada')


def anexar_frutas():
    arquivo = open('frutas.txt', 'r')

    for linha in arquivo:
        vetor = linha.split('\n')  #remove '\n' do final da linha
        lista.append(vetor[0])

    arquivo.close()
    print('Lista de frutas anexada')


def limpar_lista():
    lista.clear()
    print('Lista está vazia')
    

def menu():

    while True:
        print('\n\n\n##### App Frutas #####')
        print('1 = entrar fruta')
        print('2 = mostrar lista de frutas')
        print('3 = salvar lista de frutas')
        print('4 = recuperar lista de frutas')
        print('5 = anexar lista de frutas')
        print('6 = limpar lista de frutas')
        print('7 = sair do programa')

        opcao = int(input('Qual opção? '))
        if opcao == 1:
            entrar_fruta()
        elif opcao == 2:
            print(lista)
        elif opcao == 3:
            salvar_frutas()
        elif opcao == 4:
            recuperar_frutas()
        elif opcao == 5:
            anexar_frutas()
        elif opcao == 6:
            limpar_lista()
        elif opcao == 7:
            print('\nSaindo...')
            time.sleep(1) #espera 1 segundo
            print('Fui!!')
            break
        else:
            print('Opção inválida!!')





menu()

