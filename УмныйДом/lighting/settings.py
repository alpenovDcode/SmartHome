'''
lighting/settings.py
Хранение настроек света, таких как режимы дневного или ночного света.
'''
class LightSettings:
    def __int__(self):
        self.modes = {'day': 80, 'night': 20}

    def get_mode_settings(self, mode):
        return self.modes.get(mode, 0)