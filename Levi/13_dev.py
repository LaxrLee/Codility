# if statements

is_male = False
is_alien = True

if is_male and is_alien:
    print("You are a male and an alien")
elif is_male and not (is_alien):
    print("You are male and not alien")
elif is_alien and not(is_male):
    print("You are alien but not male")
else:
    print("You are not male and not alien")