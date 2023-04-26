#strip_method use remove white spaces
_name = "   Rakesh kumar   "
_dots = ".........."
_name1="    Rakesh      Kumar   "
#for left remove whitespace = lstrip()
#for right remove whitespace =rstrip()
#for all white space means left and right remove spaces =strip()

print(_name + _dots)
print(_name.lstrip() + _dots)
print(_name.rstrip() + _dots)
print(_name.strip() + _dots)
print(_name1.replace(" ", "") + _dots)

#exercise3
_nam, _char = input("type you name , char").split(",")
print(f"length of your name is {len(_nam)}")
#Rakesh kumar
#R - r
#" Rakesh kumar    "--------> "Rakesh kumar"------>"rakesh kumar"
#"  R "-------->"R"--------->"r"
#1:_nam.strip().lower().count()
#2:_char.strip().lower()
#3:_nam.strip().lower().count(_char.strip().lower())
print(f"character count : {_nam.strip().lower().count(_char.strip().lower())}")