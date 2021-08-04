from functools import partial
import socket
import time

client = 0
chances = 6
palavra = 'null'

def Main():
    print('Bem-vindo!! Este é o cliente')
    print('Vamos começar o jogo da forca')

    try:
        criarSocket()
    except Exception as e: print(e)

def enviarLetraEscolhida (ltr):
    client.send(ltr.encode('ascii'))  
    
def desenhar (chances):
    if (chances == 6):
        print('+----+')
        print('|    |')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
    elif (chances == 5):
        print('+----+')
        print('|    |')
        print('|    O')
        print('|')
        print('|')
        print('|')
        print('|')
    elif (chances == 4):
        print('+----+')
        print('|    |')
        print('|    O')
        print('|    |')
        print('|')
        print('|')
        print('|')
    elif (chances == 3):
        print('+----+')
        print('|    |')
        print('|    O')
        print('|   /|')
        print('|')
        print('|')
        print('|')
    elif (chances == 2):
        print('+----+')
        print('|    |')
        print('|    O')
        print('|   /|\ ')
        print('|')
        print('|')
        print('|')
    elif (chances == 1):
        print('+----+')
        print('|    |')
        print('|    O')
        print('|   /|\ ')
        print('|   /')
        print('|')
        print('|')
    elif (chances == 0):
        print('+----+')
        print('|    |')
        print('|    O')
        print('|   /|\ ')
        print('|   / \ ')
        print('|')
        print('|')
            
def socketCreation():
    # Cria um socket TCP/IP
    clientTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 8000
    #conectar o socket à uma porta
    clientTCP.connect((host,port))
    global client
    client = clientTCP
    global chances
    global palavra
    while chances > 0:
        msg= 'null'
        if(palavra == 'null'):
            palavra = clientTCP.recv(2048).decode('ascii')
            palavraDescoberta = clientTCP.recv(2048).decode('ascii')
            desenhar(chances)
        print('   ' + palavra)
        ltr = input()
        enviarLetraEscolhida(ltr)
        msg= clientTCP.recv(2048).decode('ascii')
        if(msg == 'errou'):
            chances -= 1
            print('Errou')
            if(chances == 0):
                print('Perdeu!')
                print('A palavra era: ' + palavraDescoberta)
        elif(msg.find('-') != -1):
            palavra = msg
            print('Acertou')
        elif(msg.find('-') == -1 and chances > 0):
            palavra = msg
            desenhar(chances)
            print('   ' + palavra)
            print('Ganhou!')
            break
        desenhar(chances)

if __name__ == '__main__':
    Main()        
