import socket
import threading
import colorama
from colorama import Fore, Back, Style
import random

from colorama.initialise import reset_all

colorama.init(autoreset=True)



host = '192.168.2.1' #local
port = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind( (host,port) )
server.listen()

clients = []
nicknames = []
colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]


def broadcast(sender, message):
    for client in clients:
        if client != sender:
            client.send(message)

def serverMsg():
    while True:
        try:
            message = input("Announce: ")

            for client in clients:
                client.send( f'{Back.GREEN}{Fore.BLACK}[Server]:{Style.RESET_ALL} {message}'.encode('ascii'))
        except:
            pass


def sendToEveryone(message):
    for client in clients:
        client.send(message)

def handle(client, nickname, COLOR):
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            broadcast( client, f'{COLOR}{nickname}{Fore.RESET}: {message}'.encode('ascii') )
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            sendToEveryone( f"{COLOR}{nickname}{Fore.RESET}{Style.DIM} has left the chat!".encode('ascii') )
            nicknames.remove(nickname)
            break



def receive():

    while True:
        print(f'{Back.GREEN}{Fore.BLACK}[{Fore.BLACK}LISTN]:{Style.RESET_ALL} Server is Listening...')

        client, address = server.accept()
        print( f"Connected with {Fore.YELLOW}{str(address)} ")

        COLOR = random.choice(colors)

        client.send(f'{Style.BRIGHT}NICK,{COLOR},{Fore.RESET}'.encode('ascii'))

        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f'Nickname of the client is {COLOR}{nickname}')
        sendToEveryone( f'{Back.GREEN}{Fore.BLACK}[MSG]:{Style.RESET_ALL} {COLOR}{nickname}{Fore.RESET} has joined the chat!'.encode('ascii') )
        client.send( f'\n{Back.WHITE}{Fore.GREEN}Welcome to the server!{Fore.RESET}{Style.RESET_ALL}'.encode('ascii') )

        thread = threading.Thread( target= handle, args=(client,nickname, COLOR) )
        thread.start()

print(f'{Back.GREEN}{Fore.BLACK}[START]:{Style.RESET_ALL} Server has started!!!')

announcements = threading.Thread( target= serverMsg )
announcements.start()
receive()

colorama.deinit()