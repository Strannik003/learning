# Задача 2. Система промокодов
# Создать класс PromoCode.
# Поля:
# code
# discount
# max_uses
# used_count
# Методы:
# apply()
# is_active()
# Логика:
# После достижения лимита промокод автоматически перестает работать.
# Пример
# promo = PromoCode(
#     "SUMMER25",
#     25,
#     3
# )

# promo.apply()
# promo.apply()
# promo.apply()

# print(promo.is_active())
# Что интересно:
# Объект хранит свое состояние.
# Как в проде:
# Маркетплейсы, онлайн-магазины, SaaS.


class PromoCode:
    def init(self, code, discount, max_uses, used_count = 0):
        self.code = code
        self.discount = discount
        self.max_uses = max_uses
        self.used_count = used_count

    def apply(self):
        if self.is_active():
            self.used_count += 1
            return True
        else:
            return False

    def is_active(self):
        return self.used_count < self.max_uses
    
    
    def str(self):
        return f"PromoCode(code={self.code}, discount={self.discount}%, used={self.used_count}/{self.max_uses}"


promo1 = PromoCode(1,15,5)
print(promo1.apply())
print(promo1.apply())
print(promo1.apply())
print(promo1.apply())
print(promo1.apply())
print(promo1)