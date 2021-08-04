import socket
import random

def main():
    print('Bem-vindo!! Este é o servidor')
    try:
        # Cria um socket TCP/IP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        host = '127.0.0.1'
        port = 8000
        #associa o socket à uma porta
        s.bind((host,port))

        #coloca o socket no modo servidor, e define a quantidade de solicitações de novas conexões que podem ser enfileiradas (5 não tenha necessidade de 5, 1 era o suficiente)
        s.listen(5)
        
        #espera por novas solicitações de conexões.
        c,ad = s.accept() 

        print('Connection Established with: '+ad[0])
        meuArquivo = open('dicionario.txt')
        palavras = meuArquivo.read().split('\n')
        start = True
        palavraAleatoria = ''
        palavraAleatoriaEscondida = ''
        while True:
            if(start):
                # envia palavra encolhida
                palavraAleatoria = palavras [random.randint(0,len(palavras)-1)]
                palavraAleatoriaEscondida = "-"*len(palavraAleatoria)
                c.send(palavraAleatoriaEscondida.encode('ascii'))
                c.send(palavraAleatoria.encode('ascii')) #não precisa dessa linha, esquecemos de tirar
                start = False
            else:
                #recebe letra
                letraRecebida = c.recv(2048).decode('ascii')
                # esquecemos de tirar o reset, mas basicamente se o cliente escrever reset, o jogo começa de novo. ps: não funciona direito
                if(letraRecebida == 'reset'):
                    start = True
                    palavraAleatoria = ''
                    palavraAleatoriaEscondida = ''
                else:
                    #verificar letra escolhida e retornar uma resposta    
                    index = []
                    aux = ''
                    if (palavraAleatoria.find(letraRecebida) != -1):
                        for i in range(0,len(palavraAleatoria)):
                            if(letraRecebida == palavraAleatoria[i]):
                                aux += letraRecebida
                            else :
                                aux += palavraAleatoriaEscondida[i]
                        palavraAleatoriaEscondida = aux
                        c.send(palavraAleatoriaEscondida.encode('ascii'))
                    else :
                        c.send('errou'.encode('ascii'))     
        s.close()
    except socket.error as e :
        print(e)
    except KeyboardInterrupt :
        print('chat ended')

if __name__ == "__main__":
    main()