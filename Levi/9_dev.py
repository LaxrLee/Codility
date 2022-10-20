# lists
from typing import ItemsView
from xml.dom.minidom import Element


friends = ["Kev", "Lol", "Jim"]
print(friends[1][1])
print(friends[1:])

# list functions
lucky_numbers = [4, 8, 15, 16 , 23, 42]
friend = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
# friend.extend(lucky_numbers) # adds two lists together
print(friend)

# adds individusal Items 
friend.append("Creed")
print(friend)

# add at a different position
friend.insert(1, "Kelly")
print(friend)

# Remove and Element
friend.remove("Jim")
print(friend)

print(friend.index("Kevin"))

friend.sort()  # reverse() is the opposite
print(friend)