import socket

def main():

    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    localAddress = ('', 8081)  # 本地ip端口号
    udp_socket.bind(localAddress)  # 绑定端口号

    # 接收数据
    while True:
        receive_data = udp_socket.recvfrom(1024) # 1024为接收数据的最大字节

        send_addr = receive_data[1]
        recev_msg = receive_data[0]

        print('%s: %s' % (str(send_addr), recev_msg.decode('utf-8')))

    # 关闭连接
    udp_socket.close()

if __name__ == "__main__":
    main()