'''
security/surveillance.py
Управление системами видеонаблюдения, включая включение/выключение
и регулирование углов обзора камер.
'''


class Camera:
    def __init__(self, location):
        self.location = location
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print(f"Camera at {self.location} is now on.")

    def turn_off(self):
        self.is_on = False
        print(f"Camera at {self.location} is now off.")
