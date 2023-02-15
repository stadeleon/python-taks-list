def parse(feet_inches):
    feet, inches = feet_inches.split(' ')
    # parts = feet_inches.split(' ')
    # feet = float(parts[0])
    # inches = float(parts[1])
    return {"feet": float(feet), "inches": float(inches)}


def confert(feet, inches):
    meeters = feet * 0.3048 + inches * 0.0254

    # return f"{feet} feet and {inches} inches is equal to {meeters} meeters"
    return meeters


# print(confert(feet_inches))
feet_inches = input("Enter feet and inches: ")
parsed = parse(feet_inches)
result = confert(parsed["feet"], parsed["inches"])
print (result)

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use slide.")

# def get_average():
#     with open('day1/files/data.txt') as file:
#         data = file.readlines()
#         values = data[1:]
#         values = [float(i) for i in values]
#
#         average = sum(values) / len(values)
#     return average
#
#
# average = get_average()
# print(average)

# try:
#     width = float(input("Enter rectangle width: "))
#     length = float(input("Enter rectangle length: "))
#
#     if width == length:
#         exit("That looks like a square!")
#
#     area = width * length
#     print(area)
# except ValueError:
#     print("The number should be entered")

# password = input('Enter a new password: ')
# result = {'isLengthOk': True, 'isDigit': False, 'isUpperCase': False}
#
# if not len(password) >= 8:
#     print('password is too short')
#     result['isLengthOk'] = True
#
# for symbol in password:
#     if (not result['isDigit']) & symbol.isdigit():
#         result['isDigit'] = True
#
#     if (not result['isUpperCase']) & symbol.isupper():
#         result['isUpperCase'] = True
#
# if not result['isDigit']:
#     print('Password should contain at least one digit')
#
# if not result['isUpperCase']:
#     print('Password should contain at least one Uppercase letter')
#
# print(result)
# print('Strong Password' if all(result.values()) else 'Weak Password')

# date = input("Enter today's date: ")
# mood = input("How do you rate your mood from 1 to 10? ")
# thoughts = input("Let your thoughts flow: \n")
#
# with open(f"..journal/{date}.txt", 'w') as file:
#     file.write(mood + 2 * '\n')
#     file.write(thoughts)


# filenames = ['1.doc', '1.report', '1.presentation']
# filenames = [filename.replace('.', '-') + '.txt' for filename in filenames]
# print(filenames)

# contents = ["content to file one",
#             "Contentto file 2",
#             "Content to file 3"]
# fileNames = ["doc.txt", "report.txt", "presentation.txt"]
#
# for content, fileName in zip(contents, fileNames):
#     file = open(f"files/{fileName}", 'w')
#     file.write(content)
#
# a = "I am a string " \
#     "on my " \
#     "own"
# waiting_list = ['sen', 'ben', 'john']
# waiting_list.sort(reverse=True)
#
# for index, item in enumerate(waiting_list):
#     row = f"{index+1}.{item.capitalize()}"
#     print(row)

# filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]
#
# for key, file in enumerate(filenames):
#     filenames[key] = file = file.replace('.', '-', 1)
#     print(file)
# print(filenames)

# # meals = ['pasta', 'pizza', 'salat']
# meals = 'some text'
#
# for meal in meals:
#     print(meal.capitalize())
#
# print("Bye")

# x = 1
# while x <= 6:
#     print(x)
#     x += 1

# text = ''
# while text != 'pass123':
#     text = input("Enter password:")
#
# print('password correct')
