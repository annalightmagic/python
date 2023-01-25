#Create a citylist
citylist = ['Tokyo', 'Bangkok', 'Berlin', 'Chiang Mai', 'Chiang Rai']

#Traverse the city
for i in range(len(citylist)):
    print(citylist[i])

#Append the city
name = input("Add a new city: ")
citylist.append(name)

#Delete a city
delete = int(input("Which city do you want to delete?: "))
del citylist[delete]

#Print the citylist
print(citylist)