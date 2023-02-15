SOLID_LEVEL = 0
GAS_LEVEL = 100


def get_water_state(temperature):
    if temperature <= SOLID_LEVEL:
        result = 'Solid'
    elif temperature < GAS_LEVEL:
        result = 'Liquid'
    else:
        result = "Gas"

    return result
