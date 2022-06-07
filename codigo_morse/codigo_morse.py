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


def cabecalho() -> None:
    print('*=' * 20)
    print(f"{'Deseja codificar ou decodificar?' : ^40}")
    print('*=' * 20)


def codificar(frase: str) -> str:
    """
    Codifica a frase em código morse.

    Args:
      - frase (str): frase que será codificada.

    Returns:
      - str: frase codificada em morse.
    """

    frase_codificada = ''
    for caractere in frase:
        frase_codificada += f'{codificacao[caractere]} '
    return frase_codificada.strip()


def main():
    while True:

        cabecalho()

        opcao = input('\nMENU: \n1 - Codificar\n2 - Decodificar\nSua opção: ')

        if opcao == '1':

            frase = input('\nDigite o que deseja codificar: ').lower()

            print('\nCodificando para Código Morse...\n')
            time.sleep(2)
            print('Sua resposta: ')

            print(codificar(frase))


        time.sleep(3)


if __name__ == '__main__':
    main()
