# Задача 4. Ролевая модель API
# Очень жизненная задача.
# Есть базовый класс:
# User
# Поля:
# name
# Метод:
# access_level()
 
# ⸻
 
# Наследники:
# Viewer
# Editor
# Admin
# Каждый возвращает свой уровень доступа.
# Дополнительно реализовать:
# can_delete()
# Только Admin должен возвращать:
# True
# Все остальные:
# False
# Как в проде:
# Практически любой backend.

class User:
    def __init__(self, name):
        self.name = name
        
    def can_delete(self):
        return False
    
    def access_level(self):
        return "base user"

class Viewer(User):
    def access_level(self):
        return "Viewer"

class Editor(Viewer):
    def access_level(self):
        return "Editor"

class Admin(Editor):
    def can_delete(self):
        return True
    
    def access_level(self):
        return "Admin"

Viewer1 = Viewer("Anton")
print(Viewer1.can_delete())

Admin1=Admin("Alex")
print(Admin1.can_delete())
print(Admin1.access_level())