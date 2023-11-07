from os import extsep

import netifaces
change=0
if change==0:
    import socket
    import pickle
    import netifaces as ni
    HOST = ''
    PORT = 40019
    data = ''
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        while(True):
            try:
                ip = ni.ifaddresses(ni.interfaces()[1])[ni.AF_INET][0]['addr']
                print('Server (' + str(ip) + '):')
            except:
                print('Server:')
            conn, addr = s.accept()
            list_byte = b''
            print('Connected by', addr)
            while True:
                try:
                    print("Ricezione")
                    data = conn.recv(1000000)
                except socket.timeout:
                    print("Connessione scaduta")
                list_byte = list_byte + data
                print(len(data))
                if data == b'':
                    print("Fine ricezione dati")
                    conn.send(b"OK")
                    break
                #print(data)
            list_ = pickle.loads(list_byte)
            file = open(list_[0],'ab')
            file.write(list_[1])
            file.close()
            conn.close()
            print("Fine")
