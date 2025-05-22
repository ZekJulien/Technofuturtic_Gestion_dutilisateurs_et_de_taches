import os
import time

class Tools:

    @staticmethod
    def sleep(tps : int):
        time.sleep(tps)

    @staticmethod
    def clearConsole():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def input_numeric_int(input_message : str, error_message : str, optional_condition=None) -> int:
        while True:
            number = input(input_message)
            if number.isnumeric() and (optional_condition(number) if optional_condition is not None else True):
                return int(number)
            else : 
                Tools.clearConsole()
                print(error_message)

    @staticmethod
    def input_ui_str(input_message : str, optional_condition=None) -> str:
        input_str = input(input_message)
        if input_str != "" and (optional_condition(str) if optional_condition is not None else True):
            return input_str
        else: 
            return None

    