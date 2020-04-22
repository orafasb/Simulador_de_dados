import random

class simuladordado:
    def __init__(self):
        self.valor_inicial=1
        self.valor_maximo=6
        self.mensagem = "Digite Sim para jogar os dados ou qualquer tecla para finalizar. "

    def iniciar(self):
        resposta = input(self.mensagem)
        while (resposta=="sim"):
            self.gerarvalordodado()
            resposta =input(self.mensagem)
            "break"
        else:
            print('Obrigado. ')


    def gerarvalordodado(self):
        print(random.randint(self.valor_inicial,self.valor_maximo))

simulador = simuladordado()
simulador.iniciar()