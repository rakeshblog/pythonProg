#replace() and find() method
_string="he is a best writter and he is good learnner"
print(_string.replace(" ", "_"))
print(_string.replace(" ", "_", 2))
print(_string.replace("is", "was", 1))

_str="my name is rakesh kumar and this is a good singer"
print(_str.find("is"))
print(_str.find("is", 31))
#variable + 1 type find method
_is_first=_str.find("is")
print(_str.find("is", _is_first + 1))