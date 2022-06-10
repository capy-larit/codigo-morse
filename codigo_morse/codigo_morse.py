"""Código Morse"""

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

decodificacao = dict(map(reversed, codificacao.items()))


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


def decodificar(frase: str) -> str:
    """
    Decodifica a frase para português.

    Args:
      - frase (str): frase que será decodificada.

    Returns:
      - str: frase decodificada em português.
    """

    frase_decodificada = ''
    for caractere in frase.split():
        frase_decodificada += f'{decodificacao[caractere]}'
    return frase_decodificada


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

        if opcao == '2':

            frase = input('\nDigite o que deseja decodificar: ').lower()

            print('\nDecodificando para português...\n')
            time.sleep(2)
            print('Sua resposta: ')

            print(decodificar(frase))

        time.sleep(3)


if __name__ == '__main__':
    main()
