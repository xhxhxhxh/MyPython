import socket

def main():

    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    send_ip = ('127.0.0.1', 8083)

    # 建立tcp连接
    tcp_socket.connect(send_ip)

    while True:
        # 发送数据
        send_message = input('请输入要下载的文件名：')
        tcp_socket.send(send_message.encode('utf-8'))
        receive_data = tcp_socket.recv(1024)
        if receive_data:
            with open('new_' + send_message, 'wb') as f:
                f.write(receive_data)

    # 关闭连接
    tcp_socket.close()

if __name__ == "__main__":
    main()