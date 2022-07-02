class A(object):
    def __init__(self):
        self.name='dsa'

    def fun(self):
        print('A')

class B(A):
    def __init__(self):
        super().__init__()
        print(self.name+"init")
        self.fun()

#b=B()
#print(b.name)
#b.fun()


from socket import  *

class TCP_Server():

    #创建TCP服务模型
    def __init__(self):
        self.__sockfd=socket(AF_INET,SOCK_STREAM)


    @property
    def sockfd(self):
        return  self.__sockfd

    def __prepare(self):
        #绑定IP，设置监听队列
        self.__sockfd.bind('0.0.0.0',12120)
        self.__sockfd.listen(5)

    def prepare(self):
        self.__prepare()

    def __connects(self):
        while True:
            print("等待连接建立......")
            print()
            try:
                connfd,addr=self.__sockfd.accept()
            except Exception as e:
                print("连接建立失败！尝试重新建立连接")
                pass

            while True:
                data=connfd.recv(1024)#一次最多收1024字节  此时的data是字节流
                if not data:#判断接收的消息是否为空
                    break
                print('收到来自IP地址为：{}客户端发来的数据{}'.format(addr[0],data.decode()))
                n=connfd.send('receive your message'.encode())#编码后才能发送
                print('本次向客户端发送了{}字节的数据'.format(n))

            connfd.close()#先关闭客户端
        # 再关闭服务端套接字
        self.__sockfd.close()

    def connect(self):
        self.__connects()

def test():
    # 创建服务端TCP套接字对象
    server_socket = TCP_Server()
    # 连接准备工作执行
    server_socket.prepare()
    # 开始连接，并完成通信
    server_socket.connects()

if __name__ == '__main__':
    test()