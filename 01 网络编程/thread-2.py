import threading
from time import sleep, ctime


def sing():
    for i in range(5):
        print('正在唱歌...{}'.format(i))
        sleep(1)


def dance():
    for i in range(5):
        print('正在跳舞...{}'.format(i))


if __name__ == '__main__':
    print('---开始---:{}'.format(ctime()))

    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)

    t1.start()
    t2.start()

    # sleep(8)

    print('---结束---:{}'.format(ctime()))
