#Function
def greet():
    print("Hello")
    print("Welcome to the 100 Days of Code Challenge")
    print("All the Best for the Challenge\n\n")

greet()

#Function with parameter
def greet_with_name(name):
    print(f"Hello, My name is {name}")
    print("Welcome to the 100 Days of Code Challenge")
    print("All the Best for the Challenge\n\n")


greet_with_name("Ram")

#Function with positional parameter
def greet_with_name(name,location):
    print(f"Hello, {name}")
    print(f"what it is like living in {location}")


greet_with_name("Ram","India")

#Function with Keyword parameter
greet_with_name(location="India",name="Ram")