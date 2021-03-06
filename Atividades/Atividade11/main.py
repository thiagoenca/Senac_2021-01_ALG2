"""
Construa o algoritmo em Python de uma lista duplamente encadeada que possui uma função para inserir elementos, uma para
imprimir os elementos na ordem que foram inseridos e uma função para imprimir os elementos na ordem inversa a que foram
inseridos.
"""

# Imports
from Classes.Lista import Lista
from ClassesAuxiliares.AuxMethods import AuxMethods
from ClassesAuxiliares.FormatFonts import FormatFonts
from ClassesAuxiliares.Messages import Messages

lista = Lista()
aux = AuxMethods()
fonte = FormatFonts()
msg = Messages()

# Constantes para centralizar o nome dos menus
MENU = 'MENU'
ADICIONAR = 'ADICIONAR ITEM NA LISTA'
IMPRIMIR = 'LISTA DUPLAMENTE ENCADEADA'
IMPRIMIR_INVERTIDO = 'LISTA DUPLAMENTE ENCADEADA INVERTIDA'


# Métodos referentes as opções dos menus
def menu(desc_menu):
    aux.clear_screen_menu(desc_menu)

    return input(f'''
    {fonte.green('0.')} Finalizar o programa
    {fonte.green('1.')} Adicionar
    {fonte.green('2.')} Imprimir
    {fonte.green('3.')} Imprimir invertido

Escolha a opção desejada: ''')


def adicionar_item(desc_menu):
    aux.clear_screen_menu(desc_menu)
    aux.insert_line()

    numero = 1
    while numero <= 5:
        add = aux.input_int(f'Informe o {numero}º número a ser adicionado: ')
        lista.adicionar(add)
        numero += 1

    aux.print_message('Números adicionados com sucesso.')
    aux.press_enter()


def imprimir(desc_menu):
    aux.clear_screen_menu(desc_menu)
    aux.insert_line()

    if lista.lista_vazia():
        print('A lista está vazia.')
    else:
        lista.imprimir()
    aux.press_enter()


def imprimir_invertido(desc_menu):
    aux.clear_screen_menu(desc_menu)
    aux.insert_line()

    if lista.lista_vazia():
        print('A lista está vazia.')
    else:
        lista.imprimir_invertido()
    aux.press_enter()


# Programa
while True:
    opcao = menu(MENU)

    if opcao == '0':
        aux.finish_program(MENU)
        break
    elif opcao == '1':
        adicionar_item(ADICIONAR)
    elif opcao == '2':
        imprimir(IMPRIMIR)
    elif opcao == '3':
        imprimir_invertido(IMPRIMIR_INVERTIDO)
    else:
        aux.invalid_option(MENU)
