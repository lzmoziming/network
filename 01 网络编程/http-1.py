import re
import socket
import multiprocessing


def service_client(new_socket):
    request = new_socket.recv(1024).decode('utf-8')
    # print(">>>>>>>>>>>>>"*2)
    # print(request)

    request_line = request.splitlines()
    print("")
    print(request_line)
    print("*" * 50)

    ret = re.match(r"[^/]+(/[^ ]*)", request_line[0])
    print(ret.group())
    if ret:
        file_name = ret.group(1)
        # print("*" * 50, file_name)
        if file_name == "/":
            file_name = "/index.html"

    try:
        f = open('./html' + file_name, 'rb')
    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "\r\n"
        response += "<h>没有你要的页面</h1>"
        new_socket.send(response.encode("utf-8"))

    else:
        html_content = f.read()
        f.close()
        response = "HTTP/1.1 200 OK\r\n"
        response += "\r\n"
        # response += "<h1>hahahaha</h1>"
        new_socket.send(response.encode("utf-8"))
        new_socket.send(html_content)

    new_socket.close()


def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcp_server_socket.bind(('', 8888))

    tcp_server_socket.listen()

    while True:
        new_socket, client_addr = tcp_server_socket.accept()

        p = multiprocessing.Process(target=service_client, args=(new_socket,))
        p.start()
        new_socket.close()
        # service_client(new_socket)

    tcp_server_socket.close()


if __name__ == '__main__':
    main()
