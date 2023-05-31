class Vehicle():
    def __init__(self, brand, model, speed, year) -> None:
        self.brand = brand
        self.model = model
        self.speed = speed
        self.year = year

    def high_speed(self, speed):
        self.speed += speed

    def low_speed(self, speed):
        self.speed -= speed


class Motorcicle(Vehicle):
    def __init__(self, brand, model, speed, year, motor) -> None:
        # Con super podemos actualizar los atributos de la clase madre
        super().__init__(brand, model, speed, year)
        self.motor = motor

    # Hacer caballito
    def wheelie(self):
        return "Haciendo el wheelie..."


class Bus(Vehicle):
    def __init__(self, brand, model, speed, year, seatings = 0) -> None:
        super().__init__(brand, model, speed, year)
        self.seatings = seatings

    def charge_passengers(self, passengers = 0):
        return f"We have { passengers } passengers"


motocicleta = Motorcicle("Honda", 2023, 150, 2024, 1.5)

print(motocicleta.brand)
print(motocicleta.wheelie())

autobus = Bus("Mercedez",2020,100,2022)

print(autobus.seatings)
print(autobus.charge_passengers(1000))