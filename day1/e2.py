import webbrowser

user_term = input("Enter a search term: ").replace(' ', '+')
webbrowser.open("https://google.com/search?q=" + user_term)

# import shutil
# shutil.make_archive("output", "zip", "files")

# import csv
# with open('weather.csv') as file:
#     data = list(csv.reader(file))
#
# city = input("Enter a city: ")
#
# for row in data[1:]:
#     if row[0] == city:
#         print(row[1])
