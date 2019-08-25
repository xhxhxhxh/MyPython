import socket

def main():

    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    send_ip = ('127.0.0.1', 8081)

    while True:
        # 发送数据
        send_message = input('请输入要发送的数据：')
        if send_message == 'exit':
            break

        udp_socket.sendto(send_message.encode('utf-8'), send_ip)

    # 关闭连接
    udp_socket.close()

if __name__ == "__main__":
    main()