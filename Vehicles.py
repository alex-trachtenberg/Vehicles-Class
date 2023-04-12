from random import randint


class Wheel:
    def __init__(self, wheel_radius, set_air_press=-1):
        self.puncture = False
        self.radius = wheel_radius
        self.air_percentage = set_air_press if set_air_press != -1 else randint(85, 95)

    def inflate(self):
        self.air_percentage = 100


class Vehicle:
    def __init__(self, wheels_lst):
        self.wheels_list = wheels_lst
        self.driveable = self.set_driveable()

    def add_del_wheel(self, wheel_instance, add_del_value):
        if not add_del_value:
            self.wheels_list.remove(wheel_instance)
        else:
            self.wheels_list.append(wheel_instance)
        self.driveable = self.set_driveable()

    def drive(self, dist):
        if self.driveable:
            for w in self.wheels_list:
                w.air_percentage -= dist
            self.driveable = self.set_driveable()
        else:
            print("Vehicle is not drivable! Fix problems and then try again")

    def set_driveable(self):
        is_driveable = True
        if self.wheels_list is not None:
            first_wheel_radius = self.wheels_list[0].radius
            for w in self.wheels_list:
                if (w.radius != first_wheel_radius) or (w.air_percentage <= 60) or w.puncture:
                    is_driveable = False
                    break
        return is_driveable


if __name__ == '__main__':
    Wh1 = Wheel(28, 75)
    Wh2 = Wheel(28)
    Veh1 = Vehicle([Wh1, Wh2])
    Wh3 = Wheel(28)
    Wh4 = Wheel(28, 70)
    Veh1.add_del_wheel(Wh3, True)
    Veh1.add_del_wheel(Wh4, True)
    Veh1.drive(20)
