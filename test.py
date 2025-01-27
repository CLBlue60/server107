print("Wake Up This World")

#variables

name = "Blue"
last_name = "X"
age = 31
woke = True
print(name)

#if / statement
if age < 100:
    print("You are not that old")
    print('Im using indententation')
elif age == 100: #else if
    print("You are 100 years old")
else:
    print("You are really old")

#functions

def sayHello():
    print("Hello World")

def sayGoodbye(name):
    print("Goodbye World")


#call functions
sayHello()
sayGoodbye("Blue")

#arrays are called lists

colors = ["red", "blue", "green"]

# add an element

colors.append("yellow")
print(colors)

colors.remove("red")
print(colors)


#for loop
for col in colors:
    print(col)
#for(let i=0; i<colors.length; i++)
#let temp = colors[i]
#print(temp)


#dictionaries

me = {
    "name": "Blue",
    "last_name": "X",
    "age": 31,
    "woke": True
}

print(me["last_name"])

me["last_name"] = "Blacc"
print(me["last_name"])
me["favorite_color"] = "royal blue"
print(me["favorite_color"])
