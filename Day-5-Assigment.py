import random

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '=', '-', '?']

while True:
    number = int(input("Enter the number of digits in your password: "))
    character =  int(input("Enter the number of letters in your password: "))
    special_character = int(input("sinter the number of special characters in your password: "))

    empty_list1 =[]
    for i in range(number):
        num = random.choice(numbers)
        empty_list1.append(num)

    #Add Random letters
    for i in range(character):
        alb = random.choice(alphabet)
        empty_list1.append(alb)

    #Add random special characters
    for i in range(character):
        alb = random.choice(alphabet)
        empty_list1.append(alb)

    #Shuffle the final password list
    random.shuffle(empty_list1)

    #Join the list into a single string
    final_password  ="".join(empty_list1)

    print("Your generated password is:",final_password)

    Check = input("Do you want to generate another password? (yes/no): ").lower()

    if Check!="yes":

        print("Thank you for using the password generator!")
        break