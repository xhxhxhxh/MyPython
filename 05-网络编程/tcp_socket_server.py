import socket

def main():

    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    localAddress = ('', 8082)  # 本地ip端口号
    tcp_server_socket.bind(localAddress)  # 绑定端口号

    # 让套接字从主动变为被动
    tcp_server_socket.listen(128)

    print('等待新用户到来...')

    # 接收数据
    while True:
        # 等待新用户连接
        new_client_socket, client_addr = tcp_server_socket.accept()
        print('新用户已连接...')
        while True:
            receive_data = new_client_socket.recv(1024) # 1024为接收数据的最大字节

            if not receive_data: # 客户端关闭则退出
                break

            print(receive_data.decode('utf-8'))

        new_client_socket.close()

    # 关闭连接
    tcp_server_socket.close()

if __name__ == "__main__":
    main()