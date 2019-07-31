from socket import socket, AF_INET, SOCK_STREAM

def echo_client(clinet_sock, addr):
    print('Got connectiono from', addr)

    client_in = open(client_sock.fileno(), 'rt', encoding = 'latin-1', closefd = False)
    client_out = open(client_sock.fileno(), 'wt', encoding = 'latin-1', closefd = False)

    for line in client_in:
        client_out.write(line)
        client_out.flush()

    client_sock.close()

def echo_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(80)
    while True:
        client, addr = sock.accept()
        echo_client(client, addr)
