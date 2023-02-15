class Waterflow:
    __solid_level = 0
    __gas_level = 100

    def __init__(self):
        return

    def get_water_state(self, temperature):
        if temperature <= self.__solid_level:
            result = 'Solid'
        elif temperature < self.__gas_level:
            result = 'Liquid'
        else:
            result = "Gas"

        return result
