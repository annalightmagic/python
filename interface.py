#program interface should have all of these:
#1. Tell the user what the program is and what it can do
#2. Tell the user make choices or select option
#3. Let the user enter information - you should include a helpful message and validation
#4. Display result or answer
#5. Let the user close the program

teamlist = []
choice = ''
while choice != 'X':
    print("TEAM MANANGER")
    print("=============")
    print("This program will help you manage your team")
    print("\n")
    print("A: Append a value")
    print("B: Print the team list")
    print("X: Exit the program")
    choice = input("Choose: ")
    if choice == "A":
        name = input("Enter a name: ")
        teamlist.append(name)
print(teamlist)
