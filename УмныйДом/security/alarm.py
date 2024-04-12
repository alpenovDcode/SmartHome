'''

security/alarm.py
Настройки и активация системы сигнализации, включая условия для срабатывания тревоги.

'''

class AlarmSystem:
    def __init__(self):
        self.is_armed = False

    def arm(self):
        self.is_armed = True
        print("Alarm system is armed.")

    def disarm(self):
        self.is_armed = False
        print("Alarm system is disarmed.")
