class Car():
    def __init__(self, model, color):
        self.model = model
        self.color = color
        self.speed = 0

    def accelerate(self):
        self.speed += 10

    def brake(self):
        self.speed -= 10

    def get_speed(self):
        return self.speed


car1 = Car("벤츠", "검정")
print(car1.model)
print(car1.color)
print(car1.speed)

car1.accelerate()
car1.accelerate()
car1.brake()
print(car1.get_speed())
