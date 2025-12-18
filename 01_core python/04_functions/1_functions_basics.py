def hello_function():
    print("Hello Function!")

hello_function()

# Return
def hello_world():
    return('Hello, World!')

print(hello_world())

#Parameters and Arguments V1
def hello_func(greeting):
    return greeting

print(hello_func("Hi!"))

#Parameters and Arguments V2
def hello_func(greeting, name):
    return greeting + " " + name

print(hello_func('Good morning!,', 'Kelvin'))