# Задача 3. Мониторинг серверов
# Создать класс Server.
# Поля:
# name
# cpu_usage
# ram_usage
# Метод:
# get_status()
# Логика:
# cpu < 70 и ram < 70
# => OK

# cpu > 70 или ram > 70
# => WARNING

# cpu > 90 или ram > 90
# => CRITICAL
# Пример
# server = Server(
#     "api-prod-1",
#     92,
#     40
# )

# print(server.get_status())
# Как в проде:
# DevOps, мониторинг, SRE. 


class Server:
    def __init__(self, name, cpu_usage, ram_usage):
        self.name = name
        self.cpu_usage = cpu_usage
        self.ram_usage = ram_usage
    
    def get_status(self):
        if self.cpu_usage > 90 or self.ram_usage > 90:
            return "Critical"
        elif self.cpu_usage > 70 or self.ram_usage > 70:
            return "Warning"
        else:
            return "OK"

server1 = Server("hah", 93, 56)
print(server1.get_status())