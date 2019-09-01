import socket
import threading

def send(udp_socket, send_ip):
    """发送数据"""

    while True:
        # 发送数据
        send_message = input('请输入要发送的数据：')
        if send_message == 'exit':
            break

        udp_socket.sendto(send_message.encode('utf-8'), send_ip)

    # 关闭连接
    udp_socket.close()

def receive(udp_socket):
    """接收数据"""

     # 接收数据
    localAddress = ('', 8083)  # 本地ip端口号
    udp_socket.bind(localAddress)  # 绑定端口号
    while True:
        receive_data = udp_socket.recvfrom(1024) # 1024为接收数据的最大字节

        send_addr = receive_data[1]
        recev_msg = receive_data[0]

        print('%s: %s' % (str(send_addr), recev_msg.decode('utf-8')))

    # 关闭连接
    udp_socket.close()

def main():

    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    send_ip = ('127.0.0.1', 8083)

    send_msg = threading.Thread(target=send, args=(udp_socket, send_ip))
    recv_msg = threading.Thread(target=receive, args=(udp_socket,))

    send_msg.start()
    recv_msg.start()

   

if __name__ == "__main__":
    main()