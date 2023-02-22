class Vehicle():
    def __init__(self, cost, colour, mark):
        self.cost = cost
        self.colour = colour
        self.mark = mark

    def __str__(self):
        return f'Your choice is {self.mark} and the colour is {self.colour}\nIt cost {self.cost} '

    def __repr__(self):
        return f'Vehicle(\'{self.mark}\', {self.colour}, {self.cost}'


class Moto(Vehicle):

    def __init__(self, cost, colour, mark, speed):
        super().__init__(cost, colour, mark)
        self.speed = speed
        print("Maximum speed of this moto is", self.speed)


class Auto(Vehicle):


    def __init__(self, cost, colour, mark, type, seats):
        super().__init__(cost, colour, mark)
        self.type = type
        self.seats = seats
        print("Type of this car is", self.type)
        print("The number of seats is", self.seats)


class Boat(Vehicle):

    def __init__(self, cost, colour, mark, speed, type ):
        super().__init__(cost, colour, mark)
        self.speed = speed
        self.type = type
        print("Maximum speed of this boat is", self.speed)
        print("Type of this boat is", self.type)




