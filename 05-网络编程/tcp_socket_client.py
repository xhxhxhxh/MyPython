import socket

def main():

    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    send_ip = ('127.0.0.1', 8082)

    # 建立tcp连接
    tcp_socket.connect(send_ip)

    while True:
        # 发送数据
        send_message = input('请输入要发送的数据：')
        if send_message == 'exit':
            break

        tcp_socket.send(send_message.encode('utf-8'))

    # 关闭连接
    tcp_socket.close()

if __name__ == "__main__":
    main()