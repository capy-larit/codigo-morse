"""Código Morse"""

import time

codificacao = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    ' ': '/',
}

decodificacao = dict(map(reversed, codificacao.items()))


def cabecalho() -> None:
    print('*=' * 20)
    print(f"{'Deseja codificar ou decodificar?' : ^40}")
    print('*=' * 20)


def tradutor(frase: str, cifrar: bool, dicionario: dict) -> str:
    """
    Codifica e decodifica em código morse.

    Args:
      - frase (str): frase que será codificada ou decodificada.
      - cifrar (bool): flag para definir se será codificada ou decodificada.
      - dicionario (dict): dicionário que será usado na tradução.

    Returns:
      - str: frase codificada ou decodificada.
    """

    frase_final = ''
    try:
        frase = frase if cifrar else frase.split()
        for caractere in frase:
            frase_final += f'{dicionario[caractere]}{cifrar * " "}'
        return frase_final.strip()
    except KeyError:
        print(
            f'A frase {frase} é inválida, informe o '
            f'{"texto em português" if cifrar else "código morse"}.'
        )

    return frase_final


def codificar(frase: str) -> str:
    """
    Codifica a frase em código morse.

    Args:
      - frase (str): frase que será codificada.

    Returns:
      - str: frase codificada em morse.
    """

    return tradutor(frase, True, codificacao)


def decodificar(frase: str) -> str:
    """
    Decodifica a frase para português.

    Args:
      - frase (str): frase que será decodificada.

    Returns:
      - str: frase decodificada em português.
    """

    return tradutor(frase, False, decodificacao)


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
