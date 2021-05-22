'''
string = "Hello world"

print(type(string))

print(f"How many l's : {string.count('l')}")#returns the amount of character found in the string

print(f"Where is the e: {string.find('e')}")

print(f"Where is the a: {string.find('a')}")

print(f"Where is the w: {string.index('w')}")

try:
    print(f"Where is the x: {string.index('x')}")
except:
    print("Value not found")

number = int(input("Type and numer:"))

while number != -1:
    try:
        number = int(input("Type a number: "))
    except:
        print("I asked for a number not a word")

string = "This is a long string with different words and letters and number such as 51981240913"
listofWords = string.split()
print(string)
print(f"List of String: {listofWords}")



for word in range(len(listofWords)):
    print(listofWords[word])
print("-------------------")


for word in listofWords:
    print(word)
    

print("Using inerators in the string")
print(string[15:36:])#range{start,end,jump}

start = string.find("string")
end = string.find("words")
print(string[start:end])
'''
def function1():
    x = 10

print(type(function1))

def function2():
    def function3():
        print("1984 inside of function 3")
    return function3()

print(function2())
try:
    print(function3())
except:
    print("The function3 is local")
