nome = "Isabela Saenz Cardoso"
matricula = 2021040032

def EP_answers():
    ################### NÃO ALTERE DENTRO DA SEÇÃO ABAIXO ###################
    import numpy as np
    np.random.seed(1)
    inversa, pseudo_inversa, QR, substituicao, retrosubstituicao, \
    positiva_definida, simetrica, cholesky = [None]*8
    #########################################################################

    ## 1.1
    ## Insira seu código aqui
    def inversa(X, y):
        np.linalg.inv(np.dot(X.T, X))
    ## 1.2
    ## Insira seu código aqui

    ## 1.3
    ## Insira seu código aqui

    ## 1.4
    ## Insira seu código aqui

    ################### NÃO ALTERE DENTRO DA SEÇÃO ABAIXO ###################
    answers = {
        "1.1.1" : inversa,
        "1.2" : pseudo_inversa,
        "1.3" : QR,
        "1.4.1" : substituicao,
        "1.4.2" : retrosubstituicao,
        "1.4.3" : positiva_definida,
        "1.4.4" : simetrica,
        "1.4.5" : cholesky
    }
    return answers
    ##########################################################################