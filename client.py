from pickle import dump

change = 0
if change == 0:
    import socket
    import pickle
    import time
    import os

    PORT = 40019
    list_name_file = os.listdir('.')
    #Add patterns
    old_pattern = ['']
    old_ip = ['192.168.1.218']
    print('Select a server ip(number)(-1 to new ip,esc to exit): ')
    continue_while = 1
    for i in range(0, len(old_ip)):
        print('[' + str(i) + '] ' + old_ip[i])
    ip = input("Ip's number:")
    if ip == 'esc':
        continue_while = 0
    elif int(ip) == -1:
        ip = input("New server ip:")
    else:
        ip = old_ip[int(ip)]
    HOST = ip
    while (continue_while):
        print('Select a pattern(number)(-1 to new pattern,esc to exit): ')
        for i in range(0, len(old_pattern)):
            print('[' + str(i) + '] ' + old_pattern[i])
        pattern = input("Pattern's number:")
        if pattern == 'esc':
            break
        elif int(pattern) == -1:
            pattern = input("New pattern:")
        else:
            pattern = old_pattern[int(pattern)]
        print('Select a file(number): ')
        for i in range(0, len(list_name_file)):
            print('[' + str(i) + '] ' + list_name_file[i])
        name_file = input("File's number:")
        if (name_file == 'esc'):
            break
        name_file = list_name_file[int(name_file)]
        file = open(name_file, 'rb')
        list_ = list()
        data = file.read()
        # To send pattern file
        name_file = pattern + name_file
        list_.append(name_file)
        list_.append(data)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            byte_send_Tot = 0
            byte_send = 0
            while (1):
                byte_send_Tot = byte_send_Tot + byte_send
                print("Mancano:" + str(len(pickle.dumps(list_)) - byte_send_Tot))
                if (len(pickle.dumps(list_)) == byte_send_Tot):
                    print("Dati finiti")
                    # s.close()
                    s.shutdown(socket.SHUT_WR)
                    print(s.recv(1024))

                    s.close()
                    break

                byte_send = s.send(pickle.dumps(list_)[0 + byte_send_Tot:100000 + byte_send_Tot])
                # print('Send: ' + str(byte_send) + ' bytes')
            print("Risposta")
            print("Fine")
