'''
temperature/thermostat.py
Классы для контроля температуры в помещениях.
Включает функции для установки температуры и автоматической регулировки.
'''

class Thermostat:
    def __int__(self, desired_temp=23):
        self.current_temp = 20
        self.desired_temp = desired_temp

    def set_temperature(self, temperature):
        self.desired_temp = temperature
        print(f"Desired temperature set to {temperature}`C")

    def update_temperature(self):
        if self.current_temp < self.desired_temp:
            self.current_temp += 1
        elif self.current_temp > self.desired_temp:
            self.current_temp -= 1
        print(f"Current temperature is now {self.current_temp}`C")
