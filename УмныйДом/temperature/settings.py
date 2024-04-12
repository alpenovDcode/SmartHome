'''
temperature/settings.py
Модуль для определения настроек температурного режима, например, минимальной
и максимальной температуры.
'''

class TemperatureSettings:
    def __int__(self):
        self.default_temp = 23

    def get_default_temp(self):
        return self.default_temp