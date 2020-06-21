class Car:
    def __init__(self):
        self.speed = 0
        self.odometer = 0
        self.time = 0

    def say_state(self):
        print("I'm going {} mph!".format(self.speed))

    def accelerate(self):
        self.speed += 5

    def brake(self):
        if self.speed < 5:
            self.speed = 0
        else:
            self.speed -= 5

    def step(self):
        self.odometer += self.speed
        self.time += 1

    def average_speed(self):
        if self.time != 0:
            return self.odometer / self.time


if __name__ == '__main__':
    my_car = Car()
    print("I'm a car!")
    while True:
        action = input("What should i do? [A]ccelerate, [B]rake, " "show [O]dometer, or show average [S]peed?").upper()
        if action not in "ABOS" or len(action) != 1:
            print("You did not choose A, B, O, or S. Please select again")
            continue
        if action == 'A':
            my_car.accelerate()
        elif action == 'B':
            my_car.brake()
        elif action == 'O':
            print("The car has driven {} miles.".format(my_car.odometer))
        elif action == 'S':
            print("The car's average speed was {} mph".format(my_car.average_speed))
        my_car.step()
        my_car.say_state()
