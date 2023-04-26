#string method 
#1:len() function
#2:lower() function
#3:upper() function
#4:title() function
#5:count() function
_name, char=input("type your name").split(",")
print(len(_name))
print(_name.lower())
print(_name.upper())
print(_name.title())
print(_name.count("r"))
print("exercise : ")
print(f"lenth of your name is {len(_name)}")
#_name.lower().count()
#char.lower()
#_name.lower().count(char.lower())
print(f"character count : {_name.lower().count(char.lower())}")

