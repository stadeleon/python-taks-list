from day1.converters14 import convert
from day1.parsers14 import parse
# import parsers14

feet_inches = input("Enter feet and inches: ")
parsed = parse(feet_inches)
# parsed = parsers14.parse(feet_inches)
result = convert(parsed["feet"], parsed["inches"])
print(result)

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use slide.")
