'''

lighting/control.py
Классы для управления различными типами осветительных приборов.
Методы включают в себя включение/выключение, регулировку яркости.

'''

class Light:
    def __init__(self, location, brightness=0, is_on=False):
        self.location = location
        self.brightness = brightness
        self.is_on = is_on

    def switch_on(self):
        self.is_on = True
        self.change_brightness(50)

    def switch_off(self):
        self.is_on = False
        self.brightness = 0

    def change_brightness(self, level):
        if not self.is_on:
            print("Light is off, turn in on first.")
        else:
            self.brightness = level
            print(f"Brightness set to {level}% at {self.location}.")
