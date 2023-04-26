#python 3.6 for format f"...{}{}"
_first_name="rakesh"
_last_name="kumar"
_full_name=f"Hello Mr.{_first_name} {_last_name}"
print(_full_name)
print(_full_name.title())
print(f"Hi' this is : {_first_name.title()} {_last_name}")
#python 3.5 format()method
_full_name1="{}{}".format(_first_name, _last_name)
print(_full_name1)

#print string value as multiple times
_nam="\nRakesh\n"
print(f"{_nam*5}")
#concatination + 
print("hello guys my name is :" + _first_name.title() + " " + _last_name)