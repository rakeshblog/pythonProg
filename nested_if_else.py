#nested if else statement
_winning_number = 27
user_input = int(input("guess a number b/w 1 and 100 : "))
if user_input == _winning_number :
    print("you are winner!")
else:
    #print("you are not winner")
    if user_input < _winning_number :
        print("too low number")
    else:
        print("too high number")
