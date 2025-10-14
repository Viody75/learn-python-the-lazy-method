# === Practices for Ding Dong ===
# Refer to SoalPraktikum1.pdf for the questions.
# Each function corresponds to a specific practice question.
# Comment out the function calls to run specific practices.

# 1.a.
def practices_1a():
    userName = input("Masukan nama Anda: ")
    print(f"Hi, {userName}!")

# Run it
# practices_1a()

# 1.b.
def practices_1b():
    print("What do you call a bear with no teeth?\nA gummy bear!")

# Run it
# practices_1b()

# 2.a.
def practices_2a():
    userInput = input("Choose between 1, 2, or 3: ")
    if userInput == "1":
        print("Thank you")
    elif userInput == "2":
        print("Well done")
    elif userInput == "3":
        print("Correct")
    else:
        print("Error: Invalid choice")

# Run it
# practices_2a()

# 2.b.
def practices_2b():
    try:
        userNumber = int(input("Enter a number: "))
        if 10 < userNumber < 20:
            print("Thank you")
        else:
            print("Incorrect answer")
    except ValueError:
        print("Error: Please enter a valid integer")

# Run it
# practices_2b()

# 3.a.
def practices_3a():
    again = "yes"
    while again == "yes":
        print("Hello")
        userConfirm = input("Do you want to loop again? (yes/no): ")
        if userConfirm.lower() == "yes":
            again = "yes"
        elif userConfirm.lower() == "no":
            again = "no"
        else:
            print("Error: Invalid input, will be treated as no.")
            again = "no"
# Run it
# practices_3a()

# 3.b.
def practices_3b():
    num = 10
    print(f"There are {num} green bottles hanging on the wall, {num} green bottles hanging on the wall, and if 1 green bottle should accidentally fall")
    while num > 0:
        userAnswer = input("How many green bottles will be hanging on the wall? ")
        try:
            userAnswerInt = int(userAnswer)
            if userAnswerInt == num - 1:
                num -= 1
                if num > 0:
                    print(f"There will be {num} green bottles hanging on the wall, and if 1 green bottle should accidentally fall.\n")
                else:
                    print("There are no more green bottles hanging on the wall.\n")
            else:
                print("No, try again\n")
        except ValueError:
            print("Error: Please enter a valid integer\n")

# Run it
# practices_3b()

# 5.a.
def practices_5a():
    subjects = ["Math", "Science", "History", "Art", "Physical Education", "Music"]
    print("Subjects:", subjects)
    dislike = input("Which subject do you dislike? ")
    if dislike in subjects:
        subjects.remove(dislike)
        print("Updated subjects:", subjects)
    else:
        print("Error: Subject not found in the list.")

# Run it
# practices_5a()

# 5.b.
def practices_5b():
    grid = [
        [2, 5, 8],
        [3, 7, 4],
        [1, 6, 9],
        [4, 2, 0]
    ]
    print("Grid:")
    for row in grid:
        print(row)

# Run it
# practices_5b()

# 5.c.
def practices_5c():
    sales_data = {
        "John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
        "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
        "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
        "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451},
    }
    
    print("\nSales Data for all regions:")
    for person, regions in sales_data.items():
        print(f"{person}: {regions}")
    print("\n")

    print("Update Sales Data")
    name = input("Enter the salesperson's name: ")
    region = input("Enter the region (North/South/East/West): ")

    if name in sales_data and region in sales_data[name]:
        print(f"{name}'s sales in {region}: {sales_data[name][region]}")
    else:
        print("Error: Name or region not found.")
    
    try:
        new_sales = int(input("Enter the new sales figure / value: "))
        if name in sales_data and region in sales_data[name]:
            sales_data[name][region] = new_sales
            print(f"Updated sales for {name} in {region}: {sales_data[name][region]}")
            print("\nUpdated Sales Data for all regions:")
            for person, regions in sales_data.items():
                print(f"{person}: {regions}")
            print("\n")
        else:
            print("Error: Name or region not found.")
    except ValueError:
        print("Error: Please enter a valid integer for sales.")

# Run it
# practices_5c()

# 6.a.
def practices_6a():
    with open("Names.txt", "w") as file:
        for i in range(5):
            name = input(f"Enter name {i+1}: ")
            file.write(name + "\n")
    print("Names saved to Names.txt")

# Run it
# practices_6a()

# 7.a.
def practices_7a():
    def get_number():
        while True:
            try:
                num = int(input("Enter a number: "))
                return num
            except ValueError:
                print("Error: Please enter a valid integer.")

    def count_to_number(num):
        for i in range(1, num + 1):
            print(i)

    number = get_number()
    count_to_number(number)

# Run it
# practices_7a()

