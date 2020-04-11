from socket import *


def send_msg(udp_socket):
    msg = input('\n请输入要发送的数据：')
    dest_ip = input('\n请输入对方的IP地址')
    dest_port = input('\n请输入对方的端口：')
    udp_socket.sendto(msg.encode('utf-8'), (dest_ip, dest_port))


def recv_msg(udp_socket):
    recv_msg1 = udp_socket.recvfrom(1024)
    recv_ip = recv_msg1[1]
    recv_msg1                 



def main():
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    udp_socket.bind(('', 7777))
    while True:
        print('=' * 30)
        print('1:发送消息：')
        print('2:接受消息：')
        print('=' * 30)
        op_num = input('请输入要操作的功能序号：')

        if op_num == '1':
            send_msg(udp_socket)
        elif op_num == '2':
            recv_msg(udp_socket)
        else:
            print('输入有误，请重新输入...')


if __name__ == '__main__':
    main()
