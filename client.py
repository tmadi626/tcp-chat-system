import socket
import threading
import time
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

nickname = input("Choose a nickname: ")
color = Fore.WHITE

host = '192.168.2.1' #local
port = 5555

client = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
client.connect( (host, port) )

def write():
    while True:
        message = input(f'{color}{nickname}{Fore.WHITE}: ')
        client.send( message.encode('ascii'))



def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if 'NICK' in message :
                client.send(nickname.encode('ascii'))
                global color 
                color = message.split(',')[1]
                print(f'assigned a color: {color}{nickname}{Fore.RESET}')

            else:
                print(message)
        except socket.error as e:
            print(f"{Back.RED}[ERR]{Back.RESET} An Error Occurred!:\n {e}\n")
            client.close()
            break



receive_thread = threading.Thread(target=receive)
receive_thread.start()

time.sleep(2)

write_thread = threading.Thread(target=write)
write_thread.start()