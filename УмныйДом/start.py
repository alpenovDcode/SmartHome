'''
Умный дом
Включение света в определенной комнате через интерфейс управления освещением.
Автоматическое регулирование температуры в зависимости от времени суток.
Мониторинг системы безопасности и оповещения при обнаружении движения.

Структура проекта
lighting: пакет для управления освещением
control.py: модуль с классами и функциями для включения и выключения света
settings.py: модуль для хранения настроек освещения, таких как интенсивность и режимы

temperature: пакет для контроля температуры
thermostat.py: модуль для регулировки и контроля температуры
settings.py: модуль для установки желаемых температурных параметров

security: пакет для системы безопасности
surveillance.py: модуль для управления камерами наблюдения и другими устройствами безопасности
alarm.py: модуль для настройки и активации сигнализации


Описание модулей

lighting/control.py
Классы для управления различными типами осветительных приборов.
Методы включают в себя включение/выключение, регулировку яркости.

lighting/settings.py
Хранение настроек света, таких как режимы дневного или ночного света.

temperature/thermostat.py
Классы для контроля температуры в помещениях.
Включает функции для установки температуры и автоматической регулировки.

temperature/settings.py
Модуль для определения настроек температурного режима, например, минимальной
и максимальной температуры.

security/surveillance.py
Управление системами видеонаблюдения, включая включение/выключение
и регулирование углов обзора камер.

security/alarm.py
Настройки и активация системы сигнализации, включая условия для срабатывания тревоги.

start.py
Интерфейс для управления освещением
Интерфейс для контроля температуры
Интерфейс для управления системой безопасности
Простой текстовый интерфейс для взаимодействия с пользователем
'''

from lighting.control import Light
from lighting.settings import LightSettings
from temperature.thermostat import Thermostat
from temperature.settings import TemperatureSettings
from security.surveillance import Camera
from security.alarm import AlarmSystem


def display_room(lights, thermostat, camera, alarm):
    room = f"""
    {'🔴' if alarm.is_armed else '🔵'} Alarm System: {'Armed' if alarm.is_armed else 'Disarmed'}
    🌡️ Thermostat: {thermostat.current_temp}°C (Set: {thermostat.desired_temp}°C)
    🎥 Front Door Camera: {'On' if camera.is_on else 'Off'}

    -----------------------------
    |    {'💡' if lights['living room'].is_on else '🌑'} Living Room      {'💡' if lights['kitchen'].is_on else '🌑'} Kitchen    |
    -----------------------------
    """
    print(room)


def main():
    living_room_light = Light("living room")
    kitchen_light = Light("kitchen")
    lights = {"living room": living_room_light, "kitchen": kitchen_light}
    thermostat = Thermostat()
    front_door_camera = Camera("front door")
    home_alarm = AlarmSystem()

    while True:
        display_room(lights, thermostat, front_door_camera, home_alarm)
        print("\nSmart Home System")
        print("1. Lighting")
        print("2. Temperature")
        print("3. Security")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            # Lighting control
            print("\nLighting Control")
            print("1. Turn on Living Room Light")
            print("2. Turn off Living Room Light")
            print("3. Turn on Kitchen Light")
            print("4. Turn off Kitchen Light")
            lighting_choice = input("Choose an option: ")
            if lighting_choice == '1':
                living_room_light.switch_on()
            elif lighting_choice == '2':
                living_room_light.switch_off()
            elif lighting_choice == '3':
                kitchen_light.switch_on()
            elif lighting_choice == '4':
                kitchen_light.switch_off()

        elif choice == '2':
            # Temperature control
            print("\nTemperature Control")
            temp = int(input("Set desired temperature (°C): "))
            thermostat.set_temperature(temp)

        elif choice == '3':
            # Security control
            print("\nSecurity System")
            print("1. Arm Alarm")
            print("2. Disarm Alarm")
            print("3. Turn on Camera")
            print("4. Turn off Camera")
            security_choice = input("Choose an option: ")
            if security_choice == '1':
                home_alarm.arm()
            elif security_choice == '2':
                home_alarm.disarm()
            elif security_choice == '3':
                front_door_camera.turn_on()
            elif security_choice == '4':
                front_door_camera.turn_off()

        elif choice == '4':
            print("Exiting Smart Home System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
