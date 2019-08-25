import socket

def send_file(new_client_socket, client_addr):
    file_name = new_client_socket.recv(1024).decode('utf-8')
    print('要下载的文件名是：%s' % file_name)
    file_content = None
    try:
        file = open(file_name, 'rb')
        file_content = file.read()
        file.close()
    except Exception as result:
        print('文件不存在')

    if file_content:
        new_client_socket.send(file_content)
        return True
    else:
        return False


def main():

    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    localAddress = ('', 8083)  # 本地ip端口号
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
            if send_file(new_client_socket, client_addr):
                continue
            else:
                break

        new_client_socket.close()

    # 关闭连接
    tcp_server_socket.close()

if __name__ == "__main__":
    main()