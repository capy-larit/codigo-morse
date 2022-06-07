"""Código Morse"""

from typing import Dict
import time

codificacao = {
    'a' : '.-',
    'b' : '-...',
    'c' : '-.-.',
    'd' : '-..',
    'e' : '.',
    'f' : '..-.',
    'g' : '--.',
    'h' : '....',
    'i' : '..',
    'j' : '.---',
    'k' : '-.-',
    'l' : '.-..',
    'm' : '--',
    'n' : '-.',
    'o' : '---',
    'p' : '.--.',
    'q' : '--.-',
    'r' : '.-.',
    's' : '...',
    't' : '-',
    'u' : '..-',
    'v' : '...-',
    'w' : '.--',
    'x' : '-..-',
    'y' : '-.--',
    ' ' : '/',
}


while True:

    print('*=' * 20)
    print(f"{'Deseja codificar ou decodificar?' : ^40}")
    print('*=' * 20)

    opcao = input('\nMENU: \n1 - Codificar\n2 - Decodificar\nSua opção: ')

    if opcao == '1':

        frase = input('\nDigite o que deseja codificar: ').lower()

        print('\nCodificando para Código Morse...\n')
        time.sleep(2)
        print('Sua resposta: ')
        for i in frase:
            print(f'{codificacao[i]}', end="")
        print('\n')

    time.sleep(3)

    # def decodificacao(*args) -> Dict[str, str]
