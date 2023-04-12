import os
from time import *
from random import randint

# Menu list
menu = ("Drive vehicle", "Add wheel to vehicle", "Remove wheel from vehicle", "Inflate wheel",
        "Puncture wheel", "Repair punctured wheel", "Quit")


# clear the terminal screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


class Wheel:
    existing_wheels_count = 0

    def __init__(self, wheel_radius, set_air_press=-1):
        Wheel.existing_wheels_count += 1
        self.puncture = False
        self.radius = wheel_radius
        self.air_percentage = set_air_press if set_air_press != -1 else randint(85, 95)

    def inflate(self):
        self.air_percentage = 100


class Vehicle:
    def __init__(self, wheels_lst=[]):
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
            print(f"Vehicle driven successfully {dist} KM!")
        else:
            if len(self.wheels_list) == 0:
                print("Vehicle is not drivable! Vehicle can't drive without wheels!")
            elif len(self.wheels_list) % 2 != 0:
                print(f"Vehicle is not drivable!! {len(self.wheels_list)} is an illegal number of wheels!")
            else:
                print("Vehicle is not drivable! Fix problems and try again.")

    def set_driveable(self):
        is_driveable = True
        if (len(self.wheels_list) != 0) and (len(self.wheels_list) % 2 == 0):
            first_wheel_radius = self.wheels_list[0].radius
            for w in self.wheels_list:
                if (w.radius != first_wheel_radius) or (w.air_percentage <= 60) or w.puncture:
                    is_driveable = False
                    break
        else:
            is_driveable = False
        return is_driveable


if __name__ == '__main__':
    veh = Vehicle()
    while True:
        clear()
        i = 1
        print("You are the proud owner of a vehicle!")
        for m in menu:
            print(f"{i}) {m}")
            i = i + 1
        ch = input("What do you want to do? Please enter your choice: ")

        match ch:
            case '1':
                driving_dist = int(input("Please enter desired driving distance: "))
                veh.drive(driving_dist)
                sleep(2)
            case '2':
                input_wheel_radius = int(input("Please enter desired wheel radius: "))
                veh.add_del_wheel(Wheel(input_wheel_radius), True)
                print("Wheel was successfully added!")
                sleep(2)
            case '3':
                tmp_wheel = int(input("Please enter No. of wheel to remove from vehicle: "))
                if len(veh.wheels_list) != 0:
                    if tmp_wheel <= len(veh.wheels_list):
                        veh.add_del_wheel(veh.wheels_list[(tmp_wheel - 1)], False)
                        print(f"Wheel No. {tmp_wheel} was successfully removed!")
                    else:
                        print(f"Error! Wheel No. {tmp_wheel} doesn't exist!")
                else:
                    print("Error! There are no wheels at all!")
                sleep(2)
            case '4':
                tmp_wheel = int(input("Please enter No. of wheel to inflate: "))
                if len(veh.wheels_list) != 0:
                    if tmp_wheel <= len(veh.wheels_list):
                        veh.wheels_list[(tmp_wheel - 1)].inflate()
                        print(f"Wheel No. {tmp_wheel} was inflated!")
                    else:
                        print(f"Error! Wheel No. {tmp_wheel} doesn't exist!")
                else:
                    print("Error! There are no wheels at all!")
                veh.driveable = veh.set_driveable()
                sleep(2)
            case '5':
                tmp_wheel = int(input("Please enter No. of wheel to puncture: "))
                if len(veh.wheels_list) != 0:
                    if tmp_wheel <= len(veh.wheels_list):
                        veh.wheels_list[(tmp_wheel - 1)].puncture = True
                        print(f"Wheel No. {tmp_wheel} was punctured!")
                    else:
                        print(f"Error! Wheel No. {tmp_wheel} doesn't exist!")
                else:
                    print("Error! There are no wheels at all!")
                veh.driveable = veh.set_driveable()
                sleep(2)
            case '6':
                tmp_wheel = int(input("Please enter No. of punctured wheel to repair: "))
                if len(veh.wheels_list) != 0:
                    if tmp_wheel <= len(veh.wheels_list):
                        veh.wheels_list[(tmp_wheel - 1)].puncture = False
                        print(f"Wheel No. {tmp_wheel} was successfully repaired!")
                    else:
                        print(f"Error! Wheel No. {tmp_wheel} doesn't exist!")
                else:
                    print("Error! There are no wheels at all!")
                veh.driveable = veh.set_driveable()
                sleep(2)
            case '7':
                clear()
                print("Goodbye!")
                break
            case _:
                clear()
                print("Wrong input!")
                sleep(2)
