class Server:
    __ip_counter = 0

    def __init__(self):
        Server.__ip_counter += 1
        self.__ip = Server.__ip_counter
        self.buffer = []
        self.connect = False

    def get_ip(self):
        return self.__ip

    def send_data(self, data):
        if self.connect:
            self.connect.add_buffer_router(data)
        else:
            print('Нет коннекта с роутером')

    def get_data(self):
        if self.buffer == []:
            return []
        response = []
        for data in self.buffer:
            response.append(data)
        self.buffer = []
        return response

    def add_buffer_server(self, data):
        self.buffer.append(data)

    def __str__(self):
        return f'IP: {self.get_ip()}'


class Router:

    def __init__(self):
        self.buffer = []
        self.connect_servers = {}

    def link_server(self, server):
        self.connect_servers[server.get_ip()] = server
        server.connect = self

    def unlink_server(self, server):
        del self.connect_servers[server.get_ip()]
        server.connect = False

    def send_data(self):
        if self.buffer:
            for data in self.buffer:
                if data.ip in self.connect_servers:
                    server = self.connect_servers[data.ip]
                    server.add_buffer_server(data)
            self.buffer = []
        else:
            print('Нет данных для отправки')

    def add_buffer_router(self, data):
        self.buffer.append(data)


class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip

    def __str__(self):
        return f'{self.data},{self.ip}'


if __name__ == '__main__':
    d1 = Data('1111111', 1)
    d2 = Data('2222222', 2)
    router = Router()
    serv1 = Server()
    serv2 = Server()
    router.link_server(serv1)
    serv1.send_data(d2)
    print(serv1)
    router.unlink_server(serv1)
    router.link_server(serv2)
    router.link_server(serv1)
    router.send_data()
    print(serv1.buffer)
    print(serv2.buffer)

    # d = Data('Hi', 2)
    # print(d)
