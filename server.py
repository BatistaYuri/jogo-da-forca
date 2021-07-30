import socket
import random
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    host = '127.0.0.1'
    port = 8000
    s.bind((host,port))
    s.listen(5)
    c,ad = s.accept()
    print('Connection Established with: '+ad[0])
    palavras = ['jogador']
    start = True
    palavraAleatoria = ''
    palavraAleatoriaEscondida = ''
    while True:
        if(start):
            palavraAleatoria = palavras [random.randint(0,len(palavras)-1)]
            palavraAleatoriaEscondida = "-"*len(palavraAleatoria)
            c.send(palavraAleatoriaEscondida.encode('ascii'))
            start = False
        else:
            letraRecebida = c.recv(2048).decode('ascii')
            if(letraRecebida == 'reset'):
                start = True
                palavraAleatoria = ''
                palavraAleatoriaEscondida = ''
            else:    
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