class Vehicle:
    vehicle_type = "none"


class Car:
    price = 1000000
    hp = 500

    def horse_powers(self):
        return 'Мощность: {}'.format(self.hp)


class Nissan(Car, Vehicle):
    price = 500000
    vehicle_type = "Легковой автомобиль"

    def __str__(self):
        return f'Я автомобиль {self.__class__.__name__}, моя цена: {self.price}, мой тип: {self.vehicle_type}'

    def horse_powers(self):
        print('Мощность: 250 л.с.')


car = Nissan()
print(car)
car.horse_powers()
