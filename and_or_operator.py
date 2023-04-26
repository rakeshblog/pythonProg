#check two condition at same time
#1: and operator
#2: or operator
_name = "Rakesh"
_age = 23
_check = input("enter you name : ")
_age_check = int(input("enter you age : "))
if _name == _check and _age == _age_check :
    print(f"Name : {_name} \n Age : {_age}")
else :
    print("Not equal Name or Age\nplease enter name and age equal")
