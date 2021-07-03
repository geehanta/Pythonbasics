is_male= True
is_tall= False
if is_male and is_tall:  #try using and instead of or etc
    print("You are a male and tall")
elif is_male and not (is_tall):
    print("Youre kinda short")
else:
    print("Youre female and short")
