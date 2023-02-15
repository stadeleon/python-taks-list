def parse(feet_inches):
    feet, inches = feet_inches.split(' ')
    # parts = feet_inches.split(' ')
    # feet = float(parts[0])
    # inches = float(parts[1])
    return {"feet": float(feet), "inches": float(inches)}
