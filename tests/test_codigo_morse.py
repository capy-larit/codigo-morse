from codigo_morse import codificar


def test_codificar_ola_deve_retornar_codigo_correto():
    esperado = '--- .-.. .-'
    assert codificar('ola') == esperado


def test_codificar_frase_com_espaco():
    esperado = '--- .-.. .- / --- .-.. .- / --- .-.. .-'
    assert codificar('ola ola ola') == esperado
