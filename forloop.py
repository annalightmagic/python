colorlist = []
number = input("How many colors do you want to add: ")
number = int(number)
for i in range(number):
    name = input("Enter color: ")
    colorlist.append(name)
print(colorlist)