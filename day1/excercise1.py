
names = input("enter the names separated by commas: ")
names_list = names.split(' ')
print(len(names_list))

# def get_years(birth_year, current_year=2023):
#     return current_year - birth_year
#
#
# year = int(input('Enter a year of birth: '))
# age = get_years(year)
# print(age if age < 120 else f"Its awesome, you are {age}!!")

# # Exercise 10
# try:
#     totalValue = float(input('Enter total value: '))
#     value = float(input('Enter value: '))
#
#     percent = value / (totalValue / 100)
#     print(f"That is {percent}%")
# except ValueError:
#     print('Input only numbers')
# except ZeroDivisionError:
#     print('total value should be differ than zero')

# # Exercise 9
# password = input('Enter a new password: ')
# if len(password) > 7:
#     message = "Great password there!"
# elif len(password) == 7:
#     message = "Password is OK, but not too strong"
# else:
#     message = 'Your password is weak'
#
# print(message)


# Exercise 8
# filename = '../files/coin.txt'
# while True:
#     with open(filename) as file:
#         probabilityList = file.readlines()
#
#     side = input("Throw the coin and enter 'head' or 'tail' here: ?") + '\n'
#     if side == 'exit\n':
#         break
#     elif side not in ['head\n', 'tail\n']:
#         continue
#
#     probabilityList.append(side)
#     with open(filename, 'w') as file:
#         file.writelines(probabilityList)
#
#     heads = probabilityList.count('head\n')
#     tails = probabilityList.count('tail\n')
#     print(f"Heads: {heads / ((heads + tails) if (heads + tails) > 0 else 1) * 100}%")
#     print('Type \'exit\' to stop script')
# print('Good Bye!')

# with open('../files/doc.txt') as file:
#     # print(file.read())
#     content = file.read()

# user_entries = ['10', '19.1', '20']
# print(sum([float(number) for number in user_entries]))

# user_entries = ['10', '19.1', '20']
# print([float(item) for item in user_entries])

# usernames = ["john 1990", "alberta1970", "magnola2000"]
# print([len(username) for username in usernames])

# names = ["john smith", "jay santi", "eva kuki"]
# print([name.title() for name in names])

# txtFileNames = ['a', 'b', 'c']
#
# for filName in txtFileNames:
#     file = open(f"../files/{filName}.txt", 'r')
#     print(file.read())

# fileNames = ['fileOne.txt', 'fileTwo.txt']
# message = 'Hello'
#
# for fileName in fileNames:
#     file = open(f"../files/{fileName}", 'w')
#     file.write(message)
#     file.close()

# file = open("../files/members.txt", 'r')
# contents = file.readlines()
# file.close()
# contents.append(input('Add a new member: ').title() + '\n')
#
# print(contents)
#
# file = open("../files/members.txt", 'w')
# file.writelines(contents)
# # for line in contents:
# #     file.writelines(f'{line.title()}')
# # file.write(f'\n{name.title()}')
# file.close()


# file = open('../files/essay.txt', 'r')
# contents = file.readlines()
# file.close()
# length = 0
# for line in contents:
#     print(line.title() + '\n')
#     length += len(line)
#
# print(length)


# ips = ['100.122.133.105', '100.122.133.111']
#
# num = int(input('Enter the index (0, 1)'))
# print(ips[num])


# filenames = ['document', 'report', 'presentation']
#
# for key, val in enumerate(filenames):
#     print(f"{key}-{val.capitalize()}.txt")

# ranking = ['John', 'Sen', 'Lisa']
#
# # place = input('Enter the rank')
# # print(ranking[int(place)-1])
# print(ranking)
# name = input('Enter the name: ')
# print(ranking.index(name)+1)

# sum = int(input('Input how much bucks you have: '))
# euros = sum * 0.95
# print('It will be %s Euros' % (sum * 0.95))


# ingredients = ["john smith", "sen plakay", "dora ngacely"]
#
# for item in ingredients:
#     print(item.title())

# country = input('Enter your country: ')
#
# match country:
#     case 'USA':
#         message = 'Hello'
#     case 'India':
#         message = 'Namaste'
#     case 'Germany':
#         message = 'Hallo'
#     case _:
#         message = 'WTF'
# print(message)

# countries = []
# country = input("Enter the country: ")
# while country:
#     countries.append(country)
#     print(countries)
#     country = input("Enter the country: ")

# name = input("Enter some name: ")
# print("Entered name is ", name)
# var1, var2, var3 = input(), input(), input()
# list1 = [var1, var2, var3]
# print(list1)
# print(type(list1))


# user_prompt = "Enter a todo:"
# val = 1
# todo = []
# while val:
#     val = input(user_prompt)
#     print(val.title())
#     todo.append(val.capitalize()) if val else 0
#
# print(todo)
