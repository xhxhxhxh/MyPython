import socket

def web_server(new_client_socket):
    request = new_client_socket.recv(1024) # 1024为接收数据的最大字节
    print(request)
    response = 'HTTP/1.1 200 OK\n\r'
    response += '\n\r <h1>请求成功</h1>'
    new_client_socket.send(response.encode('utf-8'))
    new_client_socket.close()

def main():

    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    localAddress = ('', 8082)  # 本地ip端口号
    tcp_server_socket.bind(localAddress)  # 绑定端口号

    # 让套接字从主动变为被动
    tcp_server_socket.listen(128)

    # 接收数据
    while True:
        # 等待新用户连接
        new_client_socket, client_addr = tcp_server_socket.accept()
        print('新用户已连接...')
        web_server(new_client_socket)

    # 关闭连接
    tcp_server_socket.close()

if __name__ == "__main__":
    main()