askNameString = "Enter Your Name"
askAgeString = "Enter Your Age"
askUserNameString = "Enter Your Reddit User Name"

def smartInput(string):
    return input(string + ": ")
def ask(string, expectedType):
    
name = smartInput(askNameString)
age = smartInput(askAgeString)
userName = smartInput(askUserNameString)

print("Name is: " + name)
print("Age is: " + age)
print("UserName is: " + userName)

