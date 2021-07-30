import tkinter
from PIL import ImageTk, Image
from functools import partial
import socket
import _thread
import time
client = 0
chances = 6
palavra = 'null'
def sendChosenLetter (ltr):
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
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    host = '127.0.0.1'
    port = 8000
    c.connect((host,port))
    global client
    client = c
    global chances
    global palavra
    while chances > 0:
        msg= 'null'
        if(palavra == 'null'):
            palavra = c.recv(2048).decode('ascii')
            desenhar(chances)
        print('   ' + palavra)
        ltr = input()
        sendChosenLetter(ltr)
        msg= c.recv(2048).decode('ascii')
        if(msg == 'errou'):
            chances -= 1
            print('Errou')
            if(chances == 0):
                print('Perdeu!')
        elif(msg.find('-') != -1):
            palavra = msg
            print('Acertou')
        elif(msg.find('-') == -1 and chances > 0):
            palavra = msg
            print('Ganhou!')

        desenhar(chances)
        
_thread.start_new_thread(socketCreation, () )
window = tkinter.Tk()
window.mainloop()
