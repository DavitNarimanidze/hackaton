# 16 "შექმენით number guess თამაში. description: შექმენით ცვლადი და მიანიჭეთ რაიმე int მნიშვნელობა. შექმენით მეორე ცვლადი რომელშიც მომხმარებელს შემოატანინებთ რაიმე რიცხვს. სანამ არ გამოიცნობს რა რიცხვი იყო პირველ ცვლადში, დაუწერეთ: ""Try again"" თუ გამოიცნობს მაშინ: ""Congrats. You guessed the number"". (გამოიყენეთ while loop'ი)"

												

secret_number = '7'
user_number = ''

tries = 3

while tries > 0 and user_number != secret_number:
    user_number = input('Enter number (you have ' + str(tries) + 'tries left: ')

    tries -= 1

    if user_number == secret_number:
        print('Access Granted.')
    elif tries == 0:
        print("you dont have any tries :(")
    else:
        print('Access Denied, try again  ')