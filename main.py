def somar(valor_principal,acrescimo):
    '''
        Adiciona o acrescimo ao valor principa

        Args:
            valor_principal (float): valor inicial da soma
            acrescimo (float): valor a ser adicionado ao valor inicial

        Retuns:
            float: soma do valor principal e acrescimo
    '''
    return valor_primcipal + acrescimo

def testar_operacao_soma():
    # Arrange
    valor1 = 100.0
    valor2 = 50.0
    # Act
    resultado = somar(valor1, valor2)
    # Assert
    assert resultado == 150.0, "A soma falhou!"
    print("Teste de Soma: PASSOU!")

testar_operacao_soma()
